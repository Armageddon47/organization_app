import tkinter as tk
from tkinter import filedialog
from test import*

def browse_folder():
    folder_path = filedialog.askdirectory()
    print("Selected Folder Path:", folder_path)
    return folder_path

def browse_destination():
    folder_path = filedialog.askdirectory()
    print("Selected Destination Path:", folder_path)
    return folder_path




# Create a window
window = tk.Tk()
window.title("File Organizer")

# Create a label
label = tk.Label(text="Select a folder to organize and a destination folder:")
label.pack()

# Create a "Browse Folder" button
browse_folder_button = tk.Button(text="Browse Folder", command=browse_folder)
browse_folder_button.pack()

# Create a "Browse Destination" button
browse_destination_button = tk.Button(text="Browse Destination", command=browse_destination)
browse_destination_button.pack()

# Create an "Organize" button
organize_button = tk.Button(text="Organize", command=organize_files(browse_folder()))
organize_button.pack()

# Run the window
window.mainloop()
