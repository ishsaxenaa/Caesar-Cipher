import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    for char in text:
        if char.isalpha():
            index = alphabet.index(char.lower())
            if mode == 'e':
                new_index = (index + shift) % 26
            elif mode == 'd':
                new_index = (index - shift) % 26
            if char.isupper():
                result += alphabet[new_index].upper()
            else:
                result += alphabet[new_index]
        else:
            result += char

    return result

def encrypt_message():
    text = text_entry.get()
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")
        return
    encrypted_text = caesar_cipher(text, shift, 'e')
    result_label.config(text=f"Encrypted text: {encrypted_text}")

def decrypt_message():
    text = text_entry.get()
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")
        return
    decrypted_text = caesar_cipher(text, shift, 'd')
    result_label.config(text=f"Decrypted text: {decrypted_text}")

def create_gradient(canvas, width, height, color1, color2):
    steps = 100  # Number of gradient steps
    for i in range(steps):
        r1, g1, b1 = window.winfo_rgb(color1)
        r2, g2, b2 = window.winfo_rgb(color2)
        r = int(r1 + (r2 - r1) * i / steps)
        g = int(g1 + (g2 - g1) * i / steps)
        b = int(b1 + (b2 - b1) * i / steps)
        color = f'#{r>>8:02x}{g>>8:02x}{b>>8:02x}'
        canvas.create_line(0, i * height // steps, width, i * height // steps, fill=color, width=2)

# Create the main window
window = tk.Tk()
window.title("Caesar Cipher GUI")

# Create a Canvas to draw the gradient background
canvas = tk.Canvas(window, width=400, height=300)
canvas.pack(fill="both", expand=True)

# Create the gradient background
create_gradient(canvas, 400, 300, 'darkblue', 'skyblue')

# Place widgets on the Canvas
text_label = tk.Label(canvas, text="Enter the message:", bg='darkblue', font=('Arial', 12))
canvas.create_window(200, 50, window=text_label)

text_entry = tk.Entry(canvas, width=50)
canvas.create_window(200, 80, window=text_entry)

shift_label = tk.Label(canvas, text="Enter the shift value:", bg='darkblue', font=('Arial', 12))
canvas.create_window(200, 110, window=shift_label)

shift_entry = tk.Entry(canvas, width=10)
canvas.create_window(200, 140, window=shift_entry)

encrypt_button = tk.Button(canvas, text="Encrypt", command=encrypt_message)
canvas.create_window(150, 180, window=encrypt_button)

decrypt_button = tk.Button(canvas, text="Decrypt", command=decrypt_message)
canvas.create_window(250, 180, window=decrypt_button)

result_label = tk.Label(canvas, text="", bg='lightblue', font=('Arial', 12))
canvas.create_window(200, 220, window=result_label)

# Start the main loop
window.mainloop()
