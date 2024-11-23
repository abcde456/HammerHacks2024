import customtkinter as ct
from tkinter import *
from PIL import Image

semester = "1"

def open(sub):
    pass

def ecTab():
    pass

def tutorTab():
    pass

app = ct.CTk()
app.geometry("854x480")
app.title("Schoolmaster")

# Adding elements
h1Font = ct.CTkFont('Tahoma', 50)
h2Font = ct.CTkFont('Tahoma', 20)
h3Font = ct.CTkFont('Tahoma', 10)

sideFrame = ct.CTkFrame(app, fg_color="#0b172b")
sideFrame.grid(row=0, column=0, rowspan=4)

logoImage = ct.CTkImage(dark_image=Image.open("images/logo.png"), light_image=Image.open("images/logo.png"), size=(204,133))

logo = ct.CTkLabel(sideFrame, text="", image=logoImage)
logo.grid(row=0, column=0)


ecButton = ct.CTkButton(sideFrame, text="Extracurriculars", command=ecTab, fg_color="#0b172b", bg_color="#FFFFFF", height=152)
ecButton.grid(row=1, column=0, sticky=E+W, pady=10)

tutorButton = ct.CTkButton(sideFrame, text="Tutors", command=tutorTab, fg_color="#0b172b", bg_color="#FFFFFF", height=152)
tutorButton.grid(row=2, column=0, sticky=E+W, pady=10)

eButton = ct.CTkButton(sideFrame, text="e", command=tutorTab, fg_color="#0b172b", bg_color="#FFFFFF", height=152)
eButton.grid(row=4, column=0, sticky=E+W, pady=10)


title = ct.CTkLabel(app, text="Subjects", font=h1Font, width=1076)
title.grid(row=0, column=1, columnspan=4, sticky=E)



semTitle = ct.CTkLabel(app, text="Semester "+semester+":", font=h2Font)
semTitle.grid(row=1, column=1, pady=20)

sub1Button = ct.CTkButton(app, text="Math", font=h2Font, command=open(sub = "math"), width=150, height=150)
sub1Button.grid(row=2, column=1)

sub2Button = ct.CTkButton(app, text="Science", font=h2Font, command=open(sub = "english"), width=150, height=150)
sub2Button.grid(row=2, column=2)

sub3Button = ct.CTkButton(app, text="French", font=h2Font, command=open(sub = "french"), width=150, height=150)
sub3Button.grid(row=2, column=3)

sub4Button = ct.CTkButton(app, text="Tech", font=h2Font, command=open(sub = "tech"), width=150, height=150)
sub4Button.grid(row=2, column=4)

sub5Button = ct.CTkButton(app, text="Math", font=h2Font, command=open(sub = "math"), width=150, height=150)
sub5Button.grid(row=4, column=1)

sub6Button = ct.CTkButton(app, text="Science", font=h2Font, command=open(sub = "english"), width=150, height=150)
sub6Button.grid(row=4, column=2)

sub7Button = ct.CTkButton(app, text="French", font=h2Font, command=open(sub = "french"), width=150, height=150)
sub7Button.grid(row=4, column=3)

sub8Button = ct.CTkButton(app, text="Tech", font=h2Font, command=open(sub = "tech"), width=150, height=150)
sub8Button.grid(row=4, column=4)

# Run app
app.mainloop()
