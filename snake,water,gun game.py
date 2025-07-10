from tkinter import *
from tkinter import scrolledtext
import random

root = Tk()
root.title('Snake, Water and Gun Game')
root.geometry('600x600')

Player_score = 0
Computer_score = 0

def play(user_choice):
  global Player_score, Computer_score
  options = ['Snake', 'Water', 'Gun']
  computer_choice = random.choice(options)

  if user_choice == computer_choice:
    result = "It's a Tie"
  elif (user_choice == "Snake" and computer_choice == "Water") or (user_choice == "Water" and computer_choice == "Gun") or (user_choice == "Gun" and computer_choice == "Snake"):
    result = "You Win !"
    Player_score += 1
  else: 
    result = "Computer Wins !"
    Computer_score += 1

  display_screen.delete('1.0', END)
  display_screen.insert(END, f"Your Choice : {user_choice} \nComputer Choice : {computer_choice} \nResult is: {result} \n\n Player Score: {Player_score} \n Computer Score: {Computer_score}")

def resetGame():
  global Player_score, Computer_score
  Player_score = 0
  Computer_score = 0
  display_screen.delete('1.0', END)
  display_screen.insert(END, "Game Reset! \n\n Player Score: 0 \n Computer Score: 0")

AppHeader = Label(root, text='Snake, Water and Gun Game', bg='skyblue',fg='white', font=('Georgia', 24))
AppHeader.pack(fill=X, expand=True)

resultText = Label(root, text='Result Screen')
resultText.pack(anchor=W, padx=10)

display_screen = scrolledtext.ScrolledText(root, wrap=WORD, height=10, font=('Georgia', 15))
display_screen.pack(fill=BOTH,expand=True, padx=10)

button_frame = Frame(root)
button_frame.pack(pady=10)

snakeBtn = Button(button_frame, text='Snake', command=lambda: play("Snake"), width=20, bg='green',fg='white', font=('Georgia', 12), relief=RAISED, bd=5)
snakeBtn.grid(row=0, column=0, padx=8)

waterBtn = Button(button_frame, text='Water', command=lambda: play('Water'), width=20, bg='skyblue', font=('Georgia', 12), relief=RAISED, bd=5)
waterBtn.grid(row=0, column=1, padx=8)

gunBtn = Button(button_frame, text='Gun', command=lambda: play('Gun'), width=20, bg='black',fg='white', font=('Georgia', 12), relief=RAISED, bd=5)
gunBtn.grid(row=0, column=2, padx=8)

playAgainBtn = Button(button_frame, text='Play Again',command=resetGame, width=20, bg='white',fg='black', font=('Georgia', 12), relief=RAISED, bd=5)
playAgainBtn.grid(row=1, column=1, padx=8)

root.mainloop()

