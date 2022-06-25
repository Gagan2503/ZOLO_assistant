# import tkinter
from tkinter import *
from itertools import count
# import canvas as canvas
# import image
# from PIL import ImageTk, Image, ImageSequence

root = Tk()
root.geometry("600x400")
btn = Button(root, text='Speak', font=('railways', 10, 'bold'),
             bg='red', fg='white').pack(fill='x', expand='no')
btn2 = Button(root, text='Close', font=('railways', 10, 'bold'), bg='yellow', fg='black', command=root.destroy).pack(
    fill='x', expand='no')
compText = StringVar()
userText = StringVar()
userText.set('Your Virtual Assistant')
userFrame = LabelFrame(root, text='Lena', font=('Railways', 24,
                                                'bold'))
userFrame.pack(fill='both', expand='yes')
top = Message(userFrame, textvariable=userText, bg='black',
              fg='white')
top.config(font=("Century Gothic", 15, 'bold'))
top.pack(side='top', fill='both', expand='yes')

#
root.mainloop()
# root = Tk()

# root.title('alexa')
# root.geometry('520x320')



# images_list = []
# gif_duration = ''


# def extract_images_from_gif(path=None):
#     global gif_duration
#     image = Image.open(path)
#     for i in count(1):
#         try:
#             images_list.append(ImageTk.PhotoImage(image.copy()))
#             image.seek(1)
#         except Exception as error:
#             print(error)
#             break
#     gif_duration = int(image.info['duration'])
#
#
# def play_slider(slider_lb):
#     global images_counting
#     try:
#         images_counting += 1

#         slider_lb.config(image=images_list[images_counting])
#
#         root.after(gif_duration, play_slider)
#
#     except Exception as error:
#         print(error)
#         images_counting = -1
#         root.after(gif_duration, play_slider)
#
#
# extract_images_from_gif('D:\My projects\AI assistant\Siri_1.gif')
# root.after(1000, play_slider)
# root.mainloop()

# reat.naintoon


# def play_gif():
#     global img
# img = Image.open("D:\My projects\AI assistant\Siri_1.gif" )
# lbl = Label(root)
# lbl.place(x=0, y=0)
#
#     # for img in ImageSequence.Iterator(img):
# img = img.resize((400, 350))
# img = ImageTk.PhotoImage(img)
# lbl.config(image=img)
# root.update()
# root.after(0, play_gif)


# def exit():
#     root.distroy()
#
#

# img = tkinter.PhotoImage(Image.open('Siri_1.gif'))
# panel = Label(root, image=img)
# my_image = PhotoImage(file='FIle Location\\Filename.gif')
# canvas.create_image(0, 0, anchor = NW, img)
# canvas.pack(side='right', fill='both', expand='no')
