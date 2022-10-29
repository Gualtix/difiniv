from turtle import width
from DrawFile import Draw
from LocatorFile import Locator

def main():

    Lc = Locator()
    Lc.multi_scale_locator('./Img/templates/chrome.png','./Img/enviroments/desktop_2.png')

if __name__ == "__main__":
    main()

































#x,y,width,height = Lc.locate('./Img/specific/gmail_icon.png')
#if(x != -1 and y != -1):
#        D = Draw()
#        D.draw_frame_by_center(x,y,width,height,D.green)