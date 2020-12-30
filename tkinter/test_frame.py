from tkinter import *



# Always at the start, it will create a window
root = Tk()



# title for program window
root.title('Title name')
root.geometry(400*500)
root.iconbitmap('python_icon.ico')

frame = LableFrame(root, text='This is frame', padx=50, pady=50)
frame.pack(padx=10, pady=20)

btn = Button(frame, text='Click me').pack
btn2 = Button(root, text='Click me to').pack

# Always in the end
root.mainloop()