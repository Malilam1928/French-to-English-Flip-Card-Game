from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
TEXT_FONT_40 = ("Ariel", 40, "italic")
TEXT_FONT_60 = ("Ariel", 60, "bold")
data_dict = {}

# -----------------------------------CREATING NEW FRENCH CARDS ---------------------#
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")
word_dict = {}


def random_french_word():
    global word_dict, flip_timer
    window.after_cancel(flip_timer)
    word_dict = random.choice(data_dict)
    rand_word_french = word_dict["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=f"{rand_word_french}", fill="black")
    canvas.itemconfig(background_image, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


# -----------------------------------FLIPPING CARDS--------------------------------#

def flip_card():
    rand_word_english = word_dict["English"]
    canvas.itemconfig(background_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=f"{rand_word_english}", fill="white")

    # rand_word_english = rand_word["English"]
    # card_title_back = canvas.create_text(400, 150, text="English", font=TEXT_FONT_40)
    # card_word_back = canvas.create_text(400, 263, text=f"{rand_word_english}", font=TEXT_FONT_60)


# -----------------------------------SAVING PROGRESS-------------------------------#

def is_known():
    data_dict.remove(word_dict)
    words_to_learn = pandas.DataFrame(data_dict)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)

    random_french_word()


# -----------------------------------UI SETUP--------------------------------------#
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
background_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=TEXT_FONT_40)
card_word = canvas.create_text(400, 263, text="", font=TEXT_FONT_60)
canvas.grid(row=0, column=0, columnspan=2)

# Creating Buttons
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=random_french_word)
wrong_button.grid(row=1, column=0)

random_french_word()
window.mainloop()
