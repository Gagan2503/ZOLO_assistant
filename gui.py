import threading
from tkinter import *
from PIL import Image, ImageSequence, ImageTk
import time
import threading

from tkinter.ttk import Button

root = Tk()
root.geometry("700x620")
root.configure(bg='blue')
frame = Frame(root, width=600, height=400, )
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("cute-robot-waving-hand-cartoon-260nw-1917055787_prev_ui.png"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()

my_lable = Label(root, text=' i am yur virtual assistant', font=('ubuntu', 15, 'bold'), bg='black', fg='white')
my_lable.pack()



# Demo function 1
def fun1():
    print("Function 1")


# Demo function 2
def fun2():
    print("Function 2")


# if __name__ == "__main__":
    # Creating top-level window
    # Creating a button with more than one command using lambda
    # button = Button(root, text="Button",bg= 'white', command=lambda: [fun1(), fun2()])

    # Attaching button to the top-level window
    # Always remember to attach your widgets to the top-level
    # button.pack()

    # Mainloop that will run forever
    # master.mainloop()


def play_gif():
    img = Image.open("ios_9.gif")
    lbl = Label(root)
    lbl.place(x=0, y=0)

    for img in ImageSequence.Iterator(img):
        img = img.resize((695, 500))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        lbl.config(bg='black')

        root.update()
        time.sleep(0.01)
    root.after(0, play_gif)


def exit():
    root.destroy()

#
btn=Button(root, text="RUN", command=lambda: [play_gif(), my_lable])
btn.pack()
# Button(root, text="EXIT", command=exit, font=('ubuntu', 15, 'bold'), bg='red', fg='black').place(x=550, y=550)
#
root.mainloop()
