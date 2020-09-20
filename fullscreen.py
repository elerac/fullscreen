import cv2
import numpy as np
import screeninfo
import os

class FullScreen:
    """
    Display the image in full screen
    """
    def __init__(self, monitor_id):
        """
        Parameters
        ----------
        monitor_id : int
            Monitor ID (0, 1, ...)
        """
        self.monitor = screeninfo.get_monitors()[monitor_id]
        self.width = self.monitor.width
        self.height = self.monitor.height
        self.x = self.monitor.x
        self.y = self.monitor.y
        self.name = str(monitor_id)

        self._interpolation = cv2.INTER_NEAREST
        
        cv2.namedWindow(self.name, cv2.WINDOW_NORMAL)
        cv2.moveWindow(self.name, self.x, self.y)
        cv2.setWindowProperty(self.name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        #Foce the image window to appear on top (MacOS only)
        if os.name == "posix":
            import subprocess
            subprocess.call(["/usr/bin/osascript", "-e", 'tell app "Finder" to set frontmost of process "Python" to true'])

        self.imshow(0)
        cv2.waitKey(100)

    def imshow(self, image):
        """
        Imshow

        Parameters
        ----------
        image : np.ndarray, int, float, tuple, list
            Image to be display
        """
        # Single int value case
        if type(image)==int:
            image = image/255.0

        # Single float value case
        if type(image)==float:
            image = (image, image, image)
        
        # RGB value case
        if isinstance(image, (tuple, list)):
            if len(image)==3:
                image = np.full((self.height, self.width, 3), image)
                if image.dtype==np.int64:
                    image = image/255.0
            else:
                raise ValueError(f"The length of the {type(image)} must be 3: {len(image)}")

        # Image case
        if type(image)==np.ndarray:
            if image.shape[0]!=self.height or image.shape[1]!=self.width:
                image = cv2.resize(image, (self.width, self.height), interpolation=self._interpolation)
        else:
            raise TypeError(f"'image' must be 'np.ndarray' type: {type(image)}")

        cv2.imshow(self.name, image)

    def destroyWindow(self):
        cv2.destroyWindow(self.name)

def main():
    import argparse
    import time
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, default=None, help="Image file path")
    parser.add_argument("-v", "--value", type=int, default=None, help="Display value (0-255). The '-f' option takes precedence.")
    parser.add_argument("-i", "--id", type=int, default=0, help="Monitor ID")
    args = parser.parse_args()

    monitor_id = args.id
    win = FullScreen(monitor_id)

    width = win.width
    height = win.height
    
    # '-f' option case
    if args.file is not None:
        image= cv2.imread(args.file)
        if image is None: raise FileNotFoundError(f"{args.file} couldn't be loaded")
    # '-v' option case
    elif args.value is not None:
        image = args.value
    # No option case
    else:
        image = np.fromfunction(lambda y, x, c: 255*(c==0)+x/width*255*(c==1)+y/height*255*(c==2), (height, width, 3)).astype(np.uint8)

    win.imshow(image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()
