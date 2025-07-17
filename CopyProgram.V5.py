import tkinter as tk
import pyautogui
import time

# 滑鼠動作封裝
def MDon(): 
    pyautogui.mouseDown()

def MUp():  
    pyautogui.mouseUp()

# 截圖函數
def a():  # 右邊螢幕截圖
    pyautogui.hotkey('win', 'shift', 's')
    time.sleep(0.3)
    pyautogui.moveTo(1925, 3, duration=0.1)
    pyautogui.dragTo(3839, 1079, duration=0.2)
    MUp()

def b():  # 細部截圖
    pyautogui.hotkey('win', 'shift', 's')
    time.sleep(0.3)
    pyautogui.moveTo(1930, 299, duration=0.2)
    pyautogui.dragTo(3185, 783, duration=0.2, button='left')
    MUp()

def c():  # 自選截圖
    pyautogui.hotkey('win', 'shift', 's')

# 主視窗
window = tk.Tk()
window.title('📸 Screenshot Tool')
window.geometry("460x450+550+200")
window.configure(bg="#e1e8ee") 

# 標題
title = tk.Label(window,
                 text="螢幕截圖小助手",
                 font=('微軟正黑體', 22, 'bold'),
                 bg="#e1e8ee",
                 fg="#082761")
title.pack(pady=(25, 15))

# 統一按鈕樣式
button_style = {
    "bg": "#094C79",                # 按鈕背景
    "activebackground": "#0ea894",  # 點擊時
    "fg": "#d6d8c5",                # 文字
    "activeforeground": "#ffffff",
    "width": 25,                    # 加寬
    "height": 3,                    # 加高
    "font": ('微軟正黑體', 16, 'bold'),
    "bd": 3,
    "relief": "raised",
    "highlightthickness": 2,
    "highlightbackground": "#ffffff"  # 邊框
}

# 建立按鈕
button1 = tk.Button(window, text="📷 右邊螢幕截圖", command=a, **button_style)
button2 = tk.Button(window, text="🔍 細部截圖", command=b, **button_style)
button3 = tk.Button(window, text="🎯 自選截圖", command=c, **button_style)

# 排版
button1.pack(pady=12)
button2.pack(pady=12)
button3.pack(pady=12)

# 主迴圈
window.mainloop()
