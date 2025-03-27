import tkinter as tk
from tkinter import messagebox

# Function to add a post
def add_post():
    post_content = post_entry.get()
    if post_content != "":
        # Insert the post into the feed
        feed_listbox.insert(tk.END, f"You: {post_content}")
        post_entry.delete(0, tk.END)  # Clear the input field
    else:
        messagebox.showwarning("Input Error", "Please write something to post.")

# Set up the main window
root = tk.Tk()
root.title("Facebook-like App")

# Frame for the header (profile name and image)
header_frame = tk.Frame(root, bg="blue", height=60)
header_frame.pack(fill="x")

# Profile picture (Placeholder)
profile_pic = tk.Label(header_frame, text="Profile Picture", bg="blue", fg="white", font=("Arial", 14))
profile_pic.pack(side=tk.LEFT, padx=10)

# Profile Name
profile_name = tk.Label(header_frame, text="
