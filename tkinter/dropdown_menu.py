from future.moves import tkinter


# Always at the start, it will create a window
root = Tk()

# title for program window
root.title('Title name')
root.geometry(400*500)
root.iconbitmap('python_icon.ico')


def show():
    myLable = Lable(root, text=clicked.get()).pack



# drop down menu
clicked = StringVar()
clicked.set('Monday')
dropdown = OptionMenu(root, clicked, *menu_list)
dropdown.pack()


# Always in the end
root.mainloop()