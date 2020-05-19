import cv2
import numpy as np

#Transforming into bird's eye view
def transform(img, points):
    #Ordering points
    #rect = order_points(points)
    tl, tr, br, bl = points

    #Construct bird's eye image matrix
    #I want it vertical, so it'll find minimum width
    #between distance for tl to tr and bl to br
    upperW = np.sqrt((tl[1] - tr[1])**2 + (tl[0] - tr[0])**2)
    lowerW = np.sqrt((bl[1] - br[1])**2 + (bl[0] - br[0])**2)
    minW = min(upperW, lowerW)

    #And max height between distance for tl to bl
    #and tr to br
    upperH = np.sqrt((tl[1] - bl[1])**2 + (tl[0] - bl[0])**2)
    lowerH = np.sqrt((tr[1] - br[1])**2 + (tr[0] - br[0])**2)
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

    return warped

#Handling reference points
ref_pts = []
def make_points(event, x, y, flags, param):
    global ref_pts

    #Handling mouse click
    if event == cv2.EVENT_LBUTTONDOWN:
        ref_pts.append([x, y])

    elif event == cv2.EVENT_LBUTTONUP:
        #draw circle in every points clicked
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
show_info = True
while True:
    cv2.imshow('Preview', img)

    #Draw rect after 4 points 
    if len(ref_pts) == 4:
        tl, tr, br, bl = ref_pts
        tl, tr, br, bl = tuple(tl), tuple(tr), tuple(br), tuple(bl)
        cv2.line(img, tl, tr, (0, 255, 0), 2)
        cv2.line(img, tr, br, (0, 255, 0), 2)
        cv2.line(img, br, bl, (0, 255, 0), 2)
        cv2.line(img, bl, tl, (0, 255, 0), 2)

        #warp_img = transform(clone.copy(), np.array(ref_pts, dtype='float32'))
        warp_img = transform(clone.copy(), np.array(ref_pts, dtype='float32'))
        cv2.imshow('Warped', warp_img)

        if show_info:
            show_info=False
            print(f'[INFO] Transformed image size: {warp_img.shape[:2]}')
            print(f'[INFO] Reference Point: {ref_pts}\n')

    #Handling key press
    key = cv2.waitKey(1) & 0xff
    if key == ord('r'):
        img = clone.copy()
        ref_pts = []
        show_info = True
    elif key == ord('x'):
        break

cv2.destroyAllWindows()