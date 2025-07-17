import tkinter as tk
import tkinter.messagebox
import pyautogui
import time
from selenium import webdriver

# 自訂函數

def MDon(): 
   pyautogui.mouseDown()

def MUp():  
   pyautogui.mouseUp()


def a():#右邊螢幕截圖
  pyautogui.hotkey('win', 'shift', 's')  #快捷鍵
  time.sleep(0.3)
  pyautogui.moveTo(1925,3, duration =0.1)#複製起始點
  pyautogui.dragTo(3839,1079, duration =0.2)#複製結束點
  MUp()

'''
def b():#左邊螢幕截圖
  pyautogui.hotkey('win','shift','s')#快捷鍵
  pyautogui.moveTo(1930,550, duration =0.1)#複製起始點
  pyautogui.sleep(0.2)
  pyautogui.dragTo(2535,862, duration =0.2,button='left')#複製結束點
'''
def b():#XXXX截圖  
  pyautogui.hotkey('win','shift','s')#快捷鍵
  time.sleep(0.3)
  pyautogui.moveTo(1930,299, duration =0.2)#複製起始點
  pyautogui.dragTo(3185,783, duration =0.2,button='left')#複製結束點
  MUp()

def c():#自選螢幕截圖
  pyautogui.hotkey('win','shift','s')#快捷鍵


# 建立主視窗 Frame   color:#E8FFF5
window = tk.Tk()
window.configure(bg='#48e0d7')
# 設定視窗標題
window.title('Copy Program')

# 設定視窗大小為 400x350，視窗（左上角）在螢幕上的座標位置為 (574, 220)
window.geometry("400x380+574+220")

# 建立按鈕
button1 = tk.Button(window,          
                   bg="#FFF8D7",     
                   width= 20,
                   height= 3 ,
                   font= ('微軟正黑體 Light',14,'bold'), 
                   text = '右邊螢幕截圖',
                   command = a
                   ) 
button2 = tk.Button(window,          
                   bg="#FFF8D7",     
                   width= 20,
                   height= 3 ,
                   font= ('微軟正黑體 Light',14,'bold'), 
                   text = '細部截圖',
                   command = b
                   ) 

button3 = tk.Button(window,          
                   bg="#FFF8D7",     
                   width= 20,
                   height= 3 ,
                   font=('微軟正黑體 Light',14,'bold'), 
                   text = '自選螢幕截圖',
                   command = c
                   ) 
        

# 按鈕排版 padx=0,pady=5
button1.pack(side="top", expand=True, anchor="center")
button2.pack(side="top", expand=True, anchor="center") 
button3.pack(side="top", expand=True, anchor="center") 
button1.config(foreground="#2dae68")
button2.config(foreground="#2dae68")
button3.config(foreground="#2dae68")

# 執行主程式
window.mainloop()
 
