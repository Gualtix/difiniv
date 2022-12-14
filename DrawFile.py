import win32gui
import win32api
import time
import win32con, win32ui


class Draw:

    def __init__(self):
        self.red    = win32api.RGB(255, 0, 0)
        self.green  = win32api.RGB(0, 255, 0)
        self.blue   = win32api.RGB(0, 0, 255)
        self.black  = win32api.RGB(0, 0, 0)
        self.white  = win32api.RGB(255, 255, 255)
        self.yellow = win32api.RGB(255, 255, 0)
        self.purple = win32api.RGB(255, 0, 255)
        self.cyan   = win32api.RGB(0, 255, 255)

    def draw_frame_by_sup_left_corner(self,x, y, width, height,color):
        dc = win32gui.GetDC(0)

        win32gui.SetPixel(dc, x, y, color)  # draw red at 0,0
        thickness = 3
        for i in range(x, x + width):

            for j in range(thickness):
                win32gui.SetPixel(dc, i, y + j, color)
                win32gui.SetPixel(dc, i, y + height - j, color)

        for i in range(y, y + height):

            for j in range(thickness):
                win32gui.SetPixel(dc, x + j, i, color)
                win32gui.SetPixel(dc, x + width - j, i, color)
    
    def draw_frame_by_center(self,x, y, width, height,color):
        self.draw_frame_by_sup_left_corner((x - (width // 2)),(y - (height // 2)),width,height,color)

    

    


    def draw_text_at(self,x,y,text,color):
        hInstance = win32api.GetModuleHandle()
        className = 'MyWindowClassName'

        # http://msdn.microsoft.com/en-us/library/windows/desktop/ms633576(v=vs.85).aspx
        # win32gui does not support WNDCLASSEX.
        wndClass                = win32gui.WNDCLASS()
        # http://msdn.microsoft.com/en-us/library/windows/desktop/ff729176(v=vs.85).aspx
        wndClass.style          = win32con.CS_HREDRAW | win32con.CS_VREDRAW
        wndClass.lpfnWndProc    = self.wndProc
        wndClass.hInstance      = hInstance
        wndClass.hCursor        = win32gui.LoadCursor(None, win32con.IDC_ARROW)
        wndClass.hbrBackground  = win32gui.GetStockObject(win32con.WHITE_BRUSH)
        wndClass.lpszClassName  = className
        # win32gui does not support RegisterClassEx
        wndClassAtom = win32gui.RegisterClass(wndClass)

        # http://msdn.microsoft.com/en-us/library/windows/desktop/ff700543(v=vs.85).aspx
        # Consider using: WS_EX_COMPOSITED, WS_EX_LAYERED, WS_EX_NOACTIVATE, WS_EX_TOOLWINDOW, WS_EX_TOPMOST, WS_EX_TRANSPARENT
        # The WS_EX_TRANSPARENT flag makes events (like mouse clicks) fall through the window.
        exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT

        # http://msdn.microsoft.com/en-us/library/windows/desktop/ms632600(v=vs.85).aspx
        # Consider using: WS_DISABLED, WS_POPUP, WS_VISIBLE
        style = win32con.WS_DISABLED | win32con.WS_POPUP | win32con.WS_VISIBLE

        # http://msdn.microsoft.com/en-us/library/windows/desktop/ms632680(v=vs.85).aspx
        hWindow = win32gui.CreateWindowEx(
            exStyle,
            wndClassAtom,
            None, # WindowName
            style,
            0, # x
            0, # y
            win32api.GetSystemMetrics(win32con.SM_CXSCREEN), # width
            win32api.GetSystemMetrics(win32con.SM_CYSCREEN), # height
            None, # hWndParent
            None, # hMenu
            hInstance,
            None # lpParam
        )
        

        # http://msdn.microsoft.com/en-us/library/windows/desktop/ms633540(v=vs.85).aspx
        win32gui.SetLayeredWindowAttributes(hWindow, 0x00ffffff, 255, win32con.LWA_COLORKEY | win32con.LWA_ALPHA)


        # http://msdn.microsoft.com/en-us/library/windows/desktop/dd145167(v=vs.85).aspx
        #win32gui.UpdateWindow(hWindow)

        # http://msdn.microsoft.com/en-us/library/windows/desktop/ms633545(v=vs.85).aspx
        win32gui.SetWindowPos(hWindow, win32con.HWND_TOPMOST, 0, 0, 0, 0,
            win32con.SWP_NOACTIVATE | win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW)

        # http://msdn.microsoft.com/en-us/library/windows/desktop/ms633548(v=vs.85).aspx
        #win32gui.ShowWindow(hWindow, win32con.SW_SHOW)

        win32gui.PumpMessages()



    def wndProc(self,hWnd, message, wParam, lParam):
        if message == win32con.WM_PAINT:
            
            print("message  = ", wParam)
            hdc, paintStruct = win32gui.BeginPaint(hWnd)
            win32gui.SetTextColor(hdc,win32api.RGB(0,255,0))

            dpiScale = win32ui.GetDeviceCaps(hdc, win32con.LOGPIXELSX) / 60.0
            fontSize = 80

            # http://msdn.microsoft.com/en-us/library/windows/desktop/dd145037(v=vs.85).aspx
            lf = win32gui.LOGFONT()
            lf.lfFaceName = "Consolas"
            lf.lfHeight = int(round(dpiScale * fontSize)) 
            #lf.lfWeight = 150
            # Use nonantialiased to remove the white edges around the text.
            
            lf.lfQuality = win32con.NONANTIALIASED_QUALITY
            hf = win32gui.CreateFontIndirect(lf)
            win32gui.SelectObject(hdc, hf)

            rect = win32gui.GetClientRect(hWnd)
            # http://msdn.microsoft.com/en-us/library/windows/desktop/dd162498(v=vs.85).aspx
            win32gui.DrawText(
                hdc,
                'Text on the screen',
                -1,
                rect,
                win32con.DT_CENTER | win32con.DT_NOCLIP | win32con.DT_SINGLELINE | win32con.DT_VCENTER
            )
            win32gui.EndPaint(hWnd, paintStruct)
            
            return 0

        elif message == win32con.WM_DESTROY:
            print ('Closing the window.')
            win32gui.PostQuitMessage(0)
            return 0

        else:
            return win32gui.DefWindowProc(hWnd, message, wParam, lParam)

    



    





