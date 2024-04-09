from tkinter import Tk,Button,Label,Listbox,Text,Entry,PhotoImage,messagebox
r=Tk()
r.title("To-Do-List")
r.configure(bg="tan1")
r.geometry("500x500")
r.minsize(500,500)
r.maxsize(500,500)

def add_to_list():
    """
       Adds a task to a list.

       Parameters:
           t1 (tk.Text): The text widget containing the task.
           L (tk.Listbox): The list widget to which the task will be added.
       """
    if t1.get(1.0,"end-1c") == "":
        messagebox.showinfo("Warning","Please Enter a Task to add")
    else:
        text = t1.get(1.0,"end-1c")
        L.insert("end",text)

    # Open the file in append mode and write the text
        with open("list.txt", "a+") as f:
            f.write(text.strip() + "\n")
            f.seek(0)
            t1.delete(1.0,"end-1c")

def delete_from_list():
    """
       Deletes a task from a list.

       Parameters:
           L (tk.Listbox): The list widget from which the task will be deleted.
       """
    delete = L.curselection()
    if not delete:
        messagebox.showinfo("Warning","Select a Task to delete")
    else:
        look = L.get(delete)
    # Remove the selected item from the listbox
        for index in reversed(delete):
            L.delete(index)
    # Remove the selected item from the file
        with open("list.txt", "r") as f:
            lines = f.readlines()
        with open("list.txt", "w") as f:
            for line in lines:
                if str(look) not in line:
                    f.write(line)

def show_list():
    """
        Populates a list widget with tasks stored in a file.

        Parameters:
            L (tk.Listbox): The list widget to populate with tasks.
        """
    # Clear the Listbox before populating it
    L.delete(0, "end")

    # Populate the Listbox with items from the file "list.txt"
    with open("list.txt", "r") as file:
        for line in file:
            L.insert("end", line.strip())


l1=Label(r,text="To-Do-List",borderwidth=10,font="ariel 20 bold",relief="sunken",bg="khaki1")
l1.pack(fill="x")

l2=Label(r,text="Add Tasks",borderwidth=10,font="ariel 20 bold",bg="khaki1",relief="sunken",padx=30)
l2.place(x=20,y=60)

l3=Label(r,text="Your Tasks",borderwidth=10,font="ariel 15 italic",bg="khaki1",relief="sunken",padx=70)
l3.place(x=250,y=60)

L=Listbox(r,height=17,width=23,borderwidth=10,relief="groove",font="ariel 12 italic",bg="khaki1")
L.place(x=260,y=130)

t1=Text(r,height=3,width=18,font="ariel 13 bold",bg="khaki1")
t1.place(x=28,y=120)

b1=Button(r,text="Add to list",height=2,width=15,bg="tan2",command=add_to_list)
b1.place(x=45,y=200)

b2=Button(r,text="Delete from the list",height=2,width=15,bg="tan2",command=delete_from_list)
b2.place(x=45,y=260)

image=PhotoImage(file="nb.PNG")
resized_image = image.subsample(3, 3)
image_label=Label(r,image=resized_image)
image_label.place(x=60,y=330)

show_list()
r.mainloop()
