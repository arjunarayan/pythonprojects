from tkinter import *
from tkinter.font import Font

root = Tk()
root.title("Your DEFINITELY DEFAULT todo list")
root.geometry("500x500")


my_font = Font(
    family="Brush Script MT",
    size=30,
    weight="bold"
)

#create frame
my_frame = Frame(root)
my_frame.pack(pady=10)

#Create ListBox
my_list = Listbox(
    my_frame,
    font=my_font,
    width=25,
    height=5,
    bg="SystemButtonFace",
    bd=0,
    fg="#464646",
    highlightthickness=0,
    selectbackground="#a6a6a6",
    activestyle="none"
)

my_list.pack()

stuff = ["do this", "do that", "do that thingy", "take nap"]
for item in stuff:
    my_list.insert(END, item)

root.mainloop()