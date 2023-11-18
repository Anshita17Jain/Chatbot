import tkinter as tk
from tkinter import scrolledtext

class ChatbotGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Chatbot GUI")

        self.chat_history = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=40, height=10)
        self.chat_history.pack(padx=10, pady=10)

        self.user_input = tk.Entry(self.root, width=40)
        self.user_input.pack(pady=10)

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack()

        # Initialize chatbot
        self.user_name = ""
        self.initialize_chatbot()

    def initialize_chatbot(self):
        self.add_to_chat_history("Hello! I'm a chatbot. What's your name?")
        self.send_button["command"] = self.get_user_name

    def get_user_name(self):
        self.user_name = self.user_input.get()
        self.add_to_chat_history(f"Nice to meet you, {self.user_name}! How can I help you today?")
        self.user_input.delete(0, tk.END)
        self.send_button["command"] = self.send_message

    def send_message(self):
        user_input_text = self.user_input.get()
        self.add_to_chat_history(f"{self.user_name}: {user_input_text}")

        # Call your chatbot logic here (replace the next line with your chatbot's response)
        bot_response = get_response(user_input_text, self.user_name)

        self.add_to_chat_history(f"Chatbot: {bot_response}")

        self.user_input.delete(0, tk.END)

    def add_to_chat_history(self, message):
        self.chat_history.insert(tk.END, message + "\n")
        self.chat_history.see(tk.END)

    def run(self):
        self.root.mainloop()

# Replace this function with your actual chatbot logic
def get_response(user_input, user_name):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return f"Hello, {user_name}! How can I assist you today?"

    if "how are you" in user_input or "how are you doing" in user_input:
        return "I'm functioning well, thank you. How about you?"

    if "tell me a joke" in user_input or "say something funny" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything! 😄"
    
    if "what's the weather like today?" in user_input or "tell me the weather":
        return "I'm sorry, I don't have real-time weather information. You can check a weather website or use a weather app for the latest updates."

    if "favorite colour" in user_input:
        return "I don't have a favorite colour. What's yours?"
    
    if "how can I learn programming" in user_input or "programming tips":
        return "Learning programming is a great choice! Start with the basics of a programming language like Python, practice coding regularly, and work on small projects to apply what you've learned."
    
    if "your favorite book" in user_input or "what do you like to read?" :
        return "I don't have preferences in books. However, I can recommend some popular books in various genres if you're interested."
    
    if "what can you do" in user_input or "how can you help me" in user_input or "tell me your abilities" in user_input:
        return "I can provide information, answer questions, and assist with various tasks. How can I help you today?"

    if "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! 😊"

    if "bye" in user_input or "see you later" in user_input or "farewell" in user_input:
        return f"Goodbye, {user_name}! Have a great day. 👋"

    # Add more custom responses based on your chatbot's functionality

    return "I'm sorry, I didn't quite catch that. Can you please rephrase or ask a different question?"

if __name__ == "__main__":
    chatbot_gui = ChatbotGUI()
    chatbot_gui.run()
