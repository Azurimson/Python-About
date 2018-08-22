from tkinter import *
import GameGui
from tkinter import messagebox

#开始界面GUI
class StartGui():
    def __init__(self, master = None): 
        self.root = master

        self.frm = Frame(self.root)

        self.frm_R = Frame(self.frm)
        Label(self.frm_R, text='行数:', font=('Arial', 15)).pack(side=LEFT)
        self.t1 = Text(self.frm_R, width=16, height=1)
        self.t1.insert(1.0,'')
        self.t1.pack(side=RIGHT)
        self.frm_R.pack()


        self.frm_C = Frame(self.frm)
        Label(self.frm_C, text='列数:', font=('Arial', 15)).pack(side=LEFT)
        self.t2 = Text(self.frm_C,width=16, height=1)
        self.t2.insert(1.0,'')
        self.t2.pack(side=RIGHT)
        self.frm_C.pack()

        self.frm_M = Frame(self.frm)
        Label(self.frm_M, text='雷数:', font=('Arial', 15)).pack(side=LEFT)
        self.t3 = Text(self.frm_M,width=16, height=1)
        self.t3.insert(1.0,'')
        self.t3.pack(side=RIGHT)
        self.frm_M.pack()

        Button(self.frm, text="确定", command = self.inputdata).pack()

        self.frm.pack()

    def inputdata(self):
        self.row = int(self.t1.get(1.0,END))
        self.col = int(self.t2.get(1.0,END))
        self.minenum = int(self.t3.get(1.0,END))
        if self.minenum <= 0 or self.minenum > self.row * self.col or self.row <= 0 or self.col <= 0:
            messagebox.showinfo(title = 'error', message = '生成失败')
        else:
            self.frm.destroy()
            GameGui.GameGui(self.row, self.col, self.minenum, self.root)
