import cv2
from fullscreen import FullScreen

win = FullScreen(0)

DELAY = 1200 #ms

filename = "image/himeji_castle.jpg"
image = cv2.imread(filename, 1)


# Single int
win.imshow(200)
cv2.waitKey(DELAY)

# Single float
win.imshow(0.2)
cv2.waitKey(DELAY)

# RGB int tuple
win.imshow((255, 100, 100))
cv2.waitKey(DELAY)

# RGB flot tuple
win.imshow((0.4, 1.0, 0.4))
cv2.waitKey(DELAY)

# RGB int list
win.imshow([100, 100, 255])
cv2.waitKey(DELAY)

# RGB float list
win.imshow([0.2, 0.8, 1.0])
cv2.waitKey(DELAY)

# Image case
win.imshow(image)
cv2.waitKey(DELAY)


win.destroyWindow()
