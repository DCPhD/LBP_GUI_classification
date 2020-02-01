from tkinter import *


def fracture():
    if var1.get() + var2.get() + var3.get() + var14.get() + var15.get() + var16.get() >=3:
        print('Increased risk for fracture')
    else:
        print('Low risk for fracture')


def cancer():
    if var4.get() + var5.get() + var3.get() >=1:
        print('Increased risk for cancer')
    else:
        print('Low risk for cancer')


def infection():
    if var6.get() + var7.get() + var8.get() >=2:
        print('Increased risk for infection')
    else:
        print('Low risk for infection')


def cauda_equina():
    if var9.get() + var10.get() >=1:
        print('Increased risk for cauda equina syndrome')
    else:
        print('Low risk for cauda equina syndrome')


def AAA():
    if var11.get() + var12.get() + var13.get() >=2:
        print('Increased risk for Abdominal Aortic Aneurysm')
    else:
        print('Low risk for Abdominal Aortic Aneurysm')


root = Tk()
root.wm_title('Red Flags')
root.configure(bg='black')

# Fracture
var1 = IntVar()
cb_1 = Checkbutton(root, text='Is your age >70 ?', variable=var1, command=fracture, bg='black',fg='white')
cb_1.pack(anchor='w')

var2 = IntVar()
cb_2 = Checkbutton(root, text='Have you been diagnosed with osteopenia or osteoporosis ?',
                   variable=var2, command=fracture, bg='black',fg='white')
cb_2.pack(anchor='w')

var3 = IntVar()
cb_3 = Checkbutton(root, text='Have you experienced recent spine related trauma ?',
                   variable=var3, command=fracture, bg='black',fg='white')
cb_3.pack(anchor='w')

var14 = IntVar()
cb_14 = Checkbutton(root, text='Do you consider yourself underweight ?',
                    variable=var14, command=fracture, bg='black',fg='white')
cb_14.pack(anchor='w')

var15 = IntVar()
cb_15 = Checkbutton(root, text='Are you female ?',
                    variable=var15, command=fracture, bg='black',fg='white')
cb_15.pack(anchor='w')

var16 = IntVar()
cb_16 = Checkbutton(root, text='Have you used oral steroid medication (i.e. prednisone) for more than 1 month ?',
                    variable=var16, command=fracture, bg='black',fg='white')
cb_16.pack(anchor='w')

# Cancer
var4 = IntVar()
cb_4 = Checkbutton(root, text='Have you recently lost weight without trying ?',
                   variable=var4, command=cancer, bg='black',fg='white')
cb_4.pack(anchor='w')

var5 = IntVar()
cb_5 = Checkbutton(root, text='Do you have a history of cancer ?',
                   variable=var5, command=cancer, bg='black',fg='white')
cb_5.pack(anchor='w')

# infection
var6 = IntVar()
cb_6 = Checkbutton(root, text='Have you recently experienced fever or chills ?',
                   variable=var6, command=infection, bg='black',fg='white')
cb_6.pack(anchor='w')

var7 = IntVar()
cb_7 = Checkbutton(root, text='Have you recently had an infection ?',
                   variable=var7, command=infection, bg='black',fg='white')
cb_7.pack(anchor='w')

var8 = IntVar()
cb_8 = Checkbutton(root,
                   text='Do you have a weakened immune system from cancer, autoimmunity or other medical problems ?',
                   variable=var8, command=infection, bg='black',fg='white')
cb_8.pack(anchor='w')

# cauda equina
var9 = IntVar()
cb_9 = Checkbutton(root, text='Have you recently had a problem controlling your bowel or bladder function ?',
                   variable=var9, command=cauda_equina, bg='black',fg='white')
cb_9.pack(anchor='w')

var10 = IntVar()
cb_10 = Checkbutton(root, text='Do you have any numbness in your groin area ?',
                    variable=var10, command=cauda_equina, bg='black',fg='white')
cb_10.pack(anchor='w')

# AAA
var11 = IntVar()
cb_11 = Checkbutton(root, text='Have you been diagnosed with hypertension?',
                    variable=var11, command=AAA, bg='black',fg='white')
cb_11.pack(anchor='w')

var12 = IntVar()
cb_12 = Checkbutton(root, text='Can you feel a pulsation in your abdomen ?',
                    variable=var12, command=AAA, bg='black',fg='white')
cb_12.pack(anchor='w')

var13 = IntVar()
cb_13 = Checkbutton(root, text='Is your age >60 ?', variable=var13, command=AAA, bg='black',fg='white')
cb_13.pack(anchor='w')

root.mainloop()