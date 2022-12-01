from tkinter import *
root=Tk()
f1 = Frame(root, bg="green", borderwidth=3,relief=SUNKEN)
f1.pack(fill='x')

f2 = Frame(root, bg="grey", borderwidth=5,relief=SUNKEN)
f2.pack(side='left',fill='y')

f3 = Frame(root, bg="grey", borderwidth=5,relief=SUNKEN)
f3.pack(side='right',fill='y')

f4 = Frame(root, bg="grey", borderwidth=5,relief=SUNKEN)
f4.pack(side='bottom',fill='x')

l1=Label(f1,text='sonu vishwakarma')
l1.pack(pady=5)

l2=Label(f1,text='Mr.sudhir vishwakarma')
l2.pack(pady=12)

l1=Label(f2,text='sonu vishwakarma')
l1.pack(pady=12)

l2=Label(f3,text='Mr.sudhir vishwakarma')
l2.pack(pady=12)

l2=Label(f4,text='copyright@by sonu vishwakarma',padx=113,pady=3
                 )
l2.pack(padx=2 , side='left')
root.mainloop()
