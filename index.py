import tkinter as tk

window = tk.Tk()
window.title("Login form")
window.geometry('340x440')
window.configure(bg = '#333333')

# Creating the widgets
loginLabel = tk.Label(window, text = "Login", bg = "#333333", fg = "#FFFFFF")
usernameLabel = tk.Label(window, text = "Username", bg = "#333333", fg = "#FFFFFF")
usernameEntry = tk.Entry(window)
passwordEntry = tk.Entry(window, show = "*")
passwordLabel = tk.Label(window, text = "Password", bg = "#333333", fg = "#FFFFFF")
loginButton = tk.Button(window, text = "Login")


# Placing the widgets on the screen
loginLabel.grid(row = 0, column = 0, columnspan = 2)
usernameLabel.grid(row = 1, column = 0)
usernameEntry.grid(row = 1, column = 1)
passwordLabel.grid(row = 2, column = 0)
passwordEntry.grid(row = 2, column = 1)
loginButton.grid(row = 3, column = 0, columnspan = 2)


#label.pack()
#pack,place,grid


window.mainloop()








