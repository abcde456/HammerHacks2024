import customtkinter as ct

def signIn():
    pass

app = ct.CTk()
app.geometry("300x400")
app.title("Schoolmaster")

# Adding elements
h1Font = ct.CTkFont('Tahoma', 50)
h2Font = ct.CTkFont('Tahoma', 20)
h3Font = ct.CTkFont('Tahoma', 10)

title = ct.CTkLabel(app, text="Sign In", font=h2Font)
title.pack(padx=10, pady=10)

usernameInputVar = ct.StringVar()
passwordInputVar = ct.StringVar()

userTitle = ct.CTkLabel(app, text="Email:", font=h3Font)
userTitle.pack(pady=5)

usernameInput = ct.CTkEntry(app, width=260, height=30, textvariable=usernameInputVar)
usernameInput.pack(pady=10)

passTitle = ct.CTkLabel(app, text="Password:", font=h3Font)
passTitle.pack(pady=10)
passwordInput = ct.CTkEntry(app, width=260, height=30, textvariable=passwordInputVar)
passwordInput.pack(pady=5)

status = ct.CTkLabel(app, text="", font=h2Font)
status.pack(side="bottom", pady=10)

signButton = ct.CTkButton(app, text="Sign In", font=h2Font, command=signIn)
signButton.pack(pady=20)

# Run app
app.mainloop()