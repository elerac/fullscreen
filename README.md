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

image = cv2.imread("image.png", 1)

window.imshow(image)
cv2.waitKey(0)
window.destroyWindow()
```