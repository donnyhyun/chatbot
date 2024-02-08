# bot.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# from cleaner import clean_corpus
import tkinter as tk
import logging


CORPUS_FILE = "chat.txt"
chatbot = ChatBot(
    "Fitbot",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)


def bot_response(input_val):
    exit_conditions = ("quit", "exit")
    if input_val in exit_conditions:
        return None
    else:
        return f"{chatbot.get_response(input_val)}"


def display_root():
    root = tk.Tk()
    root.title("Chatbot")

    text_area = tk.Text(root, bg="white", width=70, height=20)
    text_area.pack()

    input_field = tk.Entry(root, width=50)
    input_field.pack()

    send_button = tk.Button(root, text="Send", command=lambda: send_message())
    send_button.pack()

    def send_message():
        user_input = input_field.get()

        input_field.delete(0, tk.END)

        response = bot_response(user_input)

        text_area.insert(tk.END, f"You: {user_input}\n")
        text_area.insert(tk.END, f"🏋: {response}\n")

        if not response:
            root.destroy()
    logger = logging.getLogger()

    root.mainloop()


def main():
    trainer = ListTrainer(chatbot)
    # cleaned_corpus = clean_corpus(CORPUS_FILE)
    # trainer.train(cleaned_corpus)
    display_root()


if __name__ == "__main__":
    main()