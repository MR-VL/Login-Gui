from globals import *


def windowTwo():
    newWindow = tk.Toplevel()
    newWindow.title("Main Application")
    newWindow.geometry("600x600")
    frame3 = tk.Frame()
    Label(frame3, text="This is a new window").pack()

    newWindow.focus()
    newWindow.grab_set()
