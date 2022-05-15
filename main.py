import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib import *
import numpy as np
from numpy import *
import time
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from math import pi,cos
win=tk.Tk()
win.geometry('1600x1600')
win.title('Тазтдинов Денис АЭ-21-03 Инфа лабораторная работа номер 5')
x1=[]
y1=[]
z=[]
n=10
a=0
b=2*pi
h=(b-a)/n
step=1
while a!=b:
    x=a
    z.append(step)
    x1.append(a)
    y1.append(1/((2+cos(x))*(3+cos(x))))
    step+=1
    a+=h
print(x1)
print(y1)
print(z)
print(x1,y1)
frame1=Frame(win)
frame1.place(relx=0,rely=0)
def orig():
    graph = Frame(win, bg='red')  # создание графика
    z = Figure(figsize=(8, 6), dpi=40)
    plt = z.add_subplot(111)
    plt.grid()
    plt.plot(x1, y1,'r')
    plt.set_xlabel('Ось X', fontsize=15)
    plt.set_ylabel('Ось Y', fontsize=15)
    canvas = FigureCanvasTkAgg(z, master=graph)
    canvas.get_tk_widget().pack(side=LEFT, fill=BOTH)
    graph.place(relx=0.8, rely=0.03)
def kv():
    t=np.polyfit(x1,y1,2)
    f=np.poly1d(t)
    ynew=[]
    for i in range(n):
        ynew.append(f(x1[i]))
    print(f)
    graph = Frame(win, bg='red')  # создание графика
    z = Figure(figsize=(8, 6), dpi=40)
    plt = z.add_subplot(111)
    plt.grid()
    plt.plot(x1,y1,'o',x1,f(x1),'-r')
    plt.set_xlabel('Ось X', fontsize=15)
    plt.set_ylabel('Ось Y', fontsize=15)
    canvas = FigureCanvasTkAgg(z, master=graph)
    canvas.get_tk_widget().pack(side=LEFT, fill=BOTH)
    graph.place(relx=0, rely=0.03)
    graph1=Frame(win)
    graph1.place(relx=0,rely=0.4)
    tk.Label(graph1,text='шаг').pack()
    graph2 = Frame(win)
    graph2.place(relx=0.02, rely=0.4)
    graph3 = Frame(win)
    graph3.place(relx=0.06, rely=0.4)
    tk.Label(graph3, text='Полиномный Y').pack()
    graph4 = Frame(win)
    graph4.place(relx=0.12, rely=0.4)
    tk.Label(graph4, text='абс погр-ть').pack()
    graph5 = Frame(win)
    graph5.place(relx=0.18, rely=0.4)
    tk.Label(graph5, text='отн погр-ть').pack()
    tk.Label(graph2, text='Y').pack()
    for i in range(1,n+1):
        tk.Label(graph1,text=i).pack()
    for i in y1:
        tk.Label(graph2, text='%.5f'%i).pack()
    for i in ynew:
        tk.Label(graph3, text='%.5f'%i).pack()
    for i in range(n):
        tk.Label(graph4, text='%.5f'%(abs(y1[i]-ynew[i]))).pack()
    for i in range(n):
        tk.Label(graph5, text='%.5f'%(abs((y1[i]-ynew[i]))/y1[i])).pack()
def tr():
    t=np.polyfit(x1,y1,3)
    f=np.poly1d(t)
    ynew = []
    for i in range(n):
        ynew.append(f(x1[i]))
    print(f)
    graph = Frame(win, bg='red')  # создание графика
    z = Figure(figsize=(8, 6), dpi=40)
    plt = z.add_subplot(111)
    plt.grid()
    plt.plot(x1,y1,'o',x1,f(x1),'-r')
    plt.set_xlabel('Ось X', fontsize=15)
    plt.set_ylabel('Ось Y', fontsize=15)
    canvas = FigureCanvasTkAgg(z, master=graph)
    canvas.get_tk_widget().pack(side=LEFT, fill=BOTH)
    graph.place(relx=0.2, rely=0.03)
    graph2 = Frame(win)
    graph2.place(relx=0.02+0.22, rely=0.4)
    graph3 = Frame(win)
    graph3.place(relx=0.06+0.22, rely=0.4)
    tk.Label(graph3, text='Полиномный Y').pack()
    graph4 = Frame(win)
    graph4.place(relx=0.12+0.22, rely=0.4)
    tk.Label(graph4, text='абс погр-ть').pack()
    graph5 = Frame(win)
    graph5.place(relx=0.18+0.22, rely=0.4)
    tk.Label(graph5, text='отн погр-ть').pack()
    tk.Label(graph2, text='Y').pack()
    for i in y1:
        tk.Label(graph2, text='%.5f' % i).pack()
    for i in ynew:
        tk.Label(graph3, text='%.5f' % i).pack()
    for i in range(n):
        tk.Label(graph4, text='%.5f' % (abs(y1[i] - ynew[i]))).pack()
    for i in range(n):
        tk.Label(graph5, text='%.5f' % (abs((y1[i] - ynew[i])) / y1[i])).pack()
def chet():
    t=np.polyfit(x1,y1,4)
    f=np.poly1d(t)
    ynew = []
    for i in range(n):
        ynew.append(f(x1[i]))
    print(f)
    graph = Frame(win, bg='red')  # создание графика
    z = Figure(figsize=(8, 6), dpi=40)
    plt = z.add_subplot(111)
    plt.grid()
    plt.plot(x1,y1,'o',x1,f(x1),'-r')
    plt.set_xlabel('Ось X', fontsize=15)
    plt.set_ylabel('Ось Y', fontsize=15)
    canvas = FigureCanvasTkAgg(z, master=graph)
    canvas.get_tk_widget().pack(side=LEFT, fill=BOTH)
    graph.place(relx=0.4, rely=0.03)
    graph2 = Frame(win)
    graph2.place(relx=0.02 + 0.44, rely=0.4)
    graph3 = Frame(win)
    graph3.place(relx=0.06 + 0.44, rely=0.4)
    tk.Label(graph3, text='Полиномный Y').pack()
    graph4 = Frame(win)
    graph4.place(relx=0.12 + 0.44, rely=0.4)
    tk.Label(graph4, text='абс погр-ть').pack()
    graph5 = Frame(win)
    graph5.place(relx=0.18 + 0.44, rely=0.4)
    tk.Label(graph5, text='отн погр-ть').pack()
    tk.Label(graph2, text='Y').pack()
    for i in y1:
        tk.Label(graph2, text='%.5f' % i).pack()
    for i in ynew:
        tk.Label(graph3, text='%.5f' % i).pack()
    for i in range(n):
        tk.Label(graph4, text='%.5f' % (abs(y1[i] - ynew[i]))).pack()
    for i in range(n):
        tk.Label(graph5, text='%.5f' % (abs((y1[i] - ynew[i])) / y1[i])).pack()
def five():
    t=np.polyfit(x1,y1,5)
    f=np.poly1d(t)
    ynew = []
    for i in range(n):
        ynew.append(f(x1[i]))
    print(f)
    graph = Frame(win, bg='red')  # создание графика
    z = Figure(figsize=(8, 6), dpi=40)
    plt = z.add_subplot(111)
    plt.grid()
    plt.plot(x1,y1,'o',x1,f(x1),'-r')
    plt.set_xlabel('Ось X', fontsize=15)
    plt.set_ylabel('Ось Y', fontsize=15)
    canvas = FigureCanvasTkAgg(z, master=graph)
    canvas.get_tk_widget().pack(side=LEFT, fill=BOTH)
    graph.place(relx=0.6, rely=0.03)
    graph2 = Frame(win)
    graph2.place(relx=0.02 + 0.66, rely=0.4)
    graph3 = Frame(win)
    graph3.place(relx=0.06 + 0.66, rely=0.4)
    tk.Label(graph3, text='Полиномный Y').pack()
    graph4 = Frame(win)
    graph4.place(relx=0.12 + 0.66, rely=0.4)
    tk.Label(graph4, text='абс погр-ть').pack()
    graph5 = Frame(win)
    graph5.place(relx=0.18 + 0.66, rely=0.4)
    tk.Label(graph5, text='отн погр-ть').pack()
    tk.Label(graph2, text='Y').pack()
    for i in y1:
        tk.Label(graph2, text='%.5f' % i).pack()
    for i in ynew:
        tk.Label(graph3, text='%.5f' % i).pack()
    for i in range(n):
        tk.Label(graph4, text='%.5f' % (abs(y1[i] - ynew[i]))).pack()
    for i in range(n):
        tk.Label(graph5, text='%.5f' % (abs((y1[i] - ynew[i])) / y1[i])).pack()
def vivod():
    tk.Label(win, text='Самый лучший способ с полиномами в 5 степени,доказано эмпирическим путем',font='Times 22').place(relx=0.2, rely=0.8)
tk.Button(win,text='Полином второй степени',command=kv).place(relx=0,rely=0)
tk.Button(win,text='Полином третьей степени',command=tr).place(relx=0.2, rely=0)
tk.Button(win,text='Полином четвертой степени',command=chet).place(relx=0.4, rely=0)
tk.Button(win,text='Полином пятой степени',command=five).place(relx=0.6, rely=0)
tk.Button(win,text='Оригинал',command=orig).place(relx=0.8, rely=0)
tk.Button(win,text='Вывод',command=vivod).place(relx=0, rely=0.8)
win.mainloop()


