# Password Generator

This is a simple yet versatile password generator written in Python. It allows users to generate random passwords that include:

- Special characters (`+`, `-`, `*`, `/`, `@`, `#`, etc.)
- English letters (both lowercase and uppercase)
- Greek letters (both lowercase and uppercase)

The program provides two modes of use:
- **Command-line interface (CLI)**
- **Graphical User Interface (GUI) using Tkinter**

## Features

- User-defined password length.
- Random character selection from multiple sets.
- Supports both English and Greek letters.
- Option to use a GUI or stay in the terminal.

## How to Run

### Requirements
- Python 3.x
- Tkinter (usually included with standard Python distributions)

### Run the Program

```bash
python password\ generator.py
```

You will be asked whether you want to use the GUI:

```
Do you want to use the GUI version? (yes/no):
```

### If you choose `yes`:
- A GUI window will appear.
- Enter the desired password length.
- Click "Generate Password" to create a new password.

### If you choose `no`:
- The program runs in the terminal.
- You’ll be prompted to enter the desired length.
- A password will be printed directly to the console.

## Notes

- The GUI version uses `tkinter.messagebox` for error handling.
- The terminal version runs in a loop and generates a new password every time you provide a new length.
- The output password may include Greek characters, so make sure your application or website supports Unicode characters if you're using these passwords.

## Example Output

```text
Welcome to the Password Generator!
This program generates a random password using special characters, English letters, and Greek letters.
You can choose the length of the password, and it will include a mix of characters from these sets.
Let's get started!
Do you want to use the GUI version? (yes/no): no
How many characters do you want your password to have? 12
Your password is: αrΔh8@XωK$Π
You can copy and save it somewhere
I hope you liked my program!
```

## License

This project is released for educational purposes. You are free to use, modify, and distribute it.
