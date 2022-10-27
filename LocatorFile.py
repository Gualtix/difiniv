import cv2
import pyautogui


#x, y = pyautogui.locateCenterOnScreen('calc7key.png')

class Locator:

    def __init__(self):
        self.x = -1
        self.y = -1
    
    def locate(self, image):
        img = cv2.imread(image)
        dimensions = img.shape
        print(dimensions)
        try:
            self.x, self.y = pyautogui.locateCenterOnScreen(image,confidence=0.90)
            print("x: ", self.x, "y: ", self.y)
        except:
            print("Image not found")
        return self.x, self.y, dimensions[1], dimensions[0]
    
    def locate_by_template(self,):
        pass

    

    


