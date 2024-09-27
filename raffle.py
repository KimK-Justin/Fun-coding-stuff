import tkinter as tk
import random
import os

# Initialize the raffle pool
raffle_pool = []

# Path for the text file to store entries
file_path = "raffle_entries.txt"

# Function to load existing entries from the file
def load_entries_from_file():
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            for line in file:
                name = line.strip()
                raffle_pool.append(name)

# Function to save the current raffle pool to the file
def save_entries_to_file():
    with open(file_path, "w") as file:
        for entry in raffle_pool:
            file.write(entry + "\n")

# Function to add a person and their entries to the raffle pool
def add_entries():
    name = name_entry.get()
    try:
        entries = int(entries_entry.get())
        if entries > 0:
            for _ in range(entries):
                raffle_pool.append(name)
            status_label.config(text=f"Added {entries} entries for {name}.")
            save_entries_to_file()  # Save entries to file after adding
        else:
            status_label.config(text="Number of entries must be positive.")
    except ValueError:
        status_label.config(text="Please enter a valid number for entries.")
    name_entry.delete(0, tk.END)
    entries_entry.delete(0, tk.END)

# Function to randomly pick a winner from the raffle pool
def pick_winner():
    if raffle_pool:
        winner = random.choice(raffle_pool)
        status_label.config(text=f"The winner is: {winner}")
    else:
        status_label.config(text="No entries in the raffle.")

# Function to display all entries
def display_entries():
    entries_list.delete(0, tk.END)
    for entry in raffle_pool:
        entries_list.insert(tk.END, entry)

# Create the main application window
window = tk.Tk()
window.title("Raffle System")

window.geometry("600x400")

# Create input fields for name and entries
name_label = tk.Label(window, text="Participant's Name:")
name_label.pack()

name_entry = tk.Entry(window)
name_entry.pack()

entries_label = tk.Label(window, text="Number of Entries:")
entries_label.pack()

entries_entry = tk.Entry(window)
entries_entry.pack()

# Create buttons for adding entries and picking a winner
add_button = tk.Button(window, text="Add Entries", command=add_entries)
add_button.pack()

pick_button = tk.Button(window, text="Pick Winner", command=pick_winner)
pick_button.pack()

# Display the current entries
display_button = tk.Button(window, text="Display Entries", command=display_entries)
display_button.pack()

# Create a listbox to display all entries
entries_list = tk.Listbox(window)
entries_list.pack()

# Status label to display messages
status_label = tk.Label(window, text="")
status_label.pack()

# Load the existing entries from the file (if any)
load_entries_from_file()

# Start the GUI event loop
window.mainloop()