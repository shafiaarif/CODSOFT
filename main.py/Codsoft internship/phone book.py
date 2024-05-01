import sys
from tkinter import Tk, Button, Entry, Label, Frame,messagebox,Listbox

r = Tk()
r.geometry("700x700")
r.minsize(700, 600)
r.maxsize(700, 600)
r.title("Phone Book")

def exit():
    """Exit the program."""
    sys.exit()

def listbox_info(L):
    """
       Populate the given Listbox (L) with names from the phone book file.

       Args:
           L (Listbox): The Listbox widget to populate with names.

       Reads each line from the "phone_book.txt" file, splits it by comma,
       and inserts the first element (name) into the Listbox.
       """
    with open("phone_book.txt","r") as file:
         for line in file:
             a = line.strip().split(",")
             L.insert("end", a[0])
def update(L, update_contact_e1, update_contact_e2, update_contact_e3, update_contact_e4):
    """
        Update the details of a contact in the phone book file based on user input.

        Args:
            L (Listbox): The Listbox widget containing the names of contacts.
            update_contact_e1 (Entry): Entry widget for updating the name.
            update_contact_e2 (Entry): Entry widget for updating the phone number.
            update_contact_e3 (Entry): Entry widget for updating the address.
            update_contact_e4 (Entry): Entry widget for updating the email.

        Checks if any item is selected in the listbox (L). If no item is selected,
        it displays a warning message. Otherwise, it retrieves the selected name,
        updates the contact details with the information provided in the Entry widgets,
        and writes the updated details back to the phone book file.

        """
    # Check if any item is selected in the listbox
    selected_index = L.curselection()
    if not selected_index:
        messagebox.showinfo("Warning", "Select Name")
    else:
        name = L.get(selected_index[0]).strip().lower()
        updated_details = [update_contact_e1.get(), update_contact_e2.get(), update_contact_e3.get(), update_contact_e4.get()]

        # Open the phone book file
        with open("phone_book.txt", "r") as file:
            lines = file.readlines()

        # Update the contact details
        with open("phone_book.txt", "w") as file:
            for line in lines:
                contact_name, _, _, _ = line.strip().split(",")
                if name == contact_name.lower():
                    file.write(','.join(updated_details) + '\n')
                else:
                    file.write(line)

        messagebox.showinfo("Message", "Contact Updated")
        update_contact_e1.delete(0,"end")
        update_contact_e2.delete(0, 'end')
        update_contact_e3.delete(0, 'end')
        update_contact_e4.delete(0, 'end')


def search_contact(L, search_contact_l2, search_contact_l3, search_contact_l4, search_contact_l5):
    """
       Search for a contact in the phone book file based on the selected name from the Listbox.

       Args:
           L (Listbox): The Listbox widget containing the names of contacts.
           search_contact_l2 (Label): Label widget for displaying the name of the contact.
           search_contact_l3 (Label): Label widget for displaying the phone number of the contact.
           search_contact_l4 (Label): Label widget for displaying the address of the contact.
           search_contact_l5 (Label): Label widget for displaying the email of the contact.

       Checks if any item is selected in the listbox (L). If no item is selected,
       it displays a warning message. Otherwise, it retrieves the selected name,
       searches for the contact details in the phone book file, and displays
       the details in the corresponding Label widgets.

       """
    # Check if any item is selected in the listbox
    selected_index = L.curselection()
    if not selected_index:  # If nothing is selected
        # Handle the case when no item is selected
        messagebox.showinfo("Warning","Select Name")
    else:
        name = L.get(selected_index[0]).strip().lower()

    # Open the phone book file
        with open("phone_book.txt", "r") as p:
            for line in p:
               a = line.strip().split(",")
               contact_name = a[0].strip().lower()
               if name == contact_name:
                   search_contact_l2.configure(text=f"Name: {a[0]}")
                   search_contact_l3.configure(text=f"Phone Number: {a[1]}")
                   search_contact_l4.configure(text=f"Address: {a[2]}")
                   search_contact_l5.configure(text=f"E-mail: {a[3]}")
                   break
def save_contact(e1, e2, e3, e4):
    """
        Save contact details to the phone book file.

        Args:
            e1 (Entry): Entry widget containing the name of the contact.
            e2 (Entry): Entry widget containing the phone number of the contact.
            e3 (Entry): Entry widget containing the address of the contact.
            e4 (Entry): Entry widget containing the email of the contact.

        Retrieves the details of the contact from the Entry widgets. If any of the details
        are empty, it displays a warning message. Otherwise, it saves the contact details
        to the phone book file, clears the Entry widgets, and displays a confirmation message.

        """

    details = [e1.get(), e2.get(), e3.get(), e4.get()]
    if details == ["", "", "", ""]:
        messagebox.showinfo("Warning", "Details are empty")
    else:
        with open("phone_book.txt", "a+") as f:
            f.write(','.join(details) + '\n')
        messagebox.showinfo("Message", "Contact Saved")
        e1.delete(0, "end")
        e2.delete(0, "end")
        e3.delete(0, "end")
        e4.delete(0, "end")


def delete(L,delete_contact_l1,delete_contact_l2,delete_contact_l3,delete_contact_l4,delete_contact_l5,):
    """
        Delete a contact from the phone book.

        Args:
            L (Listbox): Listbox widget containing the list of contacts.
            delete_contact_l1 (Label): Label widget displaying "Select Name:-".
            delete_contact_l2 (Label): Label widget displaying the name of the selected contact.
            delete_contact_l3 (Label): Label widget displaying the phone number of the selected contact.
            delete_contact_l4 (Label): Label widget displaying the address of the selected contact.
            delete_contact_l5 (Label): Label widget displaying the email of the selected contact.

        Retrieves the index of the selected contact in the Listbox. If no contact is selected,
        it displays a warning message. Otherwise, it deletes the selected contact from the Listbox
        and removes it from the phone book file. Additionally, it clears the details displayed in
        the Label widgets and shows a confirmation message.

        """
    delete = L.curselection()
    if not delete:  # If nothing is selected
        # Handle the case when no item is selected
        messagebox.showinfo("Warning","Select Name")
    else:
        look = L.get(delete)
        for index in reversed(delete):
           L.delete(index)
    # Remove the selected item from the file
        with open("phone_book.txt", "r") as f:
            lines = f.readlines()
        with open("phone_book.txt", "w") as f:
            for line in lines:
                if str(look) not in line:
                   f.write(line)
        messagebox.showinfo("Message","Contact Deleted")
        delete_contact_l2.configure(text="")
        delete_contact_l3.configure(text="")
        delete_contact_l4.configure(text="")
        delete_contact_l5.configure(text="")

def add_contact_page():
    """
       Display the page for adding a new contact.

       Clears any existing pages and creates a new frame for adding a contact.
       It contains entry fields for name, phone number, address, and email, along with
       labels for each field. Also, it includes a button to save the contact.
       """
    delete_pages()
    add_contact_frame = Frame(main_frame,height=600,width=550,bg="sea green1")
    l1 = Label(add_contact_frame, text="Enter Details", font="ariel 20 bold",bg="sea green1")
    l1.place(x=200, y=70)
    l2 = Label(add_contact_frame,text="Name:",font="ariel 15 bold",bg="sea green1")
    l2.place(x=80,y=130)
    l3 = Label(add_contact_frame, text="Phone Number:", font="ariel 15 bold",bg="sea green1")
    l3.place(x=80, y=180)
    l4 = Label(add_contact_frame, text="Address:", font="ariel 15 bold",bg="sea green1")
    l4.place(x=80, y=230)
    l5 = Label(add_contact_frame, text="E-mail:", font="ariel 15 bold",bg="sea green1")
    l5.place(x=80, y=280)
    e1=Entry(add_contact_frame,font="ariel 13 bold",bg="khaki1",borderwidth=3,relief="sunken")
    e1.place(x=150,y=135)
    e2 = Entry(add_contact_frame, font="ariel 13 bold",bg="khaki1",borderwidth=3,relief="sunken")
    e2.place(x=235, y=185)
    e3 = Entry(add_contact_frame, font="ariel 13 bold",bg="khaki1",borderwidth=3,relief="sunken")
    e3.place(x=170, y=235)
    e4 = Entry(add_contact_frame, font="ariel 13 bold",bg="khaki1",borderwidth=3,relief="sunken")
    e4.place(x=150, y=285)
    add_contact_button = Button(add_contact_frame, text="Save Contact", height=2, command=lambda: save_contact(e1, e2, e3, e4), bg="khaki2")
    add_contact_button.place(x=300,y=350)
    add_contact_frame.pack()
    add_contact_indicator.place(x=3, y=20, width=5, height=33)

def update_contact_page():
    """
      Display the page for updating a contact.

      Clears any existing pages and creates a new frame for updating a contact.
      It includes a listbox to select a contact to update, labels to display the old contact details,
      entry fields for entering the new contact details, and buttons to update the contact.
      """
    delete_pages()
    # Create the update contact frame
    update_contact_frame = Frame(main_frame, height=600, width=550,bg="cyan2")
    update_contact_l1 = Label(update_contact_frame, text="Select Name:-", font="ariel 15 bold",bg="cyan2")
    update_contact_l1.place(x=10, y=4)
    L=Listbox(update_contact_frame,height=30,width=20,borderwidth=4,relief="sunken",font="ariel 12 bold",bg="burlywood1")
    L.place(x=0,y=30)
    listbox_info(L)
    update_contact_l2 = Label(update_contact_frame, text="", font="ariel 15 bold",bg="cyan2")
    update_contact_l2.place(x=200, y=440)
    update_contact_l3 = Label(update_contact_frame, text="", font="ariel 15 bold",bg="cyan2")
    update_contact_l3.place(x=200, y=470)
    update_contact_l4 = Label(update_contact_frame, text="", font="ariel 15 bold",bg="cyan2")
    update_contact_l4.place(x=200, y=500)
    update_contact_l5 = Label(update_contact_frame, text="", font="ariel 15 bold",bg="cyan2")
    update_contact_l5.place(x=200, y=530)
    update_contact_l6= Label(update_contact_frame, text="Old Info:-", font="ariel 15 bold",bg="cyan2")
    update_contact_l6.place(x=200, y=400)
    update_contact_b1 = Button(update_contact_frame, text="update", font="ariel 13 bold",command=lambda: search_contact(L, update_contact_l2, update_contact_l3,update_contact_l4, update_contact_l5),bg="sky blue1")
    update_contact_b1.place(x=200, y=10)
    update_contact_l7 = Label(update_contact_frame, text="Enter Details", font="ariel 20 bold",bg="cyan2")
    update_contact_l7.place(x=200, y=70)
    update_contact_l8 = Label(update_contact_frame, text="Name:", font="ariel 15 bold",bg="cyan2")
    update_contact_l8.place(x=190, y=130)
    update_contact_l9 = Label(update_contact_frame, text="Phone Number:", font="ariel 15 bold",bg="cyan2")
    update_contact_l9.place(x=190, y=180)
    update_contact_l10 = Label(update_contact_frame, text="Address:", font="ariel 15 bold",bg="cyan2")
    update_contact_l10.place(x=190, y=230)
    update_contact_l11 = Label(update_contact_frame, text="E-mail:", font="ariel 15 bold",bg="cyan2")
    update_contact_l11.place(x=190, y=280)
    update_contact_e1 = Entry(update_contact_frame, font="ariel 13 bold",bg="burlywood1",borderwidth=3,relief="sunken")
    update_contact_e1 .place(x=270, y=135)
    update_contact_e2 = Entry(update_contact_frame, font="ariel 13 bold",bg="burlywood1",borderwidth=3,relief="sunken")
    update_contact_e2.place(x=350, y=185)
    update_contact_e3= Entry(update_contact_frame, font="ariel 13 bold",bg="burlywood1",borderwidth=3,relief="sunken")
    update_contact_e3.place(x=280, y=235)
    update_contact_e4 = Entry(update_contact_frame, font="ariel 13 bold",bg="burlywood1",borderwidth=3,relief="sunken")
    update_contact_e4.place(x=280, y=285)
    update_contact_b2=Button(update_contact_frame,text="Update Permanently",command=lambda :update(L,update_contact_e1,update_contact_e2,update_contact_e3,update_contact_e4),bg="sky blue1")
    update_contact_b2.place(x=350,y=330)

    update_contact_frame.pack()
    # Place the update contact indicator
    update_contact_indicator.place(x=3, y=60, width=5, height=33)


def delete_contact_page():
    """
        Display the page for deleting a contact.

        Clears any existing pages and creates a new frame for deleting a contact.
        It includes a listbox to select a contact to delete, buttons for deleting and permanently deleting a contact,
        and labels to display the details of the contact selected for deletion.
        """
    delete_pages()
    delete_contact_frame = Frame(main_frame,height=600,width=550,bg="light pink2")
    delete_contact_l1 = Label(delete_contact_frame, text="Select Name:-",font="ariel 15 bold",bg="light pink2")
    delete_contact_l1.place(x=10,y=4)
    L = Listbox(delete_contact_frame, height=30, width=20, borderwidth=6, relief="sunken", font="ariel 12 bold",bg="lightgoldenrod1")
    L.place(x=0, y=30)
    listbox_info(L)
    delete_contact_b1 = Button(delete_contact_frame,text="Delete", font="ariel 13 bold",command=lambda: search_contact(L, delete_contact_l2, delete_contact_l3,delete_contact_l4, delete_contact_l5),bg="lightgoldenrod1")
    delete_contact_b1.place(x=220, y=500)
    delete_contact_b2 = Button(delete_contact_frame,text="Delete it permanently", font="ariel 13 bold",command=lambda :delete(L,delete_contact_l1,delete_contact_l2,delete_contact_l3,delete_contact_l4,delete_contact_l5),bg="lightgoldenrod1")
    delete_contact_b2.place(x=320, y=400)
    delete_contact_l2 = Label(delete_contact_frame, text="", font="ariel 15 bold",bg="light pink2")
    delete_contact_l2.place(x=200, y=90)
    delete_contact_l3 = Label(delete_contact_frame, text="", font="ariel 15 bold",bg="light pink2")
    delete_contact_l3.place(x=200, y=130)
    delete_contact_l4 = Label(delete_contact_frame, text="", font="ariel 15 bold",bg="light pink2")
    delete_contact_l4.place(x=200, y=170)
    delete_contact_l5 = Label(delete_contact_frame, text="", font="ariel 15 bold",bg="light pink2")
    delete_contact_l5.place(x=200, y=210)
    delete_contact_l6 = Label(delete_contact_frame, text="Contact Details:-", font="ariel 15 bold",bg="light pink2")
    delete_contact_l6.place(x=200, y=40)
    delete_contact_frame.pack()
    delete_contact_indicator.place(x=3, y=100, width=5, height=33)

def search_contact_page():
    """
       Display the page for searching a contact.

       Clears any existing pages and creates a new frame for searching a contact.
       It includes a listbox to select a contact to search for, a button to show details of the selected contact,
       and labels to display the details of the selected contact.
       """
    delete_pages()
    search_contact_frame = Frame(main_frame,height=600,width=550,bg="tan1")

    search_contact_l1 = Label(search_contact_frame, text="Select Name:-",font="ariel 15 bold",bg="tan1")
    search_contact_l1.place(x=10,y=4)
    L=Listbox(search_contact_frame,height=30,width=20,borderwidth=6,relief="sunken",font="ariel 12 bold",bg="khaki1")
    L.place(x=0,y=30)
    listbox_info(L)
    search_contact_l2 = Label(search_contact_frame, text="",font="ariel 15 bold",bg="tan1")
    search_contact_l2.place(x=200,y=90)
    search_contact_l3 = Label(search_contact_frame, text="",font="ariel 15 bold",bg="tan1")
    search_contact_l3.place(x=200,y=130)
    search_contact_l4 = Label(search_contact_frame, text="",font="ariel 15 bold",bg="tan1")
    search_contact_l4.place(x=200,y=170)
    search_contact_l5 = Label(search_contact_frame, text="",font="ariel 15 bold",bg="tan1")
    search_contact_l5.place(x=200,y=210)
    search_contact_l6 = Label(search_contact_frame, text="Contact Details:-",font="ariel 15 bold",bg="tan1")
    search_contact_l6.place(x=200,y=40)
    search_contact_frame.pack()
    search_contact_b1=Button(search_contact_frame,text="Show Details",font="ariel 13 bold",command=lambda :search_contact(L,search_contact_l2,search_contact_l3,search_contact_l4,search_contact_l5),bg="khaki2")
    search_contact_b1.place(x=350,y=500)
    search_contact_indicator.place(x=3, y=140, width=5, height=33)

def delete_pages():
    """
       Deletes all child widgets of the main_frame widget, effectively clearing the interface.
       """
    for frame in main_frame.winfo_children():
        frame.destroy()

def hide_indicators():
    """
       Hides indicators by setting their background color to gray.
       """
    add_contact_indicator.configure(bg="gray")
    update_contact_indicator.configure(bg="gray")
    delete_contact_indicator.configure(bg="gray")
    search_contact_indicator.configure(bg="gray")

def indicators(lb, page):
    """
    Highlights the selected indicator and hides others.

    Args:
        lb: The indicator to be highlighted.
        page: The function to be called for the corresponding page.
    """
    hide_indicators()
    lb.configure(bg="blue")
    page()

f1 = Frame(r, bg="gray")
f1.pack(side="left")
f1.configure(height=600, width=150)

b1 = Button(text="Add New Contact", font="ariel 12 italic", command=lambda: indicators(add_contact_indicator, add_contact_page),bg="goldenrod1")
b1.place(x=10, y=20)
b2 = Button(text="Update Contact", font="ariel 12 italic", width=14, command=lambda: indicators(update_contact_indicator, update_contact_page),bg="goldenrod1")
b2.place(x=10, y=60)
b3 = Button(text="Delete Contact", font="ariel 12 italic", width=14, command=lambda: indicators(delete_contact_indicator, delete_contact_page),bg="goldenrod1")
b3.place(x=10, y=100)
b4 = Button(text="Search Contact", font="ariel 12 italic", width=14, command=lambda: indicators(search_contact_indicator, search_contact_page),bg="goldenrod1")
b4.place(x=10, y=140)
b5 = Button(text="Exit", font="ariel 12 italic", width=14, command=exit,bg="goldenrod1")
b5.place(x=10, y=180)
add_contact_indicator = Label(f1, text="", bg="gray")
add_contact_indicator.place(x=3, y=20, width=5, height=33)
update_contact_indicator = Label(f1, text="", bg="gray")
update_contact_indicator.place(x=3, y=60, width=5, height=33)
delete_contact_indicator = Label(f1, text="", bg="gray")
delete_contact_indicator.place(x=3, y=100, width=5, height=33)
search_contact_indicator = Label(f1, text="", bg="gray")
search_contact_indicator.place(x=3, y=140, width=5, height=33)


main_frame = Frame(r, highlightbackground="black", highlightthickness=5,bg="khaki1")
main_frame.configure(height=700, width=700)
main_frame.pack(side="left")

r.mainloop()
