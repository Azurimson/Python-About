from you_get import common
from tkinter import *
import tkinter.filedialog
import os
import threading
from selenium import webdriver

# common.any_download(url='https://www.bilibili.com/video/av33241179',
#                     info_only=False,
#                     output_dir='/home/karas/Downloads',
#                     merge=True)

# import sys
# sys.argv=['you-get', 'https://www.bilibili.com/video/av33241179']
# you_get.main()

class Application():
    def __init__(self, master=None):
        self.is_s = IntVar()
        self.savepath = os.getcwd()


        self.root = master

        self.inputLabel = Label(self.root, text='请输入链接:')
        self.inputLabel.grid(row=0, column=0)
        self.checkbutton = Checkbutton(self.root, text="批量下载", variable=self.is_s)
        self.checkbutton.grid(row=1, column=0)
        self.get = Entry(self.root, width=40)
        self.get.grid(row=1, column=1)
        self.spiderButton = Button(text='spider', command=self.download)
        self.spiderButton.grid(row=1, column=2)
        self.titletLabel = Label(text='')
        self.titletLabel.grid(row=4, column=1)
        self.clearButton = Button(text='clear', command=self.clear)
        self.clearButton.grid(row=2, column=2)
        self.saveButton = Button(text='选择存储路径', command=self.save)
        self.saveButton.grid(row=2, column=0)

    def download(self):
        self.url = self.get.get()
        if self.is_s.get() == 0:#下载单个文件
            self.titletLabel["text"] = '当前文件下载中......'
            t = threading.Thread(target=self.download_one, args=(self.url, ))
            # t.setDaemon(True)
            t.start()
            t.join()
            self.titletLabel["text"] = '下载成功！'
        else:
            self.get_playlist()
            for i in self.playlist:
                t = threading.Thread(target=self.download_one, args=(i, ))
                t.start()
                t.join()
            self.titletLabel["text"] = '下载成功！'

    def clear(self):
        self.titletLabel["text"] = ''
        self.get.delete('0', 'end')

    def save(self):
        self.savepath = tkinter.filedialog.askdirectory() + "/"

    def download_one(self, url):
        common.any_download(url=url,#https://www.bilibili.com/video/av33241179
                            info_only=False,
                            output_dir=self.savepath,
                            merge=True)

    def get_playlist(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        self.playlist = []
        for link in driver.find_elements_by_class_name("title"):
            l = link.get_attribute('href')  # 无效视频为javascript:;
            if l[0] == 'h':
                self.playlist.append(link.get_attribute('href'))
        driver.quit()




root = Tk()

root.title("123")
root.geometry('500x200')
Application(root)
root.mainloop()



