from tkinter import *


# Always at the start, it will create a window
root = Tk()

user_input = Entry(root, width=50, bg='black', fg='white', borderwidth=10)
user_input.pack()
user_input.insert(0, 'Pleace enter your name: ')

def get_squares(number):
    user_input.delete(0, END)
    user_input.insert(0, int(number) ** 2)


# title
root.title('Title name')
root.geometry(400*500)

# myLabel = Label(root, text='Hello world').pack()
myButton = Button(root, text='Get squares', padx=50, pady=50, bg='#000000', fg='red', command=lambda: get_squares(user_input.get())).pack

# Always in the end
root.mainloop()