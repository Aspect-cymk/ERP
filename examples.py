import smtplib
import pickle
import random
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
import os, sys
root = Tk()



# list of email_id to send the mail
li = ["yejeykay@gmail.com"]
          
for dest in li:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("Kaearekae@gmail.com", "fmyi jkof jgog mbqt")
    message = "hello dad"
    s.sendmail("Kaearekae@gmail.com", dest, message)
    s.quit()
