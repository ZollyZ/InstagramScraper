"""
    Project Name: Instagram Scrapper
    Author: ZollyZ
    GitHub: https://github.com/ZollyZ
"""
#Imports
import instaloader
import os
import tkinter as tk
from tkinter import filedialog

# Function to select a folder for storing the downloaded media
def select_folder():
    folder_path = filedialog.askdirectory()
    folder_path_entry.delete(0, tk.END)
    folder_path_entry.insert(0, folder_path)

# Function to download all the media files from an Instagram account
def download_media():
    # Get the Instagram username from the input field
    username = username_entry.get()

    # Create an instance of Instaloader class
    L = instaloader.Instaloader()

    try:
        # Load a profile by its username
        profile = instaloader.Profile.from_username(L.context, username)

        # Create a folder to store the media files
        folder_name = folder_path_entry.get()
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Download all the media files (photos and videos) from the profile
        for post in profile.get_posts():
            L.download_post(post, target=folder_name)

        # Show a success message
        tk.messagebox.showinfo("Success", f"All media from {username} has been downloaded.")
    except Exception as e:
        # Show an error message if the username is invalid or there is an error during download
        tk.messagebox.showerror("Error", str(e))


# Create the GUI
root = tk.Tk()
root.title("IGScraper by ZollyZ")

# Username input
username_label = tk.Label(root, text="Enter Instagram username:")
username_label.grid(row=0, column=0, padx=5, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=5, pady=5)

# Folder creation
folder_path_label = tk.Label(root, text="Enter desired subfolder name:")
folder_path_label.grid(row=1, column=0, padx=5, pady=5)
folder_path_entry = tk.Entry(root)
folder_path_entry.grid(row=1, column=1, padx=5, pady=5)


# Download button
download_button = tk.Button(root, text="Download", command=download_media)
download_button.grid(row=2, column=1, padx=5, pady=5)

# Start the GUI
root.mainloop()
