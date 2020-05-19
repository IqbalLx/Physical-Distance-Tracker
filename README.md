# Physical-Distance-Tracker
![Automated CCTV Surveilance System to track Physical Distancing in crowded place using Image Processing](https://github.com/IqbalLx/Physical-Distance-Tracker/blob/master/sample/measure%20distance.jpg)

## Overview
In this project I build a surveilance CCTV cam to track physical distancing in a crowded place, like market, mall, etc that still crowded in the middle of pandemic, so hopefully with this system installed, the police or the guard of the place can easily know if people on that area following the rule or not to set a safe distance between people, so they can take action if there are too much people who violate the rule, because we need to work together to flatten the curve.
<br/>

[![Overview Video](http://img.youtube.com/vi/72GsLfNPAME/0.jpg)](http://www.youtube.com/watch?v=72GsLfNPAME)
<br/>
_english version of video added later_

## Guide
- Download faster rcnn model from TensorFlow Model Zoo here - https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md
- Create new folder called `physicaldistance` on your Drive and move the model there along with `sample.mp4` from sample directory above
- You can directly try to run the `Physical_Distance_Tracker.ipynb` on Google Colab
- or You can playing arround with warped view code in `transform.py` and selecting threshold/safe distance code in `points distance.py`

You can watch this video for more technical guide
<br/>
[![Overview Video](http://img.youtube.com/vi/tdnYdTUsP38/0.jpg)](http://www.youtube.com/watch?v=tdnYdTUsP38)
<br/>
_english version of video added later_

## Reference
- Physical Distancing Tracker by Landing AI - https://landing.ai/landing-ai-creates-an-ai-tool-to-help-customers-monitor-social-distancing-in-the-workplace
- Real Time Human Detection using TensorFlow - https://medium.com/@madhawavidanapathirana/real-time-human-detection-in-computer-vision-part-2-c7eda27115c6
- 4 Point Transform OpenCV - https://www.pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/
- Measuring Distance in OpenCV - https://www.pyimagesearch.com/2016/04/04/measuring-distance-between-objects-in-an-image-with-opencv/

> I want to thank to Bisa AI (https://bisa.ai) through this repository for trusting me to be the first winner in their open competition: solving COVID-19 with Artificial Intelligence
