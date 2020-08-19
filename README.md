# FullScreen

Display the image in full screen.

## Requirement
* [screeninfo](https://github.com/rr-/screeninfo)
* OpenCV

## Usage
```python
import cv2
from fullscreen import FullScreen

monitor_id = 0
window = FulScreen(monitor_id)
width  = window.width
height = window.height

img_src = cv2.imread("image.png", 1)
img_resized = cv2.resize(img_src, (width, height))

window.imshow(img_resized)
cv2.waitKey(0)
windos.destroyWindow()
```