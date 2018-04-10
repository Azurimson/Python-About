from tkinter import *  
import tkinter.messagebox as messagebox
import urllib.request
import re

def craw(url):
    h1=urllib.request.urlopen(url).read()
    h1=str(h1)
    p2='<img src="https://(.+?\.jpg)"'
    imglist=re.compile(p2).findall(h1)
    x=1
    for imgurl in imglist:
        imgname="d:/A/"+str(x)+".jpg"
        imgurl="http://"+imgurl
        urllib.request.urlretrieve(imgurl,filename=imgname)
        x+=1

class Application(Frame):
    def __init__(self,master = None): 
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()  
    def createWidgets(self):
        self.inputLabel = Label(self,text = '请输入链接:')
        self.inputLabel.pack(side=LEFT)
        self.input = Entry(self)#输入框
        self.input.pack(side=LEFT)
        self.spiderButton = Button(self,text = 'spider',command = self.hello)#spider按钮
        self.spiderButton.pack(side=LEFT)
        self.titleLabel = Label(self,text = '标题：')
        self.titleLabel.pack(side=LEFT)
        self.titletLabel = Label(self,text = '')#用于显示爬取的标题
        self.titletLabel.pack(side=LEFT)
        self.nameButton = Button(self,text = 'clear',command = self.quit)#清除当前显示的文本
        self.nameButton.pack(side=LEFT, anchor=W)
    def hello(self):
        url = self.input.get()#输入链接url
        #url='https://blog.csdn.net/sunhf_csdn/article/details/79848837'#测试用url
        content=urllib.request.urlopen(url).read()
        content=content.decode('utf-8')
        rt = r'<title>(.*?)</title>'
        rcontent =  re.findall(rt,content,re.S|re.M)
        for title in rcontent:
            self.titletLabel["text"]=title
        ru = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"  
        link = re.findall(ru ,  content, re.I|re.S|re.M)
        fp=open("D:\A\https.txt", "w+b")
        for url in link:
            if url[0] == 'h':
                fp.write(url.encode("utf-8")+b'\n')
        fp.close()
        craw(url)
        #messagebox.showinfo('Message','%s' %url)#显示输出
    def quit(self):
        self.titletLabel["text"]=''
        self.input.delete('0','end')
app = Application()  
app.master.title("极简网页爬虫")#窗口标题
app.master.geometry('800x50')
app.mainloop()
