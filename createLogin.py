from globals import *


def writeAccount(secondWindow, userEnter, pw1, pw2):
    data = pd.read_csv("database.csv")
    data = data.set_index(['username'])
    userEntry = hashlib.md5(userEnter.encode()).hexdigest()

    try:
        user = data.loc[userEntry]
        messagebox.showerror("ERROR: Account already exists",
                             "ERROR: Account already exists.\nPlease choose a different username or "
                             "sign in using your current credentials."
                             "\n\nIF you have forgotten your password contact your systems administrator")

    except:
        if pw1 == pw2:
            username = userEntry
            password = hashlib.md5(pw1.encode()).hexdigest()

            newUser = {
                'username': [username],
                'password': [password]
            }
            df = pd.DataFrame(newUser)
            df.to_csv('database.csv', mode='a', index=False, header=False)
            secondWindow.destroy()
            messagebox.showinfo("Account Successfully Created", "Your account has been successfully created! "
                                                                "\nLog in with you new credentials")
        else:
            messagebox.showerror("ERROR: Passwords do not match",
                                 "ERROR: Passwords do not match, re-enter your desired password")


def createAccount():
    secondary_window = tk.Toplevel()
    secondary_window.focus()
    secondary_window.resizable(False, False)
    secondary_window.grab_set()

    secondary_window.title("Secondary Window")
    secondary_window.geometry('350x440')
    secondary_window.configure(bg='#333333')

    loginLabel = tk.Label(secondary_window, text="Create New\nAccount", bg="#333333", fg="#FFFFFF", font=("Arial", 30))
    usernameLabel = tk.Label(secondary_window, text="Username", bg="#333333", fg="#FFFFFF", font=("Arial", 16))
    userEntry = tk.Entry(secondary_window, font=("Arial", 14))
    passwordEntry = tk.Entry(secondary_window, show="*", font=("Arial", 14))

    passwordLabel = tk.Label(secondary_window, text="Password", bg="#333333", fg="#FFFFFF", font=("Arial", 16))
    passwordLabelTwo = tk.Label(secondary_window, text="Re-enter\nPassword", bg="#333333", fg="#FFFFFF",
                                font=("Arial", 16))
    passwordEntryTwo = tk.Entry(secondary_window, show="*", font=("Arial", 14))
    createAccountButton = tk.Button(secondary_window, text="Create Account", bg="#FFFFFF", fg="#333333",
                                    font=("Arial", 10), activebackground='#5D3FD3', activeforeground="#FFFFFF",
                                    command=lambda: writeAccount(secondary_window, userEntry.get(), passwordEntry.get(),
                                                                 passwordEntryTwo.get()))

    loginLabel.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    usernameLabel.grid(row=1, column=0, padx=5)
    userEntry.grid(row=1, column=1, pady=20)
    passwordLabel.grid(row=2, column=0, padx=5)
    passwordLabelTwo.grid(row=3, column=0, padx=5)
    passwordEntry.grid(row=2, column=1, pady=20)
    passwordEntryTwo.grid(row=3, column=1, pady=20)
    createAccountButton.grid(row=4, column=0, columnspan=2, pady=10)
