from tkinter import *

root = Tk()
root.title("Pawn Promotion")

var = StringVar(root)
var.set("Select a  piece.")


def grab_and_assign(event):
    chosen_option = var.get()
    label_chosen_variable = Label(root, text=chosen_option)
    label_chosen_variable.grid(row=1, column=2)
    return chosen_option


drop_menu = OptionMenu(root, var, "Queen", "Rook", "Bishop", "Knight", command=grab_and_assign)
drop_menu.grid(row=0, column=0)

label_left = Label(root, text="Your pawn will be promoted to a: ")
label_left.grid(row=1, column=0)

root.mainloop()
