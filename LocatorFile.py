import cv2
import pyautogui
import numpy as np
import imutils

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
    
    

    def multi_scale_locator(self, template_url,enviroment_url):

        original = cv2.imread(enviroment_url)

        template = cv2.imread(template_url)
        template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        template = cv2.Canny(template, 50, 200)
        template_height, template_width = template.shape[:2]
        #cv2.imshow('Template', template)
        #cv2.waitKey(0)

        enviroment = cv2.imread(enviroment_url)
        enviroment = cv2.cvtColor(enviroment, cv2.COLOR_BGR2GRAY)
        enviroment = cv2.Canny(enviroment, 50, 200)
        enviroment_height, enviromente_width = enviroment.shape[:2]
        #cv2.imshow('Enviroment', enviroment)
        #cv2.waitKey(0)

        rectangles = []
        threshold = 0.13
        
        # Iteracion  sobre 20 escalas diferentes entre 0.2 y 1
        for scale in np.linspace(0.2, 1.0, 20)[::-1]:
            # Redimension de la imagen con base a la escala actual.
            resized = imutils.resize(template, width=int(template.shape[1] * scale))
            w, h = resized.shape[:2]

            #result = cv2.matchTemplate(enviroment,resized, cv2.TM_CCOEFF_NORMED)
            
            result = cv2.matchTemplate(enviroment,resized, cv2.TM_CCOEFF)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

            #yloc, xloc = np.where(result >= threshold)
            
            
            #for (x, y) in zip(xloc, yloc):
                #rectangles.append([int(x), int(y), int(w), int(h)])
                #rectangles.append([int(x), int(y), int(w), int(h)])
            
            rectangles.append([int(max_loc[0]), int(max_loc[1]), int(w), int(h)])
            rectangles.append([int(max_loc[0]), int(max_loc[1]), int(w), int(h)])
            
            #print("Rectangles: ", len(rectangles))
        
        rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
        for (x,y,w,h) in rectangles:
            cv2.rectangle(original, (x,y), (x+w, y+h), (0,255,255), 2)
        
        cv2.imshow('Imagen', original)
        cv2.waitKey(0)
        
        
        





    

    


