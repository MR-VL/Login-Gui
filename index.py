import tkinter as tk
import hashlib 
window = tk.Tk()
window.title("Login form")
window.geometry('340x440')
window.configure(bg = '#333333')

frame = tk.Frame(bg = '#333333')

def login():
    username = usernameEntry.get()
    hashUsername = hashlib.md5(username.encode())
    
    password = passwordEntry.get()
    hashPassword = hashlib.md5(password.encode())
    
    stoUsername = "21232f297a57a5a743894a0e4a801fc3"
    stoPassword = "5f4dcc3b5aa765d61d8327deb882cf99"

    
    
    if hashUsername.hexdigest() == stoUsername and hashPassword.hexdigest() == stoPassword :
        print("Success")
    else:
        print("ERROR INVALID CREDENTIALS")


# Creating the widgets
loginLabel = tk.Label(frame, text = "Login", bg = "#333333", fg = "#FFFFFF", font = ("Arial", 30))
usernameLabel = tk.Label(frame, text = "Username", bg = "#333333", fg = "#FFFFFF", font = ("Arial", 16))
usernameEntry = tk.Entry(frame, font = ("Arial", 14))
passwordEntry = tk.Entry(frame, show = "*", font = ("Arial", 14))
passwordLabel = tk.Label(frame, text = "Password", bg = "#333333", fg = "#FFFFFF", font = ("Arial", 16))
loginButton = tk.Button(frame, text = "Login", bg = "#FFFFFF", fg = "#333333", font = ("Arial", 16), command = login)


# Placing the widgets on the screen
loginLabel.grid(row = 0, column = 0, columnspan = 2, sticky = "news", pady = 40)
usernameLabel.grid(row = 1, column = 0, padx = 5)
usernameEntry.grid(row = 1, column = 1, pady = 20)
passwordLabel.grid(row = 2, column = 0, padx = 5)
passwordEntry.grid(row = 2, column = 1, pady = 20)
loginButton.grid(row = 3, column = 0, columnspan = 2, pady = 30)

frame.pack()



window.mainloop()






#label.pack()
#pack,place,grid


