# FilesBatchRenameWithGUI.py

# 导入需要的库
import tkinter as tk
from tkinter import filedialog
import os

# 控制文件列表显示函数
def DisplayList():
    listbox.delete(0,tk.END)
    for file in os.listdir(path.get()):
        listbox.insert(tk.END,file)

# 获取文件夹路径函数
def GetPath():
    filepath = filedialog.askdirectory()
    path.set(filepath)
    DisplayList()

# 批量重命名函数
def HandelFiles():
    pattern = entry2.get()
    num = 1
    for file in os.listdir(path.get()):
        result = pattern.replace('[]',str(num))
        os.rename(os.path.join(path.get(),file),os.path.join(path.get(),result)+'.'+file.split('.')[-1])
        num = num + 1
    DisplayList()

# 显示提示函数
def ShowTips(event):
    tips.place(x=10,y=50)

# 隐藏提示函数
def HideTips(event):
    tips.place_forget()

root = tk.Tk()
root.title('批量重命名')
root.resizable(0,0)

path = tk.StringVar() # 定义路径变量

# 定义控件
listbox = tk.Listbox(root)
label1 = tk.Label(root,text="文件夹路径：")
entry1 = tk.Entry(root,textvariable=path)
button1 = tk.Button(root,text="选择路径",command=GetPath)
label2 = tk.Label(root,text="递增规则?：")
entry2 = tk.Entry(root)
tips = tk.Label(root,text="[]为递增标记\n例如：图片[],结果为：图片1，图片2，图片3...")
label2.bind("<Enter>",ShowTips)
label2.bind('<Leave>',HideTips)
button2 = tk.Button(root,text="开始处理",command=HandelFiles)

# 调整控件布局
label1.grid(row=0,column=0)
entry1.grid(row=0,column=1)
button1.grid(row=0,column=2)
label2.grid(row=1,column=0)
entry2.grid(row=1,column=1)
button2.grid(row=1,column=2)
listbox.grid(row=2,column=0,columnspan=3,sticky=tk.W+tk.E)

root.mainloop()