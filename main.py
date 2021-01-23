import random
import pandas
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------- CREATE NEW FLASH CARDS ----------------------

data = pandas.read_csv("data/german_words.csv")
data_dict = data.to_dict(orient="records")


def next_card(args):
    current_card = random.choice(data_dict)
    canvas.config(card_title, text="French")
    canvas.config(card_word, text=current_card["French"])


# ---------------------- USER INTERFACE ----------------------

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 40, "italic"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")

unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

next_card()

# ---------------------- MAINLOOP ----------------------

window.mainloop()
