from tkinter import *



# Always at the start, it will create a window
root = Tk()



# title for program window
root.title('Title name')
root.geometry(400*500)
root.iconbitmap('python_icon.ico')

image1 = PhotoImage(file='python.png')

myLabel1 = Label(root, image=image1).pack()

quit_button = Button(root, text='EXIT', command=root.quit).pack


# Always in the end
root.mainloop()