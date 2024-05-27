import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Importing PIL for image resizing
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        self.random_number = None
        self.guess_count = 0

        self.create_widgets()

    def create_widgets(self):
        # Load and resize the image
        original_image = Image.open("banner.png")
        resized_image = original_image.resize((300, 200))  # Resize the image
        self.image = ImageTk.PhotoImage(resized_image)

        # Display the image
        self.image_label = tk.Label(self.root, image=self.image)
        self.image_label.pack()

        # Start button
        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.start_button.pack()

        # Instruction label
        self.instruction_label = tk.Label(self.root, text="")
        self.instruction_label.pack()

        # Guess entry (initially hidden)
        self.guess_entry = tk.Entry(self.root)
        self.guess_entry.pack()
        self.guess_entry.pack_forget()

        # Guess button (initially hidden)
        self.guess_button = tk.Button(self.root, text="Guess", command=self.check_guess)
        self.guess_button.pack()
        self.guess_button.pack_forget()

        # Result label
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def start_game(self):
        self.random_number = random.randint(1, 100)
        self.guess_count = 0

        self.instruction_label.config(text="Guess a number between 1 and 100:")
        self.guess_entry.pack()
        self.guess_button.pack()
        self.result_label.config(text="")
        self.guess_entry.delete(0, tk.END)

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number")
            return

        self.guess_count += 1

        if guess < self.random_number:
            self.result_label.config(text="Too low! Try again.")
        elif guess > self.random_number:
            self.result_label.config(text="Too high! Try again.")
        else:
            messagebox.showinfo("Congratulations!", f"You guessed it in {self.guess_count} attempts!")
            self.reset_game()

    def reset_game(self):
        self.random_number = None
        self.guess_count = 0
        self.instruction_label.config(text="")
        self.guess_entry.pack_forget()
        self.guess_button.pack_forget()
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
