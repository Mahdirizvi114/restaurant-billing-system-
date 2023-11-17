#lets Start

from tkinter import *
from PIL import ImageTk, Image

#creating screen

root= Tk()

root.geometry("1350x800")
root.resizable(0, 0)

#changing root color.
root.configure(bg= "#e8edec")

#now we will make some frame on our root

f1 = Frame(root, bg="#9adbcb", width=1200, height=50, relief=SUNKEN)
f1.pack(side=TOP)

f2 = Frame(root, bg="#e8edec", width=1350, height=700, relief=SUNKEN)
f2.pack(side=LEFT)

# f3 = Frame(root, bg='blue', width=400, height=17, bd=3, relief=RAISED)
# f3.place(x=90, y=125)
#
# f4 = Frame(root, bg='blue', width=400, height=17, bd=3, relief=RAISED)
# f4.place(x=790, y=125)



#adding labels...

top_label = Label(f1, text="Restaurant Billing System", font='Arial 28 bold', bg="#e8edec", fg="#223be0", border=10)
top_label.grid(row=0, column=0)

#Adding more label

l1 = Label(f2, text="References", bg="#e8edec", font='Arial 16')
l1.place(x=5, y=120)

l2 = Label(f2, text="Large Fries", bg="#e8edec", font='Arial 16')
l2.place(x=5, y=180) #Adding all label

l3 = Label(f2, text="Burger Meal", bg="#e8edec", font='Arial 16')
l3.place(x=5, y=240)

l4 = Label(f2, text="Fliet_O_Meal", bg="#e8edec", font='Arial 16')
l4.place(x=5, y=300)

l5 = Label(f2, text="Chicken Meal", bg="#e8edec", font='Arial 16')
l5.place(x=5, y=360)

l6 = Label(f2, text="Cheese Meal", bg="#e8edec", font='Arial 16')
l6.place(x=5, y=420)

l7 = Label(f2, text="Drinks", bg="#e8edec", font='Arial 16')
l7.place(x=500, y=120)

l8 = Label(f2, text="Cost of meal", bg="#e8edec", font='Arial 16')
l8.place(x=500, y=180)

l9 = Label(f2, text="Service Charges", bg="#e8edec", font='Arial 16')
l9.place(x=500, y=240)

l10 = Label(f2, text="State Tax", bg="#e8edec", font='Arial 16')
l10.place(x=500, y=300)

l11 = Label(f2, text="Sub Total", bg="#e8edec", font='Arial 16')
l11.place(x=500, y=360)

l12 = Label(f2, text="Total Tax", bg="#e8edec", font='Arial 16')
l12.place(x=500, y=420)

#now Adding entries of labels....

e1 = Entry(f2, border=7, relief=SUNKEN, font='Arial 16', bg='#1996e3')
e1.place(x=170, y=120)

e2 = Entry(f2, border=7, relief=SUNKEN, font='Arial 16', bg='#1996e3')
e2.place(x=170, y=180)

e3 = Entry(f2, border=7, relief=SUNKEN, font='Arial 16', bg='#1996e3')
e3.place(x=170, y=240)

e4 = Entry(f2, border=7, relief=SUNKEN, font='Arial 16', bg='#1996e3')
e4.place(x=170, y=300)

e5 = Entry(f2, border=7, relief=SUNKEN, font='Arial 16', bg='#1996e3')
e5.place(x=170, y=360)

e6 = Entry(f2, border=7, relief=SUNKEN, font='Arial 16', bg='#1996e3')
e6.place(x=170, y=420)

e7 = Entry(f2, border=7, relief=SUNKEN, font='Arial 16', bg='#1996e3')
e7.place(x=675, y=120)

e8 = Entry(f2, border=7, relief=SUNKEN, font='Arial 16', bg='#1996e3')
e8.place(x=675, y=180)

e9 = Entry(f2, border=7, relief=SUNKEN, font='Arial 16', bg='#1996e3')
e9.place(x=675, y=240)

e10 = Entry(f2, border=7, relief=SUNKEN, font='Arial 16', bg='#1996e3')
e10.place(x=675, y=300)

e11 = Entry(f2, border=7, relief=SUNKEN, font='Arial 16', bg='#1996e3')
e11.place(x=675, y=360)

e12 = Entry(f2, border=7, relief=SUNKEN, font='Arial 16', bg='#1996e3')
e12.place(x=675, y=420)

#now Adding some buttons...

bt1 = Button(f2, text='Total', bg='#2756e3', fg='#e8edec', width=15, height=2, font='Arial 16 bold', relief=RAISED, bd=10)
bt1.place(x=200, y=500)

bt2 = Button(f2, text='Quit', bg='#2756e3', fg='#e8edec', width=15, height=2, font='Arial 16 bold', relief=RAISED, bd=10)
bt2.place(x=450, y=500)

bt3 = Button(f2, text='Reset', bg='#2756e3', fg='#e8edec', width=15, height=2, font='Arial 16 bold', relief=RAISED, bd=10)
bt3.place(x=700, y=500)

#for calculation adding a calculator

#adding entry for calculator in root window


e13 = Entry(root, relief=SUNKEN, bd=15, width=23, font='Arial 16', bg='#27a5b0', fg='#e8edec')
e13.place(x=1000, y=200)

#adding buttons

bt4 = Button(root, text='7', width=5, height=3, font='Arial 14 bold', relief=RAISED, bd=6, bg='#e8edec')
bt4.place(x=1000, y=260)

bt5 = Button(root, text='8', width=5, height=3, font='Arial 14 bold', relief=RAISED, bd=6, bg='#e8edec')
bt5.place(x=1075, y=260)

bt6 = Button(root, text='9', width=5, height=3, font='Arial 14 bold', relief=RAISED, bd=6, bg='#e8edec')
bt6.place(x=1150, y=260)

bt7 = Button(root, text='+', width=5, height=3, font='Arial 14 bold', relief=RAISED, bd=6, bg='#e8edec')
bt7.place(x=1225, y=260)

bt8 = Button(root, text='4', width=5, height=3, font='Arial 14 bold', relief=RAISED, bd=6, bg='#e8edec')
bt8.place(x=1000, y=350)

bt9 = Button(root, text='1', width=5, height=3, font='Arial 14 bold', relief=RAISED, bd=6, bg='#e8edec')
bt9.place(x=1000, y=440)

bt10 = Button(root, text='0', width=5, height=3, font='Arial 14 bold', relief=RAISED, bd=6, bg='#e8edec')
bt10.place(x=1000, y=530)
#
bt11 = Button(root, text='5', width=5, height=3, font='Arial 14 bold', relief=RAISED, bd=6, bg='#e8edec')
bt11.place(x=1075, y=350)

bt12 = Button(root, text='6', width=5, height=3, font='Arial 14 bold', relief=RAISED, bd=6, bg='#e8edec')
bt12.place(x=1150, y=350)

bt13 = Button(root, text='-', width=5, height=3, font='Arial 14 bold', relief=RAISED, bd=6, bg='#e8edec')
bt13.place(x=1225, y=350)
#
bt14 = Button(root, text='2', width=5, height=3, font='Arial 14 bold', relief=RAISED, bd=6, bg='#e8edec')
bt14.place(x=1075, y=440)

bt15 = Button(root, text='3', width=5, height=3, font='Arial 14 bold', relief=RAISED, bd=6, bg='#e8edec')
bt15.place(x=1150, y=440)

bt16 = Button(root, text='*', width=5, height=3, font='Arial 14 bold', relief=RAISED, bd=6, bg='#e8edec')
bt16.place(x=1225, y=440)

bt17 = Button(root, text='C', width=5, height=3, font='Arial 14 bold', relief=RAISED, bd=6, bg='#e8edec')
bt17.place(x=1075, y=530)

bt18 = Button(root, text='=', width=5, height=3, font='Arial 14 bold', relief=RAISED, bd=6, bg='#e8edec')
bt18.place(x=1150, y=530)

bt19 = Button(root, text='/', width=5, height=3, font='Arial 14 bold', relief=RAISED, bd=6, bg='#e8edec')
bt19.place(x=1225, y=530)

# now adding some images first we need to import library for this library to be worked you need to download this package. showing in screen this pillow package
#first of all copy the image which you will use to the filw location. like this

Image1 = Image.open("1.png")
Photo1 = ImageTk.PhotoImage(Image1)
img_label1 = Label(root, image=Photo1, bg='#e8edec')
img_label1.image = Photo1
img_label1.place(x=0, y=0)

#for decoration





root.mainloop()