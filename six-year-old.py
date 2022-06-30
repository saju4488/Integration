from tkinter import *
import random


def rand_choice():
    r_img = random.choice(img_list)
    Canvas.itemconfig(canvas_img, image=r_img)

window = Tk()
window.title("육효")


Canvas = Canvas(window, height=655, width=680, bg="ivory")
Canvas.pack()

img_main = PhotoImage(file="jini.png")
canvas_img = Canvas.create_image(340, 340, image=img_main)
Canvas.create_text(340, 30, text="소원을 말해봐", fill="brown",
                   font=("나눔바른펜", 30, "bold"))

img_list = []
for i in range(55):
    img = PhotoImage(file=f"images/img{i}.png")
    img_list.append(img)

button = Button(window, text="Click", bg="white", fg="hot pink",
                font=("나눔바른펜", 20, "bold"),
                command=rand_choice)
button.place(x=610, y=0)


window.mainloop()