from future.moves import tkinter



# Always at the start, it will create a window
root = Tk()



# title for program window
root.title('Title name')
root.geometry(400*500)
root.iconbitmap('python_icon.ico')


modes = [('one')('1'), ('two', '2')]


choice = StringVar() # (IntVar(), StringVar())
choice.set('one')

for text, mode in modes:
    Radiobutton(root, text=text, variable=choice, value=mode).pack()




def choice_made(value):
    myLable = Lable(root, text=value).pack

Radiobutton(root, text='choice1', value=1, variable=choice).pack()
Radiobutton(root, text='choice2', value=1, variable=choice).pack()

MyButton = (root, text='Click me', command=lambda: choice_made(choice.get())).pack()
myLable = Lable(root, text=choice.get()).pack


# Always in the end
root.mainloop()