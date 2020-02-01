from tkinter import *


def IVD():
    if var1.get() + var2.get() + var3.get() + var4.get() + var5.get() >=3:
        print('Increased likelihood for Disc involvement')
    else:
        print('Low likelihood for Disc involvement')


def facet():
    if var6.get() + var7.get() + var8.get() + var9.get() >=3:
        print('Increased likelihood for Facet involvement')
    else:
        print('Low likelihood for Facet involvement')


def stenosis():
    if var10.get() + var11.get() + var12.get() + var13.get() + var14.get() >=3:
        print('Increased likelihood for Stenosis')
    else:
        print('Low likelihood for Stenosis')


def radiculopathy():
    if var15.get() == 1 or var18.get() == 1:
        print('Increased likelihood for radiculopathy')
    elif var16.get() == 1 or var17.get() == 1:
        print('Consider diabetic neuropathy')
    else:
        print('Low likelihood for radiculopathy')


def muscle():
    if var19.get() + var20.get() + var21.get() >=2:
        print('Increased likelihood for muscle involvement')
    else:
        print('Low likelihood for muscle involvement')


def instability():
    if var22.get() + var23.get() + var24.get() >=2:
        print('Increased likelihood for instability')
    else:
        print('Low likelihood for instability')


root = Tk()
root.wm_title('Origin of Low Back Pain')
root.configure(bg='black')

# IVD
var1 = IntVar()
cb_1 = Checkbutton(root, text='Are you favoring one leg when you walk ?',
                   variable=var1, command=IVD, bg='black',fg='white')
cb_1.pack(anchor='w')

var2 = IntVar()
cb_2 = Checkbutton(root, text='Is your back pain worse in the morning ?',
                   variable=var2, command=IVD, bg='black',fg='white')
cb_2.pack(anchor='w')

var3 = IntVar()
cb_3 = Checkbutton(root, text='Is your back pain worse when you are sitting and better when moving ?',
                   variable=var3, command=IVD, bg='black',fg='white')
cb_3.pack(anchor='w')

var4 = IntVar()
cb_4 = Checkbutton(root, text='If you have sciatica, can you position yourself to decrease your leg pain ?',
                   variable=var4, command=IVD, bg='black',fg='white')
cb_4.pack(anchor='w')

var5 = IntVar()
cb_5 = Checkbutton(root, text='Are your hips shifted to one side when you stand or sit ?',
                   variable=var5, command=IVD, bg='black',fg='white')
cb_5.pack(anchor='w')

# facet
var6 = IntVar()
cb_6 = Checkbutton(root, text='Is your age greater than or equal to 50 ?',
                   variable=var6, command=facet, bg='black',fg='white')
cb_6.pack(anchor='w')

var7 = IntVar()
cb_7 = Checkbutton(root, text='Is your back pain better when sitting ?',
                   variable=var7, command=facet, bg='black',fg='white')
cb_7.pack(anchor='w')

var8 = IntVar()
cb_8 = Checkbutton(root, text='Is your back pain better when walking ?',
                   variable=var8, command=facet, bg='black',fg='white')
cb_8.pack(anchor='w')

var9 = IntVar()
cb_9 = Checkbutton(root, text='Is your pain localized to a specific area to one side of your spine ?',
                   variable=var9, command=facet, bg='black',fg='white')
cb_9.pack(anchor='w')

# stenosis
var10 = IntVar()
cb_10 = Checkbutton(root, text='Is your age greater than or equal to 65 ?',
                    variable=var10, command=stenosis, bg='black',fg='white')
cb_10.pack(anchor='w')

var11 = IntVar()
cb_11 = Checkbutton(root, text='Is your leg pain more intense than your back pain ?',
                    variable=var11, command=stenosis, bg='black',fg='white')
cb_11.pack(anchor='w')

var12 = IntVar()
cb_12 = Checkbutton(root, text='Is your leg pain aggravated by walking and relieved by sitting ?',
                    variable=var12, command=stenosis, bg='black',fg='white')
cb_12.pack(anchor='w')

var13 = IntVar()
cb_13 = Checkbutton(root, text='Do you experience pain in both legs ?', variable=var13,
                    command=stenosis, bg='black',fg='white')
cb_13.pack(anchor='w')

var14 = IntVar()
cb_14 = Checkbutton(root, text='Has it been more than 6 months since your symptoms began ?',
                    variable=var14, command=stenosis, bg='black',fg='white')
cb_14.pack(anchor='w')

# radiculopathy
var15 = IntVar()
cb_15 = Checkbutton(root, text='Do you have a loss of sensation in one foot ?', variable=var15,
                    command=radiculopathy, bg='black',fg='white')
cb_15.pack(anchor='w')

var16 = IntVar()
cb_16 = Checkbutton(root, text='Do you have a loss of sensation in both feet ?', variable=var16,
                    command=radiculopathy, bg='black',fg='white')
cb_16.pack(anchor='w')

var17 = IntVar()
cb_17 = Checkbutton(root, text='Have you been diagnosed with Diabetes ?', variable=var17,
                    command=radiculopathy, bg='black',fg='white')
cb_17.pack(anchor='w')

var18 = IntVar()
cb_18 = Checkbutton(root, text='Does your leg pain worsen when extending your knee while sitting (i.e. driving) ?',
                    variable=var18, command=radiculopathy, bg='black',fg='white')
cb_18.pack(anchor='w')

# muscle
var19 = IntVar()
cb_19 = Checkbutton(root, text='Can you create your pain by pushing on a muscle in your low back ?',
                    variable=var19, command=muscle, bg='black',fg='white')
cb_19.pack(anchor='w')

var20 = IntVar()
cb_20 = Checkbutton(root, text='Is there swelling in the area where your low back pain is ?',
                    variable=var20, command=muscle, bg='black',fg='white')
cb_20.pack(anchor='w')

var21 = IntVar()
cb_21 = Checkbutton(root, text='Was there an injury associated with the onset of your low back pain ?',
                    variable=var21, command=muscle, bg='black',fg='white')
cb_21.pack(anchor='w')

# instability
var22 = IntVar()
cb_22 = Checkbutton(root, text='Have you had frequent (>5) episodes of low back pain ?',
                    variable=var22, command=instability, bg='black',fg='white')
cb_22.pack(anchor='w')

var23 = IntVar()
cb_23 = Checkbutton(root, text='Do you believe you are more flexible than average ?', variable=var23,
                    command=instability, bg='black',fg='white')
cb_23.pack(anchor='w')

var24 = IntVar()
cb_24 = Checkbutton(root, text='Are you less than or equal to 40 years old ?', variable=var24,
                    command=instability, bg='black',fg='white')
cb_24.pack(anchor='w')


root.mainloop()