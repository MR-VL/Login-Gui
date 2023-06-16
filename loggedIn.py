from globals import *
def windowTwo():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(window)

    # sets the title of the
    # Toplevel widget
    newWindow.title("Main Application")

    # sets the geometry of toplevel
    newWindow.geometry("600x600")

    # A Label widget to show in toplevel
    Label(newWindow, text="This is a new window").pack()