# bot.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import tkinter as tk
import logging
from cleaner_yaml import clean_yaml


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

    input_field = tk.Entry(root, width=50, bd=4, insertwidth=3)
    input_field.pack()

    def send_message(event=None):
        user_input = input_field.get()

        input_field.delete(0, tk.END)

        response = bot_response(user_input)

        text_area.insert(tk.END, f"You: {user_input}\n")
        text_area.insert(tk.END, f"Fitbot🏋: {response}\n")

        if not response:
            root.destroy()

    send_button = tk.Button(root, text="Send", command=lambda: send_message())
    send_button.pack()

    root.bind('<Return>', send_message)
    logger = logging.getLogger()

    root.mainloop()


training_corpus = ['english/sports.yml', 'english/food.yml']


def main():
    trainer = ListTrainer(chatbot)
    for corpus in training_corpus:
        cleaned_data = clean_yaml(corpus)
        trainer.train(cleaned_data)
    display_root()


if __name__ == "__main__":
    main()