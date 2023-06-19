from createLogin import createAccount
from globals import *
from logon import windowTwo


def login(frame, username, password):
    hashUsername = hashlib.md5(username.encode())
    hashPassword = hashlib.md5(password.encode())

    data = pd.read_csv("database.csv")
    data = data.set_index(['username'])

    try:
        user = data.loc[hashUsername.hexdigest()]
        pw = user.password
        if hashPassword.hexdigest() == pw:
            windowTwo()
            for widget in frame.winfo_children():
                widget.destroy()
            Label(frame, pady=60, bg="#333333").pack()
            Label(frame, text="Successfully \nlogged in!", font=("Arial", 40), bg="#333333", fg="#FFFFFF").pack()

        else:
            messagebox.showerror("Incorrect Password", "The password for the account you entered is Incorrect. "
                                                       "\nPlease try again or create a new password.")

    except:
        messagebox.showerror("No Account Found", "The username and password entered does not correspond to an existing "
                                                 "account.\n\nPlease try again or create a new account")


def createPage():
    window = tk.Tk()
    window.title("Login form")
    window.geometry('350x440')
    window.configure(bg='#333333')
    window.resizable(False, False)
    frame = tk.Frame(bg='#333333')

    # Creating the widgets main screen
    loginLabel = tk.Label(frame, text="Login", bg="#333333", fg="#FFFFFF", font=("Arial", 30))
    usernameLabel = tk.Label(frame, text="Username", bg="#333333", fg="#FFFFFF", font=("Arial", 16))
    usernameEntry = tk.Entry(frame, font=("Arial", 14))
    passwordEntry = tk.Entry(frame, show="*", font=("Arial", 14))
    passwordLabel = tk.Label(frame, text="Password", bg="#333333", fg="#FFFFFF", font=("Arial", 16))
    loginButton = tk.Button(frame, text="Login", bg="#FFFFFF", fg="#333333", font=("Arial", 16),
                            command=lambda: login(frame, usernameEntry.get(), passwordEntry.get()),
                            activebackground='#5D3FD3', activeforeground="#FFFFFF")

    createAccountButton = tk.Button(frame, text="Create Account", bg="#333333", fg="#FFFFFF", font=("Arial", 10),
                                    command=createAccount, activebackground='#5D3FD3', activeforeground="#FFFFFF")

    # Placing the widgets on the screen
    loginLabel.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    usernameLabel.grid(row=1, column=0, padx=5)
    usernameEntry.grid(row=1, column=1, pady=20)
    passwordLabel.grid(row=2, column=0, padx=5)
    passwordEntry.grid(row=2, column=1, pady=20)
    loginButton.grid(row=3, column=0, columnspan=2, pady=30)
    createAccountButton.grid(row=4, column=0, columnspan=2, pady=10)
    frame.pack()
    window.mainloop()


createPage()
