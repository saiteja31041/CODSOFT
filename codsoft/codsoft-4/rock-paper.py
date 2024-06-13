import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        self.user_choice = tk.StringVar()
        self.result_text = tk.StringVar()
        self.user_score = 0
        self.computer_score = 0

        self.choice_label = tk.Label(root, text="Choose: Rock, Paper, or Scissors")
        self.choice_label.pack(pady=10)

        choices = ['Rock', 'Paper', 'Scissors']
        for choice in choices:
            button = tk.Radiobutton(root, text=choice, variable=self.user_choice, value=choice)
            button.pack()

        play_button = tk.Button(root, text="Play", command=self.play)
        play_button.pack(pady=10)

        self.result_label = tk.Label(root, textvariable=self.result_text)
        self.result_label.pack()

        self.score_label = tk.Label(root, text="Score: User 0 - 0 Computer")
        self.score_label.pack(pady=5)

        play_again_button = tk.Button(root, text="Play Again", command=self.play_again)
        play_again_button.pack(pady=10)

    def play(self):
        user_choice = self.user_choice.get()
        computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
             (user_choice == 'Paper' and computer_choice == 'Rock') or \
             (user_choice == 'Scissors' and computer_choice == 'Paper'):
            result = "You win!"
            self.user_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1

        self.result_text.set(f"User: {user_choice} | Computer: {computer_choice} | {result}")
        self.update_score()

    def update_score(self):
        self.score_label.config(text=f"Score: User {self.user_score} - {self.computer_score} Computer")

    def play_again(self):
        self.user_choice.set('')
        self.result_text.set('')
        self.update_score()

root = tk.Tk()
app = RockPaperScissors(root)
root.mainloop()
