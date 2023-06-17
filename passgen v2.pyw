import tkinter as tk
import random
import string
import tkinter.messagebox as messagebox

# Function to generate a random password
def generate_password():
    length = length_entry.get()
    include_lowercase = lowercase_var.get()
    include_uppercase = uppercase_var.get()
    include_digits = digits_var.get()
    include_punctuation = punctuation_var.get()

    characters = ""
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_punctuation:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Please select at least one character type!")
        return

    password = ''.join(random.choice(characters) for _ in range(int(length)))
    password_label.config(text=password)

# Function to handle the copy button click event
def copy_password():
    password = password_label.cget("text")
    window.clipboard_clear()
    window.clipboard_append(password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create the main window
window = tk.Tk()
window.title("Custom Password Generator")

# Create a label and entry for password length
length_label = tk.Label(window, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

# Create checkboxes for character types
lowercase_var = tk.IntVar()
lowercase_check = tk.Checkbutton(window, text="Lowercase", variable=lowercase_var)
lowercase_check.pack()

uppercase_var = tk.IntVar()
uppercase_check = tk.Checkbutton(window, text="Uppercase", variable=uppercase_var)
uppercase_check.pack()

digits_var = tk.IntVar()
digits_check = tk.Checkbutton(window, text="Digits", variable=digits_var)
digits_check.pack()

punctuation_var = tk.IntVar()
punctuation_check = tk.Checkbutton(window, text="Punctuation", variable=punctuation_var)
punctuation_check.pack()

# Create a button to generate the password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Create a label to display the generated password
password_label = tk.Label(window, text="", font=("Arial", 14))
password_label.pack(padx=50, pady=20)

# Create a button to copy the password
copy_button = tk.Button(window, text="Copy Text", command=copy_password)
copy_button.pack(pady=10)

# Run the main event loop
window.mainloop()
