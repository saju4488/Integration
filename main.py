from unittest import result
from turtle import title, width
from tkinter import messagebox
from tkinter import *
reading_file = open('idioms04.txt', 'r')


def data_open():
    with open("idioms04.txt", "r") as file:
        data = file.read()
    result_label.config(text=data)


def data_save():
    idiom = idiom_entry.get()
    meaning = meaning_entry.get()

    if len(idiom) == 0 or len(meaning) == 0:
        messagebox.showinfo(title="저장실패", message="자미두수 용어와 뜻을 모두 입력하세요")
    else:
        with open("idioms04.txt", "a") as file:
            file.write(f"{idiom} : {meaning}\n")
        result_label.config(text=f"저장완료\n{idiom} : {meaning}")
        idiom_entry.delete(0, END)
        meaning_entry.delete(0, END)


def data_find():
    word = idiom_entry.get()
    with open("idioms04.txt", "r") as file:
        for data in file:
            if word in data:
                result_label.config(text=data)


window = Tk()

img = PhotoImage(file="bgimg.png")
img_label = Label(window, image=img)
img_label.grid(column=0, row=0, columnspan=3)

title_label = Label(window, text="자미두수", font=("나눔바른펜", 20, "bold"))
title_label.grid(column=0, row=1, columnspan=3, pady=20)

idiom_label = Label(window, text="자미두수 용어", width=10,
                    font=("나눔바른펜", 15))
idiom_label.grid(column=0, row=2)

idiom_entry = Entry(window, width=30)
idiom_entry.grid(column=1, row=2)

meaning_label = Label(window, text="뜻", width=10,
                      font=("나눔바른펜", 15))
meaning_label.grid(column=0, row=3)

meaning_entry = Entry(window, width=30)
meaning_entry.grid(column=1, row=3)

Button_open = Button(window, text="불러오기", width=10, font=("나눔바른펜, 12"),
                     bg="pink", command=data_open)

Button_open.grid(column=0, row=4, pady=20)

Button_save = Button(window, text="저장하기", width=10, font=("나눔바른펜, 12"),
                     bg="pink", command=data_save)

Button_save.grid(column=1, row=4, pady=20)

Button_find = Button(window, text="검색하기", width=10, font=("나눔바른펜, 12"),
                     bg="pink", command=data_find)

Button_find.grid(column=2, row=4, pady=20)

result_label = Label(window, wraplength=300)
result_label.grid(column=0, row=5, columnspan=3)


window.mainloop()
