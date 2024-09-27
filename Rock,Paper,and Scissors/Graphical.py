import tkinter as tk
import random

# Function to determine winner
def determine_winner(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result.set(f"Tie! Both chose {player_choice}")
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result.set(f"You Win! {player_choice} beats {computer_choice}")
    else:
        result.set(f"You Lose! {computer_choice} beats {player_choice}")

# Function to reset the game
def reset_game():
    result.set("Choose Rock, Paper, or Scissors")

# Initialize the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("400x400")  # Set the window size
root.configure(bg="#F0F0F0")  # Set background color

# Make sure the grid cells expand to center the widgets
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Define result variable
result = tk.StringVar()
result.set("Choose Rock, Paper, or Scissors")

# Create label for the title
title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Helvetica", 20, "bold"), bg="#F0F0F0", fg="#333333")
title_label.grid(row=0, column=0, columnspan=3, pady=20)

# Create buttons for player choices with styling
button_style = {"font": ("Helvetica", 14, "bold"), "width": 10, "height": 2, "bg": "#4CAF50", "fg": "white", "relief": "raised"}

rock_button = tk.Button(root, text="Rock", command=lambda: determine_winner("Rock"), **button_style)
paper_button = tk.Button(root, text="Paper", command=lambda: determine_winner("Paper"), **button_style)
scissors_button = tk.Button(root, text="Scissors", command=lambda: determine_winner("Scissors"), **button_style)

# Position buttons in a grid and center them
rock_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
paper_button.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
scissors_button.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

# Create label to display the result with styling
result_label = tk.Label(root, textvariable=result, font=("Helvetica", 14), bg="#F0F0F0", fg="#FF5733")
result_label.grid(row=2, column=0, columnspan=3, pady=20)

# Create Reset button
reset_button = tk.Button(root, text="Reset", command=reset_game, font=("Helvetica", 14, "bold"), width=10, height=2, bg="#f44336", fg="white", relief="raised")
reset_button.grid(row=3, column=1, pady=20)

# Start the GUI event loop
root.mainloop()
