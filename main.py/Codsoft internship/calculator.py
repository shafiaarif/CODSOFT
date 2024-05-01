from tkinter import Tk,Button,Label
r=Tk()
r.title("Calculator")
r.geometry("280x300+100+200")
r.maxsize(280,300)
r.minsize(280,300)
r.configure(bg="black")

equation=""

def show(value):
    """
        Update the equation string and display it on the calculator's label.

        Parameters:
            value (str): The value to append to the equation string.

        Returns:
            None

        Globals:
            equation (str): The global variable representing the current equation string.
            l1 (Label): The label widget used to display the equation on the calculator's GUI.

        """
    global equation
    equation+=value
    l1.config(text=equation)

def clear():
    """
        Clear the current equation and update the calculator's display.

        Parameters:
            None

        Returns:
            None

        Globals:
            equation (str): The global variable representing the current equation string.
            l1 (Label): The label widget used to display the equation on the calculator's GUI.

        """
    global equation
    equation=""
    l1.config(text="")

def calculate():
    """
       Evaluate the current equation and display the result on the calculator's label.

       Parameters:
           None

       Returns:
           None

       Globals:
           equation (str): The global variable representing the current equation string.
           l1 (Label): The label widget used to display the equation and result on the calculator's GUI.

       """
    global equation
    result=""
    if equation!="":
        try:
            result=eval(equation)
            l1.config(text=result)
        except:
            result="Error"
            l1.config(text=result)
            equation=""

l1=Label(r,text="",width=50,height=2,font="ariel 17 bold",relief="sunken",borderwidth=8)
l1.pack()
b1=Button(r,text="C",bg="cyan2",font="ariel 13 bold",height=1,width=5,command=clear)
b1.place(x=8,y=75)
b2=Button(r,text="/",bg="dark gray",font="ariel 13 bold",height=1,width=5,command=lambda :show("/"))
b2.place(x=75,y=75)
b3=Button(r,text="%",bg="dark gray",font="ariel 13 bold",height=1,width=5,command=lambda :show("%"))
b3.place(x=145,y=75)
b4=Button(r,text="*",bg="dark gray",font="ariel 13 bold",height=1,width=5,command=lambda :show("*"))
b4.place(x=215,y=75)
b5=Button(r,text="7",bg="dark gray",font="ariel 13 bold",height=1,width=5,command=lambda :show("7"))
b5.place(x=8,y=120)
b6=Button(r,text="8",bg="dark gray",font="ariel 13 bold",height=1,width=5,command=lambda :show("8"))
b6.place(x=75,y=120)
b7=Button(r,text="9",bg="dark gray",font="ariel 13 bold",height=1,width=5,command=lambda :show("9"))
b7.place(x=145,y=120)
b8=Button(r,text="-",bg="dark gray",font="ariel 13 bold",height=1,width=5,command=lambda :show("-"))
b8.place(x=215,y=120)
b9=Button(r,text="4",bg="dark gray",font="ariel 13 bold",height=1,width=5,command=lambda :show("4"))
b9.place(x=8,y=165)
b10=Button(r,text="5",bg="dark gray",font="ariel 13 bold",height=1,width=5,command=lambda :show("5"))
b10.place(x=75,y=165)
b11=Button(r,text="6",bg="dark gray",font="ariel 13 bold",height=1,width=5,command=lambda :show("6"))
b11.place(x=145,y=165)
b12=Button(r,text="+",bg="dark gray",font="ariel 13 bold",height=1,width=5,command=lambda :show("+"))
b12.place(x=215,y=165)
b13=Button(r,text="1",bg="dark gray",font="ariel 13 bold",height=1,width=5,command=lambda :show("1"))
b13.place(x=8,y=210)
b14=Button(r,text="2",bg="dark gray",font="ariel 13 bold",height=1,width=5,command=lambda :show("2"))
b14.place(x=75,y=210)
b15=Button(r,text="3",bg="dark gray",font="ariel 13 bold",height=1,width=5,command=lambda :show("3"))
b15.place(x=145,y=210)
b16=Button(r,text="0",bg="dark gray",font="ariel 13 bold",height=1,width=12,command=lambda :show("0"))
b16.place(x=8,y=255)
b17=Button(r,text=".",bg="dark gray",font="ariel 13 bold",height=1,width=5,command=lambda :show("."))
b17.place(x=145,y=255)
b18=Button(r,text="=",bg="dark orange",font="ariel 13 bold",height=3,width=5,command=calculate)
b18.place(x=215,y=210)

r.mainloop()