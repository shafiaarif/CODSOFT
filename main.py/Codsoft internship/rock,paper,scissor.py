import sys
from tkinter import Tk, Label, Button, PhotoImage
from random import randint

def final_score():
    """
        Update and display the final score and outcome of the game.

        Retrieves player and computer scores, updates GUI labels with the scores, and determines
        the game outcome. Displays the final scores and outcome message accordingly.
        """
    score1 = int(player_score["text"])
    score2 = int(computer_score["text"])
    final_score1.configure(text=f"Your Score: {score1}")
    final_score2.configure(text=f"Computer Score: {score2}")
    if score1 == score2:
        msg.configure(text="It's a tie!!!")
    elif score1 > score2:
        msg.configure(text="Congratulations! You won!!!")
    elif score1 < score2:
        msg.configure(text="Oops! You lost!!!")

def update_image(x):
    """
       Update the displayed images for the user and computer choices and check the game outcome.

       Parameters:
           x (str): The choice selected by the player ('rock', 'paper', or 'scissor').

       Retrieves a random choice for the computer, updates the displayed images accordingly for
       both the user and computer, and checks the game outcome based on the user and computer choices.

       Args:
           x (str): The choice selected by the player ('rock', 'paper', or 'scissor').
       """
    comp_choice = choice[randint(0, 2)]
    if comp_choice == "rock":
        computer_label.configure(image=rock_image1)
    elif comp_choice == "paper":
        computer_label.configure(image=paper_image1)
    elif comp_choice == "scissor":
        computer_label.configure(image=scissor_image1)

    if x == "rock":
        user_label.configure(image=rock_image1)
    elif x == "paper":
        user_label.configure(image=paper_image1)
    elif x == "scissor":
        user_label.configure(image=scissor_image1)

    check_win(x, comp_choice)

def update_user_score():
    """
        Update the player's score by incrementing it and updating the displayed score label.

        Retrieves the current score from the player's score label, increments it by 1,
        and updates the displayed score label with the new score.

        """
    score = int(player_score["text"])
    score += 1
    player_score["text"] = str(score)

def update_computer_score():
    """
       Update the computer's score by incrementing it and updating the displayed score label.

       Retrieves the current score from the computer's score label, increments it by 1,
       and updates the displayed score label with the new score.

       """
    score = int(computer_score["text"])
    score += 1
    computer_score["text"] = str(score)

def check_win(player, computer):
    """
       Check the winner of the game and update the scores accordingly.

       Compares the choices of the player and the computer to determine the winner.
       If the player wins, their score is updated; if the computer wins, its score is updated.

       Args:
           player (str): The choice of the player ('rock', 'paper', or 'scissor').
           computer (str): The randomly generated choice of the computer ('rock', 'paper', or 'scissor').

       """
    if player == computer:
        pass
    elif player == "rock":
        if computer == "paper":
            update_computer_score()
        else:
            update_user_score()
    elif player == "paper":
        if computer == "scissor":
            update_computer_score()
        else:
            update_user_score()
    elif player == "scissor":
        if computer == "rock":
            update_computer_score()
        else:
            update_user_score()
    else:
        pass

def quit():
    """
       Quit the game and exit the program.
       """
    sys.exit()

# Main code
r = Tk()
r.title("Rock, Paper, Scissor Game")
r.geometry("600x600")
r.maxsize(600, 600)
r.minsize(600, 600)
r.configure(bg="black")

welcome = Label(r, text="Welcome to the Game!!", font="ariel 20 italic", bg="black", fg="white")
luck = Label(r, text="***Best Of Luck***", font="ariel 20 italic", bg="black", fg="white")
welcome.place(x=180, y=10)
luck.place(x=200, y=50)

rock_button = Button(r, text="Rock", font="arial 15 italic", width=10, command=lambda: update_image("rock"))
rock_button.place(x=90, y=400)
paper_button = Button(r, text="Paper", font="arial 15 italic", width=10, command=lambda: update_image("paper"))
paper_button.place(x=230, y=400)
scissor_button = Button(r, text="Scissor", font="arial 15 italic", width=10, command=lambda: update_image("scissor"))
scissor_button.place(x=370, y=400)
check_result = Button(text="Check Final Score", font="arial 15 italic", width=15, command=final_score)
check_result.place(x=200, y=450)
quit=Button(text="Quit Game", font="arial 15 italic", width=8, command=quit)
quit.place(x=0,y=10)

rock_image1 = PhotoImage(file="rock.png").subsample(1, 1)
paper_image1 = PhotoImage(file="paper.png").subsample(1, 1)
scissor_image1 = PhotoImage(file="scissor.png").subsample(1, 1)

rock_image2 = PhotoImage(file="rock.png").subsample(1, 1)
paper_image2 = PhotoImage(file="paper.png").subsample(1, 1)
scissor_image2 = PhotoImage(file="scissor.png").subsample(1, 1)

player_score = Label(text=0, fg="white", font="ariel 20 bold", bg="black")
player_score.place(x=260, y=220)
computer_score = Label(text=0, fg="white", font="ariel 20 bold", bg="black")
computer_score.place(x=320, y=220)

you = Label(text="You:", fg="white", bg="black", font="ariel 15 italic")
computer = Label(text="Computer:", fg="white", bg="black", font="ariel 15 italic")
you.place(x=20, y=110)
computer.place(x=340, y=110)

user_label = Label(r, image=rock_image1, bg="black")
computer_label = Label(r, image=rock_image2, bg="black")
user_label.place(x=60, y=150)
computer_label.place(x=350, y=150)

final_score1 = Label(text="", bg="black", fg="white", font="ariel 15 italic")
final_score1.place(x=100, y=500)
final_score2 = Label(text="", bg="black", fg="white", font="ariel 15 italic")
final_score2.place(x=300, y=500)
msg = Label(text="", font="ariel 20 italic", bg="black", fg="white")
msg.place(x=230, y=550)

choice = ["rock", "paper", "scissor"]
r.mainloop()
