from turtle import width
from DrawFile import Draw
from LocatorFile import Locator

def main():

    Lc = Locator()
    #Lc.multi_scale_locator('./Img/templates/chrome.png','./Img/enviroments/desktop_1.png')

    Dw = Draw()
    Dw.draw_text_at(100,100,'Text on the screen',Dw.green)

if __name__ == "__main__":
    main()

































#x,y,width,height = Lc.locate('./Img/specific/gmail_icon.png')
#if(x != -1 and y != -1):
#        D = Draw()
#        D.draw_frame_by_center(x,y,width,height,D.green)