from tkinter import Tk, Entry, Radiobutton, Button, Label, IntVar, Spinbox, Checkbutton
import random
import string
import pyperclip

r = Tk()
r.title("Password Generator")
r.geometry("450x450")
r.minsize(450, 450)
r.maxsize(450, 450)
r.configure(bg="gray17")
choice = IntVar()

def pass_generator():
    """
        Generate a random password based on the selected criteria.

        Parameters:
        None, but assumes the following global variables are defined:
        - length: Desired length of the password.
        - choice: Choice of character set (1 for lowercase letters, 2 for digits, 3 for all characters).
        - e1: Entry widget to display the generated password.

        Returns:
        None. The generated password is inserted into the entry widget e1.
        """
    s = []
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    password_length = int(length.get())
    if choice.get() == 1:
        random_password = ''.join(random.sample(s2, password_length))
    elif choice.get() == 2:
        random_password = ''.join(random.sample(s3, password_length))
    elif choice.get() == 3:
        random_password = ''.join(random.sample(s, password_length))
    e1.delete(0, 'end')  # Clear previous content
    e1.insert(0, random_password)

def copy():
    """
        Copy the generated random password from the entry widget e1 to the clipboard.

        Assumes that e1 is a global variable representing an entry widget containing the generated password.
        """
    random_password = e1.get()
    pyperclip.copy(random_password)

def checkbutton_action():
    """
        Action to be performed when the check button is clicked or toggled.
        """
    pass_generator()

l1 = Label(r, text="Welcome to Password Generator!!!", bg="wheat1", font="ariel 12 bold")
l1.place(y=15, x=90)
r1 = Radiobutton(r, text="Weak", font="ariel 12 bold", padx=15, bg="wheat1", variable=choice, value=1)
r1.place(x=10, y=90)
r2 = Radiobutton(r, text="Medium", font="ariel 12 bold", padx=15, bg="wheat1", variable=choice, value=2)
r2.place(x=160, y=90)
r3 = Radiobutton(r, text="Strong", font="ariel 12 bold", padx=15, bg="wheat1", variable=choice, value=3)
r3.place(x=320, y=90)
l2 = Label(r, text="Generated Password", font="ariel 12 bold", bg="wheat1")
l2.place(x=135, y=230)
l3 = Label(r, text="Choose length of Password", font="ariel 12 bold", bg="wheat1")
l3.place(x=115, y=140)
e1 = Entry(font="ariel 15 bold", borderwidth=5, relief="sunken")
e1.place(x=105, y=270)
b1 = Button(r, text="Generate Again", font="ariel 12 italic", bg="wheat1", command=pass_generator)
b1.place(x=150, y=330)
b2 = Button(r, text="Copy Password", font="ariel 12 italic", bg="wheat1", command=copy)
b2.place(x=150, y=380)
length = Spinbox(from_=5, to=100, font="ariel 12 bold")
length.place(x=125, y=190)
l3 = Label(r, text="Choose Password Type", font="ariel 12 bold", bg="wheat1")
l3.place(x=125, y=50)
c1 = Checkbutton(r, bg="wheat1", command=checkbutton_action)
c1.place(x=330, y=190)

r.mainloop()
