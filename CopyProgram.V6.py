import tkinter as tk
import pyautogui
import time
from PIL import Image
from tkinter import messagebox

# === 截圖函數 ===
def screenshot_by_coords():
        x = int(entry_x.get())
        y = int(entry_y.get())
        x2 = int(entry_x2.get())
        y2 = int(entry_y2.get())
        pyautogui.hotkey('win', 'shift', 's')
        time.sleep(1.2)
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.dragTo(x2,y2, duration=0.2)



# === 原有功能 ===
def a():
    pyautogui.hotkey('win', 'shift', 's')
    time.sleep(1.2)
    pyautogui.moveTo(1925, 3, duration=0.1)
    pyautogui.dragTo(3839, 1079, duration=0.2)

def b():
    pyautogui.hotkey('win', 'shift', 's')
    time.sleep(1.2)
    pyautogui.moveTo(1930, 299, duration=0.2)
    pyautogui.dragTo(3185, 783, duration=0.2, button='left')

def c():
    pyautogui.hotkey('win', 'shift', 's')



# === 視窗設計 ===
window = tk.Tk()
window.title('📸 Screenshot Tool')
window.geometry("460x550+550+200")
window.configure(bg='#f3e5f5')

# === 按鈕樣式 ===
button_style = {
    "bg": "#ce93d8",
    "activebackground": "#ba68c8",
    "fg": "#ffffff",
    "width": 25,
    "height": 2,
    "font": ('微軟正黑體', 14, 'bold'),
    "bd": 3,
    "relief": "raised",
    "highlightthickness": 2,
    "highlightbackground": "#ab47bc"
}

# === 按鈕 ===
tk.Label(window, text="螢幕截圖小助手", font=('微軟正黑體', 22, 'bold'), bg='#f3e5f5', fg='#4a148c').pack(pady=(20,10))
tk.Button(window, text="📷 右邊螢幕截圖", command=a, **button_style).pack(pady=8)
tk.Button(window, text="🔍 細部截圖", command=b, **button_style).pack(pady=8)
tk.Button(window, text="🎯 自選截圖", command=c, **button_style).pack(pady=8)

# 自訂座標輸入區（整合區塊）
coord_frame = tk.LabelFrame(window, text="🎯 自訂座標截圖", bg="#f3e5f5", fg="#4a148c", font=('微軟正黑體', 12, 'bold'))
coord_frame.pack(pady=15, padx=10, fill="x")

# 起始點
tk.Label(coord_frame, text="起始點 X1:", bg='#f3e5f5', anchor='e', width=10).grid(row=0, column=0, sticky='e', pady=4)
entry_x = tk.Entry(coord_frame, width=10)
entry_x.grid(row=0, column=1, padx=5)

tk.Label(coord_frame, text="Y1:", bg='#f3e5f5', anchor='e', width=10).grid(row=0, column=2, sticky='e', pady=4)
entry_y = tk.Entry(coord_frame, width=10)
entry_y.grid(row=0, column=3, padx=5)

# 結束點
tk.Label(coord_frame, text="結束點 X2:", bg='#f3e5f5', anchor='e', width=10).grid(row=1, column=0, sticky='e', pady=4)
entry_x2 = tk.Entry(coord_frame, width=10)
entry_x2.grid(row=1, column=1, padx=5)

tk.Label(coord_frame, text="Y2:", bg='#f3e5f5', anchor='e', width=10).grid(row=1, column=2, sticky='e', pady=4)
entry_y2 = tk.Entry(coord_frame, width=10)
entry_y2.grid(row=1, column=3, padx=5)

# 截圖按鈕（放在區塊內）
tk.Button(
    coord_frame,
    text="📸 截圖指定區域",
    command=screenshot_by_coords,
    bg="#7b1fa2",
    fg="white",
    font=('微軟正黑體', 14, 'bold'),
    height=2,
    width=25
).grid(row=2, column=0, columnspan=4, pady=30)

window.mainloop()
