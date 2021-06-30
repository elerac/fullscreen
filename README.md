# FullScreen
Display image in fullscreen for the projector-camera system.

Python has some GUI tools, but only a few of them are suitable for fullscreen display. In this repository, *Tkinter* or *OpenCV* is used as the backend. The best backend depends on the environment (i.e. OS, monitor, version of software), so choose the best one for you.

## Requirement
### Tkinter backend (default)
- Pillow (PIL)

### OpenCV backend (optional)
- OpenCV
- screeninfo (from https://github.com/rr-/screeninfo)

## Usage

### Basic imshow
```python
import time
import cv2
from fullscreen import FullScreen

screen = FullScreen()

image = cv2.imread("image/himeji_castle.jpg", 1)

screen.imshow(image)

time.sleep(3)
```

### Get the size of the screen
```python
height, width, ch = screen.shape
```

### Choosing backend
```python
screen = FullScreen(backend="tkinter") # default
```
```python
screen = FullScreen(backend="cv2")
```

## Testing environment
✅ macOS (Catalina), MacBook Pro (13-inch, 2017), Tkinter

✅ macOS (Catalina), MacBook Pro (13-inch, 2017), OpenCV-Python (4.4)

❌ macOS (Catalina), MacBook Pro (13-inch, 2017), OpenCV-Python (4.5)

✅  macOS (BigSur), MacBook Pro (13-inch, 2017), Tkinter

❌ macOS (BigSur), MacBook Pro (13-inch, 2017), OpenCV-Python (4.4)

❌ macOS (BigSur), MacBook Pro (13-inch, 2017), OpenCV-Python (4.5)

✅  macOS (BigSur), MacPro (2019), OpenCV-Python (4.4)

Although I have only tested on Mac, it should also work on Windows and Ubuntu as the software is cross-platform.

## ToDo
- Stable support for multiple monitors.
- OpenGL (or Metal?) based fullscreen imshow (like [kamino410/gl_imshow](https://github.com/kamino410/gl_imshow)) on **macOS** for faster rendering.