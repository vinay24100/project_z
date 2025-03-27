import tkinter as tk
from tkinter import scrolledtext

# Function to send a message
def send_message():
    user_message = entry.get()
    if user_message != "":
        # Display user's message in the chat window
        chat_window.config(state=tk.NORMAL)  # Enable editing
        chat_window.insert(tk.END, "You: " + user_message + "\n")
        chat_window.yview(tk.END)  # Auto-scroll to the bottom
        chat_window.config(state=tk.DISABLED)  # Disable editing

        # Clear the input box
        entry.delete(0, tk.END)

        # Simulate a bot response after a delay
        root.after(1000, bot_response)

# Function to generate a simple bot response
def bot_response():
    bot_message = "Bot: Hello, how can I assist you?"
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, bot_message + "\n")
    chat_window.yview(tk.END)  # Auto-scroll to the bottom
    chat_window.config(state=tk.DISABLED)

# Set up the main window
root = tk.Tk()
root.title("WhatsApp-like Chat App")

# Chat window where messages are displayed
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, font=("Arial", 12), state=tk.DISABLED)
chat_window.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Entry box to type new messages
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.grid(row=1, column=0, padx=10, pady=10)

# Send button
send_button = tk.Button(root, text="Send", width=10, font=("Arial", 12), command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Start the main event loop
root.mainloop()

