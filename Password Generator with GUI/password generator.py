import random
import tkinter as tk
from tkinter import messagebox

# List of special characters to use in the password
special_characters = ['+', '-', '*', '/','@','#','$','%','^','&','*','(',')']

# List of English alphabet letters (lowercase and uppercase)
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

# List of Greek alphabet letters (lowercase and uppercase)
greek_letters = [
    'α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω',
    'Α', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'Μ', 'Ν', 'Ξ', 'Ο', 'Π', 'Ρ', 'Σ', 'Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω'
]

# Welcome message
print("Welcome to the Password Generator!")
print("This program generates a random password using special characters, English letters, and Greek letters.")
print("You can choose the length of the password, and it will include a mix of characters from these sets.")
print("Let's get started!")

gui= input("Do you want to use the GUI version? (yes/no): ").strip().lower()
if gui == 'yes':
    # --- GUI Implementation with tkinter ---
    def generate_password():
        try:
            length = int(length_entry.get())
            if length <= 0:
                messagebox.showerror("Error", "Please enter a positive number.")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            return

        all_lists = [special_characters, letters, greek_letters]
        output_password = ""
        for i in range(length):
            character_list = random.choice(all_lists)
            symbol = random.choice(character_list)
            output_password += symbol
        password_var.set(output_password)

    # Create main window
    root = tk.Tk()
    root.title("Password Generator")

    # Label for instructions
    tk.Label(root, text="Enter password length:").pack(pady=5)

    # Entry for password length
    length_entry = tk.Entry(root)
    length_entry.pack(pady=5)

    # Button to generate password
    tk.Button(root, text="Generate Password", command=generate_password).pack(pady=5)

    # Variable to hold the generated password
    password_var = tk.StringVar()

    # Entry widget to show the generated password (so you can copy it)
    password_entry = tk.Entry(root, textvariable=password_var, font=("Consolas", 14), fg="blue", width=30)
    password_entry.pack(pady=10)

    # Start the GUI event loop
    root.mainloop()

elif gui == 'no':
    # Combine all character lists into one list for easier selection
    all_lists = [special_characters, letters, greek_letters]
    while True:
        # Ask the user for the desired password length
        password_length = int(input("How many characters do you want your password to have? "))

        # Initialize the output password as an empty string
        output_password = ""

        # Loop to generate each character of the password
        for i in range(0, password_length):
            # Randomly select one of the character lists (special, English, or Greek)
            character_list = random.choice(all_lists)
            # Randomly select a symbol from the chosen list
            symbol = random.choice(character_list)
            # Add the selected symbol to the password
            output_password = output_password + symbol

        # Print the generated password
        print("Your password is:", output_password)
        print("You can copy and save it somewhere")
        print("I hope you liked my program!")