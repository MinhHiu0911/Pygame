from tkinter import*
root=Tk()

Label(root,text='Nhap A*',font=('camvria',20),width=25 ).grid(row=1)
root.minsize(height=500,width=400)
Label(root,width=60,height=20).grid(row=1,column=2)
        

Entry(root,width=25,textvariable=id).grid(row=2,column=1)
button=Frame(root)
Button(button,text='Them').pack(side=LEFT)
Button(button,text='back', command=root.quit).pack(side=LEFT)
         
button.grid(row=3,column=1)
 
root.mainloop()