import tkinter
from tkinter import *
import tkinter as tk
from tkinter import Tk, Canvas, Frame, BOTH

def WriteIter(canv,x1,x2,y1,y2):
    a = list()
    a=[[x1,y1],[x1+(x2-x1)/3,y1+(y2-y1)/3],[x1+(x2-x1)*2/3,y1+(y2-y1)*2/3],[x2,y2]]
    b = list()
    b = a
    a = [[x1,y1],[x1+(x2-x1)/3,y1+(y2-y1)/3],[b[1][0]+(b[1][0]-x1)/2-((3**1/2)/2)*(b[1][1]-y1),b[1][1]+(b[1][0]-x1)*((3**1/2)/2)+(b[1][1]-y1)/2],[x1+(x2-x1)*2/3,y1+(y2-y1)*2/3],[x2,y2]]
    for i in range(0,4):
        canv.create_line(a[i][0],a[i][1],a[i+1][0],a[i+1][1])
    canv.create_line(a[1][0],a[1][1],a[3][0],a[3][1], fill = "white")
    return a

def Koch(canv,listOfAngles,num):
    if num == 0:
        return
    new = list()
    new = listOfAngles
    for i in range(0,len(listOfAngles)):
        tmp = list()
        tmp = WriteIter(canv,listOfAngles[i][0],listOfAngles[i][1],listOfAngles[i+1][0],listOfAngles[i+1][1])
        k = 0
        for j in tmp:
            new.insert(i+k,j)
            k = k + 1
    listOfAngles = new
    num = num - 1
    Koch(canv,listOfAngles,num)


if __name__ == '__main__':
    root = Tk()
    listOfAngles = list()
    canv = Canvas(root, width=1000, height=1000)
    num = int(input())
    listOfAngles = [[0, 0], [1000, 0]]
    Koch(canv,listOfAngles,num)
    canv.pack()
    root.mainloop()