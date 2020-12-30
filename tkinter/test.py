from tkinter import *

# Always at the start, it will create a window
root = Tk()

user_input = Entry(root, width=50, bg='black', fg='white', borderwidth=10)
user_input.pack()
user_input.insert(0, 'Pleace enter your name: ')

def myClick():
    myLabel = Label(root, text='Hello ' + user_input.get()).pack

#
# title
root.title('Title name')
root.geometry(400*500)

# myLabel = Label(root, text='Hello world').pack()
myButton = Button(root, text='click', padx=50, pady=50, bg='#000000', fg='red', command=(myClick)).pack

# Always in the end
root.mainloop()