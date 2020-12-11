#!/usr/bin/env python

import sys
import os
from functools import partial
from tkFileDialog import askdirectory
import Tkinter as tk
import tkMessageBox
import subprocess as sub
import ttk

from os import listdir
my_dir = '/home/tseibel/deep-visualization-toolbox/data_pull/auto/'
layers = [a_dir for a_dir in os.listdir(my_dir) if os.path.isdir(os.path.join(my_dir,a_dir))]
####################################################

data = {} # dictionary to store all the IntVars
####################################################
####################################################

top = tk.Tk()
top.title('SPM COMPARISON FOR DVT')

####################################################
def onEnterDir(dropdown, var):
    path = askdirectory()
    if not path:
        return
    filenames = os.listdir(path)
    dropdown.configure(state='normal')  # Enable drop down
    menu = dropdown['menu']

    # Clear the menu.
    menu.delete(0, 'end')
    for name in filenames:
        # Add menu items.
        menu.add_command(label=name, command=lambda name=name: var.set(name))
        # OR menu.add_command(label=name, command=partial(var.set, name))

def run_program():
    x = dropdownVar1.get()
    y = dropdownVar2.get()
    with open("Array_1.txt", 'w') as outfile:
        outfile.write(x)
    with open("Array_2.txt", 'w') as outfile:
        outfile.write(y)
    os.system('python /home/tseibel/deep-visualization-toolbox/data_pull/filter_avg.py')


def Input1():
    with open("Input1.txt", 'w') as outfile:
        outfile.write(e1.get())

def Input2():
    with open("Input2.txt", 'w') as outfile:
        outfile.write(e2.get())

def u_b_press():
    with open("output.txt", "r") as f:
        label.config(text=f.read())

def print_ingredients(*args):
    values = [[filter, var.get()] for filter, var in data.items()]
    f_values = ''
    for v in values:
        if v[1] == 1:
            f_values += ' ' + v[0]
    print f_values
    with open("filters.txt", "w") as outfile:
        outfile.write(f_values)
#################################################### 
#TAB1
####################################################
frame1 = tk.Frame(top, borderwidth=2, relief='ridge')
frame2 = tk.Frame(top, borderwidth=2, relief='ridge')
frame3 = tk.Frame(top, borderwidth=2, relief='ridge')
frame4 = tk.Frame(top, borderwidth=2, relief='ridge')
frame5 = tk.Frame(top, borderwidth=2, relief='ridge')
frame6 = tk.Frame(top, borderwidth=2, relief='ridge')
frame7 = tk.Frame(top, borderwidth=2, relief='ridge')
frame8 = tk.Frame(top, borderwidth=2, relief='ridge')
frame9 = tk.Frame(top, borderwidth=2, relief='ridge')
frame10 = tk.Frame(top, borderwidth=2, relief='ridge')
frame11 = tk.Frame(top, borderwidth=2, relief='ridge')
frame12 = tk.Frame(top, borderwidth=2, relief='ridge')
frame13 = tk.Frame(top, borderwidth=2, relief='ridge')

frame1.grid(column=0, row=0, sticky="nsew")
frame2.grid(column=1, row=0, sticky="nsew")
frame3.grid(column=0, row=1, sticky="nsew")
frame4.grid(column=1, row=1, sticky="nsew")
frame5.grid(column=0, row=2, sticky="nsew", columnspan=2)
frame6.grid(column=0, row=3, sticky="nsew")
frame7.grid(column=1, row=3, sticky="nsew")
frame8.grid(column=0, row=4, sticky="nsew")
frame9.grid(column=1, row=4, sticky="nsew")
frame10.grid(column=0, row=5, sticky="nsew", columnspan=2)
frame11.grid(column=0, row=6, sticky="nsew", columnspan=2)
frame12.grid(column=0, row=7, sticky="nsew", columnspan=2)
frame13.grid(column=0, row=8, sticky="nsew", columnspan=2)
####################################################
#VARIABLES
dropdownVar1 = tk.StringVar()
dropdownVar2 = tk.StringVar()
var1 = tk.IntVar()
var2 = tk.IntVar()
####################################################
#input1
e1 = tk.Entry(frame2)
b1 = tk.Button(frame1, text ="Black Space Threshold", command = Input1)
#input2
e2 = tk.Entry(frame4)
b2 = tk.Button(frame3, text ="Activation Threshold", command = Input2)
#RUN Button
run_B = tk.Button(frame5,text="RUN",command= run_program)
#FILE Button #1
file_B1 = tk.Button(frame6, text='Image 1', command=lambda: onEnterDir(dropdown1, dropdownVar1))
dropdown1 = tk.OptionMenu(frame7, dropdownVar1, "Select")
dropdown1.configure(state="disabled")
#FILER Button #2
file_B2 = tk.Button(frame8, text='Image 2', command=lambda: onEnterDir(dropdown2, dropdownVar2))
dropdown2 = tk.OptionMenu(frame9, dropdownVar2, "Select")
dropdown2.configure(state="disabled")
# UPDATE Button
u_b = tk.Button(frame12, text ="UPDATE", command=u_b_press)
####################################################
label = tk.Label(frame12, text = 'empty')
####################################################
mb =  tk.Menubutton(frame10, text="Layers", relief='ridge' )
mb.menu  =  tk.Menu(mb, tearoff = 0 )
mb["menu"]  =  mb.menu

for layer in layers:
    var = tk.IntVar()
    mb.menu.add_checkbutton(label=layer, variable=var)
    data[layer] = var # add IntVar to the dictionary

menu_btn = tk.Button(frame11, text="Update Layers", command=print_ingredients)

#####################################################
menu_btn.pack(fill='x')
mb.pack(fill='x')
e1.pack(fill='x')
e2.pack(fill='x')
b1.pack(fill='x')
b2.pack(fill='x')
run_B.pack(fill='x')
file_B1.pack(fill='x')
dropdown1.pack(fill='x')
file_B2.pack(fill='x')
dropdown2.pack(fill='x')
u_b.pack(fill='x')
label.pack(fill='x')
####################################################
#
####################################################



top.mainloop()