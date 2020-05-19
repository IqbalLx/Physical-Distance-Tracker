import cv2
import numpy as np

def euclidean_dist(a, b):
    return np.sqrt((a[1] - b[1])**2 + (a[0] - b[0])**2)

#Transforming into bird's eye view
def transform(img, points):
    #Ordering points
    #rect = order_points(points)
    tl, tr, br, bl = points

    #Construct bird's eye image matrix
    #I want it vertical, so it'll find minimum width
    #between distance for tl to tr and bl to br
    upperW = euclidean_dist(tl, tr)
    lowerW = euclidean_dist(bl, br)
    minW = min(upperW, lowerW)

    #And max height between distance for tl to bl
    #and tr to br
    upperH = euclidean_dist(tl, bl)
    lowerH = euclidean_dist(tr, br)
    maxH = max(upperH, lowerH)

    #Put all the information
    tmp = np.array([
        [0, 0],
        [minW-1, 0],
        [minW-1, maxH-1],
        [0, maxH-1]
    ], dtype='float32')

    #Warping and transform
    M = cv2.getPerspectiveTransform(points, tmp)
    warped = cv2.warpPerspective(img, M, (int(minW), int(maxH)))

    return warped, M

#Handling reference points
ref_pts = []
def make_points(event, x, y, flags, param):
    global ref_pts

    #Handling mouse click
    if event == cv2.EVENT_LBUTTONDOWN:
        ref_pts.append([x, y])
        #print(ref_pts)

    elif event == cv2.EVENT_LBUTTONUP:
        for pts in ref_pts:
            cv2.circle(img, (pts[0], pts[1]), 5, (0, 0, 255), 3)
            cv2.imshow('Preview', img)

#Load image
img = cv2.imread('sample/sample-ss.jpg')

#Resizing Image
height, width = img.shape[:2]
baseW= 640
newH = (baseW / width) * height
img = cv2.resize(img, (baseW, int(newH)), interpolation= cv2.INTER_LINEAR)

#Duplicate img
clone = img.copy()

#Set callbacks
cv2.namedWindow('Preview')
cv2.setMouseCallback('Preview', make_points)

#Showing Image
show_dist = True
while True:
    cv2.imshow('Preview', img)

    #Draw rect after 4 points 
    if len(ref_pts) == 2:
        #warp_img = transform(clone.copy(), np.array(ref_pts, dtype='float32'))
        warp_img, mat = transform(clone.copy(), np.array([[353, 11], [618, 13], [530, 350], [4, 217]], dtype='float32'))
        for pts in ref_pts:
            src = np.array(pts, dtype='float32').reshape(1, 1, 2)
            dst = np.zeros((1, 2), dtype='float32')

            warp_pts = cv2.perspectiveTransform(src, mat, dst).reshape(2,)
            cv2.circle(warp_img, (warp_pts[0], warp_pts[1]), 5, (0, 0, 255), 3)
            cv2.imshow('Warped', warp_img)
        
        if show_dist:
            show_dist= False
            distance = euclidean_dist(ref_pts[0], ref_pts[1])
            print(f'[INFO] Distance betwwen points: {distance}\n')
            cv2.line(warp_img, tuple(ref_pts[0]), tuple(ref_pts[1]), (255, 0, 0), 2)
            #cv2.putText(img, "Close contact: ", (23, 23), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 1)

    #Handling key press
    key = cv2.waitKey(1) & 0xff
    if key == ord('r'):
        img = clone.copy()
        ref_pts = []
        show_dist = True
    elif key == ord('x'):
        break

cv2.destroyAllWindows()