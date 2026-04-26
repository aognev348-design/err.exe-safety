import tkinter as tk
from tkinter import messagebox
import time
import ctypes
import random
import sys
import math
from ctypes import wintypes

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32
screen_w = user32.GetSystemMetrics(0)
screen_h = user32.GetSystemMetrics(1)
SRCCOPY = 0x00CC0020
NOTSRCCOPY = 0x00550009
IDI_HAND = 32513

def show_warning():
    root = tk.Tk()
    root.withdraw()
    response = messagebox.showwarning("⚠️ ВНИМАНИЕ ⚠️", "hi! this is a safe malware virus, it doesn't hurt your computer. It's just GDI effects, but if you're an epileptic, it's recommended not to run the program because it has effects that can be dangerous for epileptics. do you want to run the program?", icon='warning')
    if response == 'ok':
        confirm = messagebox.askyesno("Подтверждение", "this is serious, the virus can cause harm to epileptics, DO YOU REALLY WANT TO LAUNCH THE PROGRAM? the author is not responsible for damage by this GDI Virus", icon='question')
        if confirm:
            root.destroy()
            return True
    root.destroy()
    return False

disco_colors = [0x0000FF, 0x00FF00, 0xFF0000, 0x00FFFF, 0xFF00FF, 0xFFFF00, 0x0080FF, 0x8000FF]

def draw_half_transparent_rect(x, y, w, h, color):
    hdc = user32.GetDC(0)
    brush = gdi32.CreateSolidBrush(color)
    rect = ctypes.create_string_buffer(16)
    rect_ptr = ctypes.cast(rect, ctypes.POINTER(ctypes.c_long))
    rect_ptr[0] = x
    rect_ptr[1] = y
    rect_ptr[2] = x + w
    rect_ptr[3] = y + h
    user32.FillRect(hdc, ctypes.byref(rect), brush)
    for i in range(y, y + h, 4):
        pen = gdi32.CreatePen(0, 1, 0xFFFFFF)
        gdi32.SelectObject(hdc, pen)
        gdi32.MoveToEx(hdc, x, i, None)
        gdi32.LineTo(hdc, x + w, i)
        gdi32.DeleteObject(pen)
    gdi32.DeleteObject(brush)
    user32.ReleaseDC(0, hdc)

def disco_background():
    draw_half_transparent_rect(0, 0, screen_w, screen_h, random.choice(disco_colors))

def shake_disco():
    hdc = user32.GetDC(0)
    dx, dy = random.randint(-10, 10), random.randint(-10, 10)
    gdi32.BitBlt(hdc, dx, dy, screen_w, screen_h, hdc, 0, 0, SRCCOPY)
    user32.ReleaseDC(0, hdc)

def bulge_effect_disco():
    hdc = user32.GetDC(0)
    w, h = random.randint(200, screen_w), random.randint(200, screen_h)
    x1, y1 = (screen_w - w) // 2, (screen_h - h) // 2
    x2, y2 = random.randint(0, screen_w - w), random.randint(0, screen_h - h)
    gdi32.StretchBlt(hdc, x1, y1, w, h, hdc, x2, y2, w, h, SRCCOPY)
    user32.ReleaseDC(0, hdc)

def draw_disco_icon():
    x, y = random.randint(0, screen_w - 40), random.randint(0, screen_h - 40)
    color = random.choice(disco_colors)
    hdc = user32.GetDC(0)
    brush = gdi32.CreateSolidBrush(color)
    gdi32.SelectObject(hdc, brush)
    gdi32.Ellipse(hdc, x, y, x + 40, y + 40)
    for i in range(y, y + 40, 4):
        pen = gdi32.CreatePen(0, 1, 0xFFFFFF)
        gdi32.SelectObject(hdc, pen)
        gdi32.MoveToEx(hdc, x, i, None)
        gdi32.LineTo(hdc, x + 40, i)
        gdi32.DeleteObject(pen)
    gdi32.DeleteObject(brush)
    user32.ReleaseDC(0, hdc)

IDI_ERROR = 32513
icon_error = user32.LoadIconW(None, IDI_ERROR)

def draw_error_icon():
    hdc = user32.GetDC(0)
    x = random.randint(0, screen_w - 32)
    y = random.randint(0, screen_h - 32)
    user32.DrawIcon(hdc, x, y, icon_error)
    user32.ReleaseDC(0, hdc)

def shake_error():
    hdc = user32.GetDC(0)
    dx = random.randint(-10, 10)
    dy = random.randint(-10, 10)
    gdi32.BitBlt(hdc, dx, dy, screen_w, screen_h, hdc, 0, 0, SRCCOPY)
    user32.ReleaseDC(0, hdc)

def bulge_effect_error():
    hdc = user32.GetDC(0)
    w = random.randint(200, screen_w)
    h = random.randint(200, screen_h)
    x1 = (screen_w - w) // 2
    y1 = (screen_h - h) // 2
    x2 = random.randint(0, screen_w - w)
    y2 = random.randint(0, screen_h - h)
    gdi32.StretchBlt(hdc, x1, y1, w, h, hdc, x2, y2, w, h, SRCCOPY)
    user32.ReleaseDC(0, hdc)

def draw_text():
    hdc = user32.GetDC(0)
    if not hdc:
        return
    x = random.randint(0, screen_w - 300)
    y = random.randint(0, screen_h - 80)
    color = random.randint(0, 0xFFFFFF)
    stretch = random.uniform(1.2, 2.5)
    font = gdi32.CreateFontW(-48, int(20 * stretch), 0, 0, 400, 0, 0, 0, 0, 0, 0, 0, "Arial")
    if font:
        gdi32.SelectObject(hdc, font)
    gdi32.SetTextColor(hdc, color)
    gdi32.SetBkMode(hdc, 1)
    text = "err.exe"
    rect = (ctypes.c_long * 4)(x, y, x + 400, y + 100)
    user32.DrawTextW(hdc, text, -1, ctypes.byref(rect), 0)
    if font:
        gdi32.DeleteObject(font)
    user32.ReleaseDC(0, hdc)

def invert_screen():
    hdc = user32.GetDC(0)
    if hdc:
        gdi32.BitBlt(hdc, 0, 0, screen_w, screen_h, hdc, 0, 0, NOTSRCCOPY)
        user32.ReleaseDC(0, hdc)

def draw_text_fit():
    hdc = user32.GetDC(0)
    if not hdc:
        return
    x = random.randint(20, screen_w - 100)
    y = random.randint(20, screen_h - 35)
    font_size = random.randint(18, 24)
    font = gdi32.CreateFontW(-font_size, 0, 0, 0, 400, 0, 0, 0, 0, 0, 0, 0, "Arial")
    if font:
        gdi32.SelectObject(hdc, font)
    text = "err.exe"
    rect = (ctypes.c_long * 4)(0, 0, 0, 0)
    user32.DrawTextW(hdc, text, -1, ctypes.byref(rect), 0x00000400)
    text_width = rect[2] - rect[0]
    text_height = rect[3] - rect[1]
    padding = 3
    bg_rect = (ctypes.c_long * 4)(x - padding, y - padding, x + text_width + padding, y + text_height + padding)
    white_brush = gdi32.CreateSolidBrush(0xFFFFFF)
    user32.FillRect(hdc, ctypes.byref(bg_rect), white_brush)
    gdi32.DeleteObject(white_brush)
    pen = gdi32.CreatePen(0, 1, 0x000000)
    old_pen = gdi32.SelectObject(hdc, pen)
    gdi32.Rectangle(hdc, bg_rect[0], bg_rect[1], bg_rect[2], bg_rect[3])
    gdi32.SelectObject(hdc, old_pen)
    gdi32.DeleteObject(pen)
    text_color = random.choice([0x000000, 0x0000FF, 0x00FF00, 0xFF0000])
    gdi32.SetTextColor(hdc, text_color)
    gdi32.SetBkMode(hdc, 1)
    text_rect = (ctypes.c_long * 4)(x, y, x + text_width, y + text_height)
    user32.DrawTextW(hdc, text, -1, ctypes.byref(text_rect), 0)
    gdi32.DeleteObject(font)
    user32.ReleaseDC(0, hdc)

def shake_effect():
    hdc = user32.GetDC(0)
    dx = random.randint(-8, 8)
    dy = random.randint(-8, 8)
    gdi32.BitBlt(hdc, dx, dy, screen_w, screen_h, hdc, 0, 0, SRCCOPY)
    user32.ReleaseDC(0, hdc)

def blur_effect():
    hdc = user32.GetDC(0)
    for _ in range(4):
        dx = random.randint(-2, 2)
        dy = random.randint(-2, 2)
        gdi32.BitBlt(hdc, dx, dy, screen_w, screen_h, hdc, 0, 0, SRCCOPY)
    user32.ReleaseDC(0, hdc)

system_icon_ids = [32512, 32513, 32514, 32515, 32516, 32517]
icons = []
for icon_id in system_icon_ids:
    hicon = user32.LoadIconW(0, icon_id)
    if hicon:
        icons.append(hicon)

def draw_icon():
    hdc = user32.GetDC(0)
    if hdc and icons:
        x = random.randint(0, screen_w - 100)
        y = random.randint(0, screen_h - 100)
        w = random.randint(40, 140)
        h = random.randint(40, 140)
        icon = random.choice(icons)
        user32.DrawIconEx(hdc, x, y, icon, w, h, 0, None, 3)
        user32.ReleaseDC(0, hdc)

def stretch_screen():
    hdc = user32.GetDC(0)
    if hdc:
        stretch_w = random.randint(screen_w - 100, screen_w + 200)
        stretch_h = random.randint(screen_h - 100, screen_h + 200)
        x = (screen_w - stretch_w) // 2
        y = (screen_h - stretch_h) // 2
        gdi32.StretchBlt(hdc, x, y, stretch_w, stretch_h, hdc, 0, 0, screen_w, screen_h, SRCCOPY)
        user32.ReleaseDC(0, hdc)

def horizontal_stretch():
    hdc = user32.GetDC(0)
    if hdc:
        stretch_w = random.randint(screen_w - 50, screen_w + 300)
        x = (screen_w - stretch_w) // 2
        gdi32.StretchBlt(hdc, x, 0, stretch_w, screen_h, hdc, 0, 0, screen_w, screen_h, SRCCOPY)
        user32.ReleaseDC(0, hdc)

def vertical_stretch():
    hdc = user32.GetDC(0)
    if hdc:
        stretch_h = random.randint(screen_h - 50, screen_h + 200)
        y = (screen_h - stretch_h) // 2
        gdi32.StretchBlt(hdc, 0, y, screen_w, stretch_h, hdc, 0, 0, screen_w, screen_h, SRCCOPY)
        user32.ReleaseDC(0, hdc)

def wave_stretch():
    hdc = user32.GetDC(0)
    if hdc:
        for i in range(0, screen_w, 50):
            gdi32.StretchBlt(hdc, i, 0, 50, screen_h, hdc, i, 0, 50, screen_h, SRCCOPY)
        user32.ReleaseDC(0, hdc)

def tunnel_effect():
    hdc = user32.GetDC(0)
    mem_dc = gdi32.CreateCompatibleDC(hdc)
    bmp = gdi32.CreateCompatibleBitmap(hdc, screen_w, screen_h)
    gdi32.SelectObject(mem_dc, bmp)
    gdi32.BitBlt(mem_dc, 0, 0, screen_w, screen_h, hdc, 0, 0, SRCCOPY)
    
    start_time = time.time()
    while time.time() - start_time < 20:
        for level in range(20):
            scale = 1.0 - (level * 0.04)
            w = int(screen_w * scale)
            h = int(screen_h * scale)
            x = (screen_w - w) // 2
            y = (screen_h - h) // 2
            gdi32.StretchBlt(hdc, x, y, w, h, mem_dc, 0, 0, screen_w, screen_h, SRCCOPY)
        time.sleep(0.3)
    
    gdi32.BitBlt(hdc, 0, 0, screen_w, screen_h, mem_dc, 0, 0, SRCCOPY)
    gdi32.DeleteDC(mem_dc)
    gdi32.DeleteObject(bmp)
    user32.ReleaseDC(0, hdc)

def get_rainbow_color(t):
    r = int(127 * math.sin(t) + 128)
    g = int(127 * math.sin(t + 2) + 128)
    b = int(127 * math.sin(t + 4) + 128)
    return r | (g << 8) | (b << 16)

def ultra_err_effect():
    hdc = user32.GetDC(0)
    sw = screen_w
    sh = screen_h
    text = "err.exe".encode('ascii')
    
    balls = []
    for _ in range(5):
        balls.append({
            'x': random.randint(100, sw-100),
            'y': random.randint(100, sh-100),
            'vx': random.choice([-15, 15]),
            'vy': random.choice([-15, 15]),
            'size': 60
        })
    
    t = 0
    start_time = time.time()
    
    try:
        while time.time() - start_time < 20:
            t += 0.1
            
            gdi32.BitBlt(hdc, 10, 10, sw - 20, sh - 20, hdc, 0, 0, SRCCOPY)
            
            for ball in balls:
                ball['x'] += ball['vx']
                ball['y'] += ball['vy']
                
                if ball['x'] <= 0 or ball['x'] >= sw - ball['size']:
                    ball['vx'] *= -1
                if ball['y'] <= 0 or ball['y'] >= sh - ball['size']:
                    ball['vy'] *= -1
                
                color = get_rainbow_color(t + balls.index(ball))
                brush = gdi32.CreateSolidBrush(color)
                old_obj = gdi32.SelectObject(hdc, brush)
                
                gdi32.Ellipse(hdc, ball['x'], ball['y'], ball['x'] + ball['size'], ball['y'] + ball['size'])
                
                gdi32.SetBkMode(hdc, 1)
                gdi32.SetTextColor(hdc, 0xFFFFFF)
                gdi32.TextOutA(hdc, ball['x'] + 5, ball['y'] + ball['size']//3, text, len(text))
                
                gdi32.SelectObject(hdc, old_obj)
                gdi32.DeleteObject(brush)
            
            if random.random() > 0.8:
                tx, ty = random.randint(0, sw), random.randint(0, sh)
                gdi32.SetTextColor(hdc, get_rainbow_color(t * 2))
                gdi32.TextOutA(hdc, tx, ty, text, len(text))
            
            time.sleep(0.001)
    except:
        pass
    finally:
        user32.ReleaseDC(0, hdc)

def malware_style_gdi():
    hdc = user32.GetDC(0)
    width = screen_w
    height = screen_h
    YELLOW = 0x0000FFFF
    ORANGE = 0x0000A5FF
    lx, ly = width // 2, height // 2
    start_time = time.time()
    
    try:
        while time.time() - start_time < 20:
            hdc = user32.GetDC(0)
            pen = gdi32.CreatePen(0, 4, ORANGE)
            old_pen = gdi32.SelectObject(hdc, pen)
            nx = lx + random.randint(-60, 60)
            ny = ly + random.randint(-60, 60)
            nx = max(0, min(width, nx))
            ny = max(0, min(height, ny))
            gdi32.MoveToEx(hdc, lx, ly, None)
            gdi32.LineTo(hdc, nx, ny)
            lx, ly = nx, ny
            for _ in range(300):
                rx = random.randint(0, width)
                ry = random.randint(0, height)
                gdi32.SetPixel(hdc, rx, ry, YELLOW)
            gdi32.SelectObject(hdc, old_pen)
            gdi32.DeleteObject(pen)
            user32.ReleaseDC(0, hdc)
            time.sleep(0.005)
    except:
        pass
    finally:
        user32.InvalidateRect(0, None, True)

def chaos_effect():
    width = screen_w
    height = screen_h
    hFont = gdi32.CreateFontW(60, 0, 0, 0, 700, False, False, False, 1, 0, 0, 0, 0, "Impact")
    
    texts = []
    for _ in range(5):
        texts.append({
            "x": random.randint(0, width-200),
            "y": random.randint(0, height-80),
            "dx": random.choice([-12, 12]),
            "dy": random.choice([-12, 12])
        })
    
    ball = {"x": width // 2, "y": height // 2, "dx": 10, "dy": 10, "size": 100}
    
    t = 0
    start_time = time.time()
    
    try:
        while time.time() - start_time < 20:
            hdc = user32.GetDC(0)
            gdi32.SelectObject(hdc, hFont)
            gdi32.SetBkMode(hdc, 1)
            
            for txt in texts:
                gdi32.SetTextColor(hdc, random.choice([0x0000FFFF, 0x0000A5FF]))
                gdi32.TextOutW(hdc, txt["x"], txt["y"], "err.exe", 7)
                txt["x"] += txt["dx"]
                txt["y"] += txt["dy"]
                if txt["x"] <= 0 or txt["x"] >= width - 180: txt["dx"] *= -1
                if txt["y"] <= 0 or txt["y"] >= height - 60: txt["dy"] *= -1
            
            factor = (math.sin(t) + 1) / 2
            red = 255
            green = int(165 + (255 - 165) * factor)
            blue = 0
            ball_color = (blue << 16) | (green << 8) | red
            
            brush = gdi32.CreateSolidBrush(ball_color)
            old_brush = gdi32.SelectObject(hdc, brush)
            
            gdi32.Ellipse(hdc, ball["x"], ball["y"], ball["x"] + ball["size"], ball["y"] + ball["size"])
            
            ball["x"] += ball["dx"]
            ball["y"] += ball["dy"]
            
            if ball["x"] <= 0 or ball["x"] >= width - ball["size"]: ball["dx"] *= -1
            if ball["y"] <= 0 or ball["y"] >= height - ball["size"]: ball["dy"] *= -1
            
            gdi32.SelectObject(hdc, old_brush)
            gdi32.DeleteObject(brush)
            user32.ReleaseDC(0, hdc)
            
            t += 0.1
            time.sleep(0.01)
    except:
        pass
    finally:
        gdi32.DeleteObject(hFont)
        user32.InvalidateRect(0, None, True)

def pure_chaos_effect():
    width = screen_w
    height = screen_h
    ball = {"x": width // 2, "y": height // 2, "dx": 20, "dy": 20, "size": 150}
    t = 0
    start_time = time.time()
    
    try:
        while time.time() - start_time < 20:
            hdc = user32.GetDC(0)
            
            for _ in range(3):
                sx = random.randint(50, width - 150)
                sy = random.randint(50, height - 150)
                gdi32.StretchBlt(hdc, sx - 20, sy - 20, 160, 160, hdc, sx, sy, 100, 100, SRCCOPY)
            
            factor = (math.sin(t) + 1) / 2
            green = int(140 + (255 - 140) * factor)
            ball_color = (0 << 16) | (green << 8) | 255
            
            brush = gdi32.CreateSolidBrush(ball_color)
            old_brush = gdi32.SelectObject(hdc, brush)
            
            gdi32.Ellipse(hdc, ball["x"], ball["y"], ball["x"] + ball["size"], ball["y"] + ball["size"])
            
            ball["x"] += ball["dx"]
            ball["y"] += ball["dy"]
            if ball["x"] <= 0 or ball["x"] >= width - ball["size"]: ball["dx"] *= -1
            if ball["y"] <= 0 or ball["y"] >= height - ball["size"]: ball["dy"] *= -1
            
            if random.random() > 0.8:
                hIcon = user32.LoadIconW(0, IDI_HAND)
                user32.DrawIcon(hdc, random.randint(0, width), random.randint(0, height), hIcon)
            
            for _ in range(200):
                gdi32.SetPixel(hdc, random.randint(0, width), random.randint(0, height), 0x0000FFFF)
            
            gdi32.SelectObject(hdc, old_brush)
            gdi32.DeleteObject(brush)
            user32.ReleaseDC(0, hdc)
            
            t += 0.2
            time.sleep(0.005)
    except:
        pass
    finally:
        user32.InvalidateRect(0, None, True)

def exact_video_effect():
    width = screen_w
    height = screen_h
    ball = {"x": width // 2, "y": height // 2, "dx": 22, "dy": 22, "size": 160}
    t = 0
    start_time = time.time()
    
    try:
        while time.time() - start_time < 20:
            hdc = user32.GetDC(0)
            
            for _ in range(6):
                x = random.randint(0, width)
                y = random.randint(0, height)
                gdi32.StretchBlt(hdc, x - 75, y - 75, 150, 150, hdc, x - 50, y - 50, 100, 100, SRCCOPY)
            
            factor = (math.sin(t) + 1) / 2
            green = int(160 + (95 * factor))
            ball_color = (0 << 16) | (green << 8) | 255
            
            brush = gdi32.CreateSolidBrush(ball_color)
            old_brush = gdi32.SelectObject(hdc, brush)
            
            gdi32.Ellipse(hdc, ball["x"], ball["y"], ball["x"] + ball["size"], ball["y"] + ball["size"])
            
            ball["x"] += ball["dx"]
            ball["y"] += ball["dy"]
            if ball["x"] <= 0 or ball["x"] >= width - ball["size"]: ball["dx"] *= -1
            if ball["y"] <= 0 or ball["y"] >= height - ball["size"]: ball["dy"] *= -1
            
            for _ in range(3):
                ix, iy = random.randint(0, width), random.randint(0, height)
                hIcon = user32.LoadIconW(0, IDI_HAND)
                user32.DrawIcon(hdc, ix, iy, hIcon)
            
            gdi32.SelectObject(hdc, old_brush)
            gdi32.DeleteObject(brush)
            user32.ReleaseDC(0, hdc)
            
            t += 0.2
            time.sleep(0.001)
    except:
        pass
    finally:
        user32.InvalidateRect(0, None, True)

def slow_icon_flood():
    width = screen_w
    height = screen_h
    icon_ids = [32513, 32515, 32514, 32516]
    step = 32
    hdc = user32.GetDC(0)
    
    try:
        for y in range(0, height, step):
            for x in range(0, width, step):
                h_icon = user32.LoadIconW(0, random.choice(icon_ids))
                user32.DrawIcon(hdc, x, y, h_icon)
                time.sleep(0.02)
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        user32.ReleaseDC(0, hdc)
        user32.InvalidateRect(0, None, True)

def total_destruction():
    width = screen_w
    height = screen_h
    hFont = gdi32.CreateFontW(120, 45, 0, 0, 400, False, False, False, 1, 0, 0, 0, 0, "Arial")
    ball = {"x": width // 2, "y": height // 2, "dx": 30, "dy": 30, "size": 180}
    hue = 0
    start_time = time.time()
    
    try:
        while time.time() - start_time < 20:
            hdc = user32.GetDC(0)
            
            gdi32.StretchBlt(hdc, -10, -10, width + 20, height + 20, hdc, 0, 0, width, height, SRCCOPY)
            
            brush_bg = gdi32.CreateSolidBrush(random.randint(0, 0xFFFFFF))
            gdi32.SelectObject(hdc, brush_bg)
            gdi32.PatBlt(hdc, 0, 0, width, height, 0x005A0049)
            gdi32.DeleteObject(brush_bg)
            
            r = int(math.sin(hue) * 127 + 128)
            g = int(math.sin(hue + 2) * 127 + 128)
            b = int(math.sin(hue + 4) * 127 + 128)
            ball_brush = gdi32.CreateSolidBrush((b << 16) | (g << 8) | r)
            gdi32.SelectObject(hdc, ball_brush)
            gdi32.Ellipse(hdc, ball["x"], ball["y"], ball["x"] + ball["size"], ball["y"] + ball["size"])
            
            ball["x"] += ball["dx"]
            ball["y"] += ball["dy"]
            if ball["x"] <= 0 or ball["x"] >= width - ball["size"]: ball["dx"] *= -1
            if ball["y"] <= 0 or ball["y"] >= height - ball["size"]: ball["dy"] *= -1
            gdi32.DeleteObject(ball_brush)
            
            for _ in range(5):
                h = random.randint(5, 50)
                y = random.randint(0, height)
                gdi32.BitBlt(hdc, random.randint(-100, 100), y, width, h, hdc, 0, y, SRCCOPY)
            
            gdi32.SelectObject(hdc, hFont)
            gdi32.SetBkMode(hdc, 1)
            gdi32.SetTextColor(hdc, random.randint(0, 0xFFFFFF))
            tx = (width // 2 - 200) + random.randint(-40, 40)
            ty = (height // 2 - 60) + random.randint(-40, 40)
            gdi32.TextOutW(hdc, tx, ty, "err.exe", 7)
            
            for _ in range(2):
                user32.DrawIcon(hdc, random.randint(0, width), random.randint(0, height), user32.LoadIconW(0, IDI_HAND))
            
            user32.ReleaseDC(0, hdc)
            hue += 0.4
            time.sleep(0.001)
    except:
        pass
    finally:
        gdi32.DeleteObject(hFont)
        user32.InvalidateRect(0, None, True)

def slow_falling_fade():
    sw = screen_w
    sh = screen_h
    hFont = gdi32.CreateFontW(90, 35, 0, 0, 400, False, False, False, 1, 0, 0, 0, 0, "Arial")
    
    columns = []
    for _ in range(12):
        columns.append({
            "x": random.randint(0, sw),
            "y": random.randint(-sh, 0),
            "speed": random.randint(2, 6)
        })
    
    start_time = time.time()
    
    try:
        while time.time() - start_time < 20:
            hdc = user32.GetDC(0)
            gdi32.SelectObject(hdc, hFont)
            gdi32.SetBkMode(hdc, 1)
            
            for _ in range(100):
                gdi32.SetPixel(hdc, random.randint(0, sw), random.randint(0, sh), 0x000000)
            
            for col in columns:
                gdi32.SetTextColor(hdc, random.choice([0x0000FF, 0x00FFFF, 0x00A5FF]))
                gdi32.TextOutW(hdc, col["x"], col["y"], "err.exe", 7)
                col["y"] += col["speed"]
                
                if col["y"] > sh:
                    col["y"] = -100
                    col["x"] = random.randint(0, sw)
            
            if random.random() > 0.95:
                ix = random.randint(0, sw-100)
                iy = random.randint(0, sh-100)
                gdi32.StretchBlt(hdc, ix-5, iy-5, 110, 110, hdc, ix, iy, 100, 100, SRCCOPY)
            
            user32.ReleaseDC(0, hdc)
            time.sleep(0.05)
    except:
        pass
    finally:
        gdi32.DeleteObject(hFont)
        user32.InvalidateRect(0, None, True)

if __name__ == "__main__":
    if show_warning():
        start_time = time.time()
        while time.time() - start_time < 20:
            if random.random() < 0.4: disco_background()
            if random.random() < 0.3: shake_disco()
            if random.random() < 0.2: bulge_effect_disco()
            if random.random() < 0.5: draw_disco_icon()
            time.sleep(0.03)
        user32.InvalidateRect(0, 0, 1)
        
        start_time = time.time()
        while time.time() - start_time < 20:
            shake_error()
            if random.random() < 0.4:
                bulge_effect_error()
            if random.random() < 0.7:
                draw_error_icon()
            time.sleep(0.03)
        user32.InvalidateRect(0, 0, 1)
        
        start_time = time.time()
        while time.time() - start_time < 20:
            draw_text()
            time.sleep(random.uniform(0.05, 0.15))
        user32.InvalidateRect(0, 0, 1)
        
        start_time = time.time()
        while time.time() - start_time < 20:
            invert_screen()
            time.sleep(0.0002)
        user32.InvalidateRect(0, 0, 1)
        
        start_time = time.time()
        while time.time() - start_time < 20:
            if random.random() < 0.5:
                shake_effect()
            if random.random() < 0.3:
                blur_effect()
            if random.random() < 0.6:
                draw_text_fit()
            time.sleep(0.05)
        user32.InvalidateRect(0, 0, 1)
        
        start_time = time.time()
        while time.time() - start_time < 20:
            if random.random() < 0.6:
                draw_icon()
            if random.random() < 0.4:
                stretch_screen()
            elif random.random() < 0.3:
                horizontal_stretch()
            elif random.random() < 0.3:
                vertical_stretch()
            if random.random() < 0.15:
                wave_stretch()
            time.sleep(random.uniform(0.05, 0.12))
        user32.InvalidateRect(0, 0, 1)
        
        tunnel_effect()
        
        ultra_err_effect()
        
        malware_style_gdi()
        
        chaos_effect()
        
        pure_chaos_effect()
        
        exact_video_effect()
        
        slow_icon_flood()
        
        total_destruction()
        
        slow_falling_fade()
        
        time.sleep(2)
    else:
        sys.exit(0)