import tkinter as tk
import tkinter.messagebox
import pyautogui
from selenium import webdriver
import time


# 自訂函數
                           
def a():#右邊螢幕截圖

  pyautogui.hotkey('win','shift','s')#快捷鍵
  pyautogui.moveTo(1925,3, duration =0.1)#複製起始點
  pyautogui.sleep(0.2)
  pyautogui.dragTo(3839,1079, duration =0.2,button='left')#複製結束點

def b():#右Product Updates截圖  
  pyautogui.hotkey('win','shift','s')#快捷鍵
  pyautogui.moveTo(1930,550, duration =0.1)#複製起始點
  pyautogui.sleep(0.2)
  pyautogui.dragTo(2535,862, duration =0.2,button='left')#複製結束點

def c():#右Boot Time截圖  
  pyautogui.hotkey('win','shift','s')#快捷鍵
  pyautogui.moveTo(3180,370, duration =0.1)#複製起始點
  pyautogui.sleep(0.2)
  pyautogui.dragTo(3815,710, duration =0.2,button='left')#複製結束點

def d():#右Traffic截圖  
  pyautogui.hotkey('win','shift','s')#快捷鍵
  pyautogui.moveTo(2565,501, duration =0.1)#複製起始點
  pyautogui.sleep(0.2)
  pyautogui.dragTo(3190,750, duration =0.2,button='left')#複製結束點  

def e():#自選螢幕截圖
  pyautogui.hotkey('win','shift','s')#快捷鍵

'''
def x():
  driver = webdriver.Chrome('./chromedriver.exe')
  driver.get('https://drive.google.com/drive/folders/1cOOSyJemeEMMwqHs_jKHC0TMsAnT2UlY')
  time.sleep(30)
'''


# 建立主視窗 Frame
window = tk.Tk()
window.configure(bg='#E8FFF5')
# 設定視窗標題
window.title('Copy Program')

# 設定視窗大小為 400x350，視窗（左上角）在螢幕上的座標位置為 (574, 220)
window.geometry("500x300+574+220")

# 建立按鈕
button = tk.Button(window,          #按鈕所在視窗
                   bg="#FFF8D7",    #按鈕顏色
                   width= 20,       #按鈕寬度
                   height= 3 ,      #按鈕高度
                   font= 8,         #字體大小
                   text = '右邊螢幕截圖',  # 顯示文字
                   command = a ) # 按下按鈕所執行的函數


button1 = tk.Button(window,          
                   bg="#FFF8D7",     
                   width= 20,
                   height= 3 ,
                   font= 8, 
                   text = '右Product Updates截圖',
                   command = b
                   ) 

button2 = tk.Button(window,          
                   bg="#FFF8D7",     
                   width= 20,
                   height= 3 ,
                   font= 8, 
                   text = '右Boot Time截圖',
                   command = c
                   ) 

button3 = tk.Button(window,          
                   bg="#FFF8D7",     
                   width= 20,
                   height= 3 ,
                   font= 8, 
                   text = '右Traffic截圖',
                   command = d
                   )    

button4 = tk.Button(window,          # 按鈕所在視窗
                   bg="#FFF8D7",     # 按鈕顏色
                   width= 20,
                   height= 3 ,
                   font= 8, 
                   text = '自選螢幕截圖',  # 顯示文字
                   command = e) # 按下按鈕所執行的函數

        

# 按鈕排版 padx=0,pady=5
button.grid(row=1,column=2)
button1.grid(row=1,column=3)
button2.grid(row=2,column=2)
button3.grid(row=2,column=3)
button4.grid(row=0,column=2)


# 執行主程式
window.mainloop()
 
