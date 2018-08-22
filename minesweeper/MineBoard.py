import random
from numpy import *

class MineBoard():
    def __init__(self, row, col, minenum):
        self.__row = row
        self.__col = col
        self.__minenum = minenum
        self.__mboa = array([[0 for i in range(col)] for j in range(row)])
        self.__nboa = array([[0 for i in range(col)] for j in range(row)])
        self.__boa = array([[0 for i in range(col)] for j in range(row)])
        self.reset()
        self.__flag = 0#0尚未分出胜负，1胜-1负

    def getflag(self):
        return self.__flag

    def setflag(self, flag):
        self.__flag = flag
    
    def reset(self):
        mlist = []
        i = 0
        while i < self.__minenum:#雷的位置
            ri = random.randint(0, self.__row * self.__col - 1)
            if ri not in mlist:
                mlist.append(ri)
                i += 1
                self.__mboa[ri // self.__col][ri % self.__row] = -1

        for i in range(self.__row):#计算其他位置的数字值
            for j in range(self.__col):
                self.__nboa[i][j] = self.setvalue(i, j)
        self.__boa = self.__mboa + self.__nboa

    def getboard(self):
        return self.__boa

    #计算每一个位置的值
    def setvalue(self, i, j):
        if self.__mboa[i][j] == -1:
            return 0
        if i - 1 < 0:
            if j - 1 < 0:#左上角
                return -(self.__mboa[i][j + 1] + self.__mboa[i + 1][j] + self.__mboa[i + 1][j + 1])
            elif j - 1 >= 0 and j + 1 < self.__row:#最上列
                return -(self.__mboa[i][j - 1] + self.__mboa[i][j + 1] + self.__mboa[i + 1][j - 1] + self.__mboa[i + 1][j] + self.__mboa[i + 1][j + 1])
            else:#右上角
                return -(self.__mboa[i][j - 1] + self.__mboa[i + 1][j - 1] + self.__mboa[i + 1][j])
        elif i - 1 >= 0 and i + 1 < self.__row:
            if j - 1 < 0:#最左列
                return -(self.__mboa[i - 1][j] + self.__mboa[i - 1][j + 1] + self.__mboa[i][j + 1] + self.__mboa[i + 1][j] + self.__mboa[i + 1][j + 1])
            elif j - 1 >= 0 and j + 1 < self.__row:#内层
                return -(self.__mboa[i - 1][j - 1] + self.__mboa[i - 1][j] + self.__mboa[i - 1][j + 1] + self.__mboa[i][j - 1] + self.__mboa[i][j + 1] + self.__mboa[i + 1][j - 1] + self.__mboa[i + 1][j] + self.__mboa[i + 1][j + 1])
            else:#最右列
                return -(self.__mboa[i - 1][j - 1] + self.__mboa[i - 1][j] + self.__mboa[i][j - 1] + self.__mboa[i + 1][j - 1] + self.__mboa[i + 1][j])
        else:
            if j - 1 < 0:#左下角
                return -(self.__mboa[i - 1][j + 1] + self.__mboa[i - 1][j] + self.__mboa[i][j + 1])
            elif j - 1 >= 0 and j + 1 < self.__row:#最下列
                return -(self.__mboa[i - 1][j - 1] + self.__mboa[i - 1][j] + self.__mboa[i - 1][j + 1] + self.__mboa[i][j - 1] + self.__mboa[i][j + 1])
            else:#右下角
                return -(self.__mboa[i - 1][j - 1] + self.__mboa[i - 1][j] + self.__mboa[i][j - 1])
