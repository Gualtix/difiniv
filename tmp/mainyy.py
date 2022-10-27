import sys
import time
import win32ui
import win32con
import win32print


def get_data_strings():
    rows = (("PETER PAUL", "MALE", "100000"), ("MARGARET ", "FEMALE", "1000"), ("MICHAEL JORDAN", "MALE", "1"),("AGNES", "FEMALE", "200"))
    return ["{:20} {:8} {}".format(*row) for row in rows]


def text():
    return "\r\n".join(get_data_strings())


def paint_dc(dc, printer_dc, paint_each_string=True):
    scale_factor = 20
    if printer_dc:
        x_y = 100, 0  # TopLeft of the page. In order to move away from the point, X increases to positives, while Y to negatives
        font_scale = 10
        y_direction_scale = -1  # For printers, the Y axis is "reversed"
        y_ellipsis = -100
    else:
        x_y = 100, 150  # TopLeft from wnd's client area
        font_scale = 1
        y_direction_scale = 1
        y_ellipsis = 100

    font0 = win32ui.CreateFont(
        {
            "name": "Lucida Console",
            "height": scale_factor * font_scale,
            "weight": 400,
        })
    font1 = win32ui.CreateFont(
        {
            "name": "algerian",
            "height": scale_factor * font_scale,
            "weight": 400,
        })
    fonts = [font0, font1]
    dc.SelectObject(font0)
    dc.SetTextColor(0x0000FF00) # 0BGR
    #dc.SetBkColor(0x000000FF)
    dc.SetBkMode(win32con.TRANSPARENT)
    if paint_each_string:
        for idx, txt in enumerate(get_data_strings()):
            dc.SelectObject(fonts[idx % len(fonts)])
            dc.TextOut(x_y[0], x_y[1] + idx * scale_factor * font_scale * y_direction_scale, txt)
    else:
        dc.TextOut(*x_y, text())
    pen = win32ui.CreatePen(0, 0, 0)
    dc.SelectObject(pen)
    dc.Ellipse((50, y_ellipsis, *x_y))


def paint_wnd(wnd, paint_each_string=True):
    dc = wnd.GetWindowDC()
    paint_dc(dc, False, paint_each_string=paint_each_string)
    wnd.ReleaseDC(dc)


def paint_prn(printer_name, paint_each_string=True):
    printer_name = printer_name or win32print.GetDefaultPrinter()
    dc = win32ui.CreateDC()
    dc.CreatePrinterDC(printer_name)
    dc.SetMapMode(win32con.MM_TWIPS)
    dc.StartDoc("Win32print")
    #dc.StartPage()
    paint_dc(dc, True, paint_each_string=paint_each_string)
    #dc.EndPage()
    dc.EndDoc()

def get_data_strings():
    rows = (("PETER PAUL", "MALE", "100000"), ("MARGARET ", "FEMALE", "1000"), ("MICHAEL JORDAN", "MALE", "1"),("AGNES", "FEMALE", "200"))
    return ["{:20} {:8} {}".format(*row) for row in rows]   


def main():
    print("Python {:s} on {:s}\n".format(sys.version, sys.platform))
    print(text())
    time.sleep(0.1)
    if len(sys.argv) > 1:
        if sys.argv[1] == "window":
            paint_func = paint_wnd
            paint_func_dc_arg = win32ui.GetForegroundWindow()
        else:
            paint_func = paint_prn
            paint_func_dc_arg = sys.argv[1]
    else:
        paint_func = paint_prn
        paint_func_dc_arg = None
    paint_func(paint_func_dc_arg, paint_each_string=True)


if __name__ == "__main__":
    dc = win32ui.CreateDC()

    dc.CreatePrinterDC("Microsoft Print to PDF")
    dc.SetMapMode(win32con.MM_TWIPS)
    #dc.StartDoc("Win32print")


    scale_factor = 20
    font_scale = 10

    y_ellipsis = 100
    x_y = 100, 150

    font0 = win32ui.CreateFont(
        {
            "name": "Lucida Console",
            "height": scale_factor * font_scale,
            "weight": 400,
        })
    dc.SelectObject(font0)
    dc.SetTextColor(0x0000FF00) # 0BGR
    dc.SetBkMode(win32con.TRANSPARENT)

    #dc.TextOut(*x_y, text())
    #pen = win32ui.CreatePen(0, 0, 0)
    #dc.SelectObject(pen)
    #dc.Ellipse((50, y_ellipsis, *x_y))
    #dc.EndDoc()
    
    for idx, txt in enumerate(get_data_strings()):
        dc.SelectObject(font0)
        dc.TextOut(100, 0 + idx * scale_factor * font_scale * -1, txt)
        time.sleep(1)


    #main()