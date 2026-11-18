from translate import Translator
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

# Initialize the main window
root = tk.Tk()
root.title('Language Translator')

# Load and display background image
try:
    img = ImageTk.PhotoImage(Image.open("langtrans.jpg"))
    lbl = tk.Label(root, image=img)
    lbl.pack()
except FileNotFoundError:
    print("Warning: 'langtrans.jpg' not found. Skipping image display.")

# Main Heading
h1 = Label(root, text='Language Translator', font='Sans 14', bg='yellow', fg='blue')
h1.pack(fill='both')

# Source Language Selection
t1 = Label(root, text='From', font='Sans 14 bold')
t1.pack()

lang1 = ['English']
c1 = ttk.Combobox(root, values=lang1, font='Sans 14 bold')
c1.pack()

# Target Language Selection
t2 = Label(root, text='TO', font='Sans 14 bold')
t2.pack()

lang2 = ['English', 'Hindi', 'Kannada']
c2 = ttk.Combobox(root, values=lang2, font='Sans 14 bold')
c2.pack()

# Text Entry Area
t3 = Label(root, text='Enter text', font='Sans 14 bold')
t3.pack()
e3 = Entry(root, font='Sans 14 bold')
e3.pack()

# Translation Function
def trans():
    t1_val = c1.get()
    t2_val = c2.get()
    t3_val = e3.get()
    
    # Initialize translator and get result
    translator = Translator(from_lang=t1_val, to_lang=t2_val)
    translation = translator.translate(t3_val)
    
    # Display the result in a label
    lb = Label(root, bg="cyan", text=translation, font='Sans 14')
    lb.pack()
    print(translation)

# Submit Button
b1 = Button(root, text='Submit', command=trans, font='Sans 12', bg='blue', fg='yellow')
b1.pack(fill='both')

# Run the application loop
root.mainloop()
