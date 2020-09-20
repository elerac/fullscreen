import cv2
from fullscreen import FullScreen

screen = FullScreen(0)

DELAY = 1200 #ms

filename = "image/himeji_castle.jpg"
image = cv2.imread(filename, 1)


# Single int
screen.imshow(200)
cv2.waitKey(DELAY)

# Single float
screen.imshow(0.2)
cv2.waitKey(DELAY)

# RGB int tuple
screen.imshow((255, 100, 100))
cv2.waitKey(DELAY)

# RGB flot tuple
screen.imshow((0.4, 1.0, 0.4))
cv2.waitKey(DELAY)

# RGB int list
screen.imshow([100, 100, 255])
cv2.waitKey(DELAY)

# RGB float list
screen.imshow([0.2, 0.8, 1.0])
cv2.waitKey(DELAY)

# Image case
screen.imshow(image)
cv2.waitKey(DELAY)


screen.destroyWindow()