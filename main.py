from globals import *
from loggedIn import *

window.title("Login form")
window.geometry('350x440')
window.configure(bg='#333333')
frame = tk.Frame(bg='#333333')


def login():
    keepGoing = 0
    loggedIn = False
    username = usernameEntry.get()
    hashUsername = hashlib.md5(username.encode())

    password = passwordEntry.get()
    hashPassword = hashlib.md5(password.encode())

    data = pd.read_csv("database.csv")
    data = data.set_index(['username'])

    try:
        user = data.loc[hashUsername.hexdigest()]
        pw = user.password
        if hashPassword.hexdigest() == pw:
            loggedIn = True

        else:
            print("Incorrect Password. Try again or create a new account.")

    except:
        print("An account with that username does not exist. Please try again or create an account")

    if loggedIn == True:
        windowTwo()
        for widget in frame.winfo_children():
            widget.destroy()
        Label(frame, pady=60, bg="#333333").pack()
        Label(frame, text="Successfully \nlogged in!", font=("Arial", 40), bg="#333333", fg="#FFFFFF").pack()


# Creating the widgets main screen
loginLabel = tk.Label(frame, text="Login", bg="#333333", fg="#FFFFFF", font=("Arial", 30))
usernameLabel = tk.Label(frame, text="Username", bg="#333333", fg="#FFFFFF", font=("Arial", 16))
usernameEntry = tk.Entry(frame, font=("Arial", 14))
passwordEntry = tk.Entry(frame, show="*", font=("Arial", 14))
passwordLabel = tk.Label(frame, text="Password", bg="#333333", fg="#FFFFFF", font=("Arial", 16))
loginButton = tk.Button(frame, text="Login", bg="#FFFFFF", fg="#333333", font=("Arial", 16), command=login)

# Placing the widgets on the screen
loginLabel.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
usernameLabel.grid(row=1, column=0, padx=5)
usernameEntry.grid(row=1, column=1, pady=20)
passwordLabel.grid(row=2, column=0, padx=5)
passwordEntry.grid(row=2, column=1, pady=20)
loginButton.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()
window.mainloop()
