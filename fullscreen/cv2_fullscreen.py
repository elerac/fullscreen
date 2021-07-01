import numpy as np
import cv2
import screeninfo # https://github.com/rr-/screeninfo

class FullScreen:
    """Full-screen with OpenCV High-level GUI backend
    """
    
    delay : int = 1 # internal delay time after imshow

    def __init__(self, screen_id: int = 0):
        self.monitor = screeninfo.get_monitors()[screen_id]
        self.width = self.monitor.width
        self.height = self.monitor.height
        self.x = self.monitor.x
        self.y = self.monitor.y
        self.name = str(screen_id)
        
        cv2.namedWindow(self.name, cv2.WINDOW_NORMAL)
        cv2.moveWindow(self.name, self.x, self.y)
        cv2.resizeWindow(self.name, self.width, self.height)
        cv2.setWindowProperty(self.name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        # set initial image
        img_gray = np.full((self.height, self.width), 127, dtype=np.uint8)
        self.imshow(img_gray)
        cv2.waitKey(750) # first imshow require long delay time
    
    @property
    def shape(self):
        return self.height, self.width, 3

    def imshow(self, image: np.ndarray):
        # Single int value case
        if type(image) == int:
            image = image/255.0

        # Single float value case
        if type(image) == float:
            image = (image, image, image)
        
        # RGB value case
        if isinstance(image, (tuple, list)):
            if len(image) == 3:
                image = np.full((self.height, self.width, 3), image)
                if image.dtype == np.int64:
                    image = image/255.0
            else:
                raise ValueError(f"The length of the {type(image)} must be 3: {len(image)}")

        # Image case
        if type(image) == np.ndarray:
            if image.shape[0] != self.height or image.shape[1] != self.width:
                image = cv2.resize(image, (self.width, self.height), interpolation=cv2.INTER_NEAREST)
        else:
            raise TypeError(f"'image' must be 'np.ndarray' type: {type(image)}")

        cv2.imshow(self.name, image)
        cv2.waitKey(self.delay)
        cv2.waitKey(self.delay) # magic

    def destroyWindow(self):
        cv2.destroyWindow(self.name)
