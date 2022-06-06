import tkinter as tk                   #匯入tkinter模組
win = tk.Tk() #建立主視窗

win.title('YouTube MP3 Downloader')  # 設定主視窗標題
win.geometry('640x480')              # 大小  寬x高
# win.minsize(width=400,height=200)
# win.maxsize(width=1024,height=768)
win.resizable(0,0)
win.config(bg="skyblue")
win.attributes()

#icon
win.iconbitmap("YouTube.ico")

win.mainloop() #常駐主視窗


# win = tk.Tk()                          # 建立主視窗物件
# win.geometry('640x480')                # 設定主視窗預設尺寸為640x480
# win.resizable(False,False)             # 設定主視窗的寬跟高皆不可縮放
# win.title('YouTube MP3 Downloader')  # 設定主視窗標題
# # win.iconbitmap('YouTube.ico')          # 設定主視窗 icon
# win.mainloop()