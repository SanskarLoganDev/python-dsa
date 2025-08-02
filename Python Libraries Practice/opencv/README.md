The cv2.VideoCapture.get() method in OpenCV allows retrieval of various properties of a video stream or camera. These properties are identified by an integer index or, more commonly, by a symbolic constant from the cv2.CAP_PROP_ enumeration. Not all properties are applicable or supported by every video source or device.

Here is a list of common cv2.CAP_PROP_ properties and their corresponding integer numbers:

0: cv2.CAP_PROP_POS_MSEC: Current position of the video file in milliseconds.
1: cv2.CAP_PROP_POS_FRAMES: 0-based index of the frame to be decoded/captured next.
2: cv2.CAP_PROP_POS_AVI_RATIO: Relative position of the video file (0.0 - 1.0).
3: cv2.CAP_PROP_FRAME_WIDTH: Width of the frames in the video stream.
4: cv2.CAP_PROP_FRAME_HEIGHT: Height of the frames in the video stream.
5: cv2.CAP_PROP_FPS: Frame rate (frames per second).
6: cv2.CAP_PROP_FOURCC: 4-character code of codec.
7: cv2.CAP_PROP_FRAME_COUNT: Number of frames in the video file.
8: cv2.CAP_PROP_FORMAT: Format of the Mat objects returned by retrieve().
9: cv2.CAP_PROP_MODE: Backend-specific value indicating the current capture mode.
10: cv2.CAP_PROP_BRIGHTNESS: Brightness of the image (only for cameras).
11: cv2.CAP_PROP_CONTRAST: Contrast of the image (only for cameras).
12: cv2.CAP_PROP_SATURATION: Saturation of the image (only for cameras).
13: cv2.CAP_PROP_HUE: Hue of the image (only for cameras).
14: cv2.CAP_PROP_GAIN: Gain of the image (only for cameras).
15: cv2.CAP_PROP_EXPOSURE: Exposure of the image (only for cameras).
16: cv2.CAP_PROP_CONVERT_RGB: Boolean flags indicating whether images should be converted to RGB.
17: cv2.CAP_PROP_WHITE_BALANCE_BLUE_U: White balance blue U component (only for cameras).
18: cv2.CAP_PROP_RECTIFICATION: Rectification flag for stereo cameras.


Parameters for detectMultiScale:

void CascadeClassifier::detectMultiScale(
    const Mat& image, 
    vector<Rect>& objects, 
    double scaleFactor=1.1,
    int minNeighbors=3, 
    int flags=0, 
    Size minSize=Size(),
    Size maxSize=Size() )

1) scaleFactor – Parameter specifying how much the image size is reduced at each image scale.

Basically the scale factor is used to create your scale pyramid. More explanation can be found here. In short, as described here, your model has a fixed size defined during training, which is visible in the xml. This means that this size of face is detected in the image if present. However, by rescaling the input image, you can resize a larger face to a smaller one, making it detectable by the algorithm.

1.05 is a good possible value for this, which means you use a small step for resizing, i.e. reduce size by 5%, you increase the chance of a matching size with the model for detection is found. This also means that the algorithm works slower since it is more thorough. You may increase it to as much as 1.4 for faster detection, with the risk of missing some faces altogether.

2) minNeighbors – Parameter specifying how many neighbors each candidate rectangle should have to retain it.

This parameter will affect the quality of the detected faces. Higher value results in less detections but with higher quality. 3~6 is a good value for it.

3) minSize – Minimum possible object size. Objects smaller than that are ignored.

This parameter determine how small size you want to detect. You decide it! Usually, [30, 30] is a good start for face detection.

4) maxSize – Maximum possible object size. Objects bigger than this are ignored.

This parameter determine how big size you want to detect. Again, you decide it! Usually, you don't need to set it manually, the default value assumes you want to detect without an upper limit on the size of the face.