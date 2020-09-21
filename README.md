# FullScreen

Display the image in full screen.

## Requirement
* [screeninfo](https://github.com/rr-/screeninfo)
* OpenCV

## Usage
```python
import cv2
from fullscreen import *

screen = FullScreen(0)
width  = screen.width
height = screen.height

image = cv2.imread("image.png", 1)

screen.imshow(image)
cv2.waitKey(0)
screen.destroyWindow()
```
