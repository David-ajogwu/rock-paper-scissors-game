import tkinter as tk
from tkinter import messagebox
import random

window = tk.Tk ()
window.title = ('Rock,paper, scissors game')
window.geometry = ('400x300')

def determine_winner(player_choice ):
    choices = ('Rock','paper','scissors')
    computer_choice = random.choice(choices)
    result = ''

    if player_choice == computer_choice:
        result = 'its a tie'
    elif player_choice == ('Rock' and computer_choice == 'scissors')or\
        player_choice == ('scissors' and computer_choice == 'paper')or\
        player_choice == ('paper' and computer_choice == 'Rock'):
        result = 'You are the winner'
    else:
        result = 'You lost', 'kindly restart the game'

    result_message = f'your turn {player_choice}.\nComputer turn {computer_choice}.\n{result}'
    messagebox.showinfo('result', result_message)


def rock():
    determine_winner('rock')

def paper():
    determine_winner('paper')

def scissors():
    determine_winner('scissors')


title_label = tk.Label(window, text='rock, paper, scissors', font=('bookmanoldstyle', 22))
title_label.pack(pady=10)

rock_button = tk.Button(window, text='Rock', command= rock, width=15, height=2  )
rock_button.pack(pady=10)

paper_button = tk.Button(window, text='Rock', command= paper, width=15, height=2  )
paper_button.pack(pady=10)

scissors_button = tk.Button(window, text='Rock', command= scissors, width=15, height=2  )
scissors_button.pack(pady=10)

window.mainloop



