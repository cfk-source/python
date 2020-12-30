from future.moves import tkinter
from future.moves.tkinter import messagebox
from pandas._typing import Label



# Always at the start, it will create a window


root = Tk()

# title for program window
root.title('Title name')
root.geometry(400*500)
root.iconbitmap('python_icon.ico')


# showinfo, showwarning, showerror, askquestion, ask ok cancel, ask ok cencel
def clicked():
    responce = messagebox.askyesno('this is window', 'Some text')
    Label(root, text=responce).pack
    if responce == 1:

Button(root, text='Click me', command=clicked).pack()


# Always in the end
root.mainloop()