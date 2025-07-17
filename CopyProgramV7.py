import tkinter as tk
import pyautogui
import time
from tkinter import messagebox
import threading
from pynput import mouse

# === 截圖函數 ===
def screenshot_by_coords():
    try:
        x = int(entry_x.get())
        y = int(entry_y.get())
        x2 = int(entry_x2.get())
        y2 = int(entry_y2.get())
        pyautogui.hotkey('win', 'shift', 's')
        time.sleep(1.2)
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.dragTo(x2, y2, duration=0.2)
    except Exception as e:
        messagebox.showerror("錯誤", f"輸入錯誤或截圖失敗：\n{e}")

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

# === 座標監聽函數 ===

def get_start_coords():
    def on_click(x, y, button, pressed):
        if pressed:
            entry_x.delete(0, tk.END)
            entry_x.insert(0, str(x))
            entry_y.delete(0, tk.END)
            entry_y.insert(0, str(y))
            listener.stop()  # 一次點擊就結束監聽

    listener = mouse.Listener(on_click=on_click)
    listener.start()

def get_end_coords():
    def on_click(x, y, button, pressed):
        if pressed:
            entry_x2.delete(0, tk.END)
            entry_x2.insert(0, str(x))
            entry_y2.delete(0, tk.END)
            entry_y2.insert(0, str(y))
            listener.stop()  # 一次點擊就結束監聽

    listener = mouse.Listener(on_click=on_click)
    listener.start()

# === 主視窗設計 ===
window = tk.Tk()
window.title('📸 Screenshot Tool')
window.geometry("500x600+550+200")
window.configure(bg='#e0f7fa')  # 淡藍綠背景

# === 按鈕樣式 ===
button_style = {
    "bg": "#1d8f9e",              # 鮮藍綠
    "activebackground": "#b8f3f0",# 按下去的顏色
    "fg": "white",              # 字色：深藍
    "width": 25,
    "height": 2,
    "font": ('微軟正黑體', 14, 'bold'),
    "bd": 3,
    "relief": "raised",
    "highlightthickness": 2,
    "highlightbackground": "#00acc1"
}

# === 標題 ===
tk.Label(window, text="螢幕截圖小助手_Win版", font=('微軟正黑體', 22, 'bold'),
         bg='#e0f7fa', fg='#006064').pack(pady=(20,10))

# === 主功能按鈕 ===
tk.Button(window, text="📷 右邊螢幕截圖", command=a, **button_style).pack(pady=8)
tk.Button(window, text="🔍 細部截圖", command=b, **button_style).pack(pady=8)
tk.Button(window, text="🎯 自選截圖", command=c, **button_style).pack(pady=8)

# === 座標輸入區塊 ===
coord_frame = tk.LabelFrame(
    window,
    text="🎯 自訂座標截圖",
    bg="#e0f7fa",
    fg="#006064",
    font=('微軟正黑體', 12, 'bold'),
    labelanchor='nw',
    bd=2,
    relief="groove",
    highlightbackground="#006064",  # 框線顏色
    highlightcolor="#006064"
)
coord_frame.pack(pady=20, padx=20, fill="x")


# 起始點
tk.Button(coord_frame, text="🎯 取得起始點", command=get_start_coords,
          bg="#4db6ac", fg="white", font=('微軟正黑體', 10, 'bold')).grid(row=0, column=4, padx=5)

tk.Label(coord_frame, text="起始點座標 X1:", bg='#b2ebf2', anchor='e', width=12).grid(row=0, column=0, sticky='e', pady=6)
entry_x = tk.Entry(coord_frame, width=10)
entry_x.grid(row=0, column=1, padx=5)

tk.Label(coord_frame, text="起始點座標 Y1:", bg='#b2ebf2', anchor='e', width=12).grid(row=0, column=2, sticky='e', pady=6)
entry_y = tk.Entry(coord_frame, width=10)
entry_y.grid(row=0, column=3, padx=5)

# 結束點
tk.Button(coord_frame, text="🎯 取得結束點", command=get_end_coords,
          bg="#4db6ac", fg="white", font=('微軟正黑體', 10, 'bold')).grid(row=1, column=4, padx=5)

tk.Label(coord_frame, text="結束點座標 X2:", bg='#b2ebf2', anchor='e', width=12).grid(row=1, column=0, sticky='e', pady=6)
entry_x2 = tk.Entry(coord_frame, width=10)
entry_x2.grid(row=1, column=1, padx=5)

tk.Label(coord_frame, text="結束點座標 Y2:", bg='#b2ebf2', anchor='e', width=12).grid(row=1, column=2, sticky='e', pady=6)
entry_y2 = tk.Entry(coord_frame, width=10)
entry_y2.grid(row=1, column=3, padx=5)

# 設定欄寬平均分配
for i in range(5):
    coord_frame.grid_columnconfigure(i, weight=1)

# 置中按鈕
tk.Button(
    coord_frame,
    text="📸 截圖指定區域",
    command=screenshot_by_coords,
    activebackground="#b8f3f0",
    bg="#b2ebf2",
    fg="#0d626d",
    font=('微軟正黑體', 14, 'bold'),
    height=2,
    width=30
).grid(row=2, column=0, columnspan=5, pady=20)


# 建立 Label 顯示座標
coord_label = tk.Label(window, 
                       text="目前座標：-- , --",
                         font=('微軟正黑體', 12), 
                         bg='#e0f2f1', fg='#006064')
coord_label.place(relx=0.01, rely=0.97, anchor='sw')

# 定期更新滑鼠座標
def update_mouse_position():
    while True:
        try:
            x, y = pyautogui.position()
            coord_label.config(text=f"目前座標：{x} , {y}")
            time.sleep(0.1)
        except:
            break

# 用 Thread 避免卡住 UI
threading.Thread(target=update_mouse_position, daemon=True).start()

# === 執行程式 ===
window.mainloop()
