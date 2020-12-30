from future.moves import tkinter


# Always at the start, it will create a window
root = Tk()

# title for program window
root.title('Title name')
root.geometry(400*500)
root.iconbitmap('python_icon.ico')

def show_check_status():
    myLable = Lable(root, text=some_var.get()).pack

chk_box = Checkbutton(root, text='Click me', variable=some_var).pack()
myLable - Lable(root, text=some_var.get()).pack()
myButton = Button(root, text='Show check status', command=chow_check_status).pack
chk_box = Chekbutton(root, text'Check me', variable=some_var, onvalue='ON', offvalue='OFF')
chk_box.deselct()
chk_box.pack()


# Always in the end
root.mainloop()