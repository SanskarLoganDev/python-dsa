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