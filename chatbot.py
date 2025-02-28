import tkinter as tk
from tkinter import scrolledtext

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot Assistant")
        self.root.geometry("500x500")

        # Chat Window
        self.chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
        self.chat_window.pack(pady=10)
        self.chat_window.insert(tk.END, "Chatbot: Hello! I am your assistant. How can I assist you today?\n")

        # User Input Field
        self.user_input = tk.Entry(root, width=50)
        self.user_input.pack(pady=5)

        # Send Button
        self.send_button = tk.Button(root, text="Send", command=self.process_input)
        self.send_button.pack()

        # State Variables
        self.awaiting_numbers = False  # Track if the chatbot is waiting for numbers

    def process_input(self):
        user_text = self.user_input.get().strip()
        self.chat_window.insert(tk.END, f"User: {user_text}\n")
        self.user_input.delete(0, tk.END)

        if self.awaiting_numbers:
            self.process_numbers(user_text)
            self.awaiting_numbers = False
            return

        # Bot Responses
        if user_text.lower() == "hello":
            response = "Hi there! How can I help you today?"
        elif user_text.lower() == "integer":
            response = "Please enter a list of integers (comma-separated):"
            self.chat_window.insert(tk.END, f"Chatbot: {response}\n")
            self.awaiting_numbers = True  # Set flag for next input
            return
        elif user_text.lower() == "thanks":
            response = "Goodbye! Have a great day!"
            self.chat_window.insert(tk.END, f"Chatbot: {response}\n")
            self.root.after(2000, self.root.quit)  # Close after 2 seconds
            return
        else:
            response = "I'm sorry, I didn't understand that. Can you rephrase?"

        self.chat_window.insert(tk.END, f"Chatbot: {response}\n")

    def process_numbers(self, numbers):
        try:
            num_list = list(map(int, numbers.split(',')))
            sum_numbers = sum(num_list)
            max_number = max(num_list)
            reversed_list = list(reversed(num_list))

            result = f"\n       Sum: {sum_numbers}\n       Maximum: {max_number}\n       Reversed List: {reversed_list}"
        except ValueError:
            result = "Invalid input! Please enter only integers separated by commas."

        self.chat_window.insert(tk.END, f"Chatbot: {result}\n")
        self.chat_window.insert(tk.END, "Chatbot: How else can I assist you?\n")

# Run the chatbot
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
