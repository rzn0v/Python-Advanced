from tkinter import *
import requests

def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    quote = response.json()["quote"]
    canvas.itemconfig(text, text=quote)



window = Tk()
window.title("Kanye Quotes")
window.config(padx=50, pady=50)
canvas = Canvas(width=300, height=414)
background = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background)
text = canvas.create_text(150, 207, text="Your text goes here", font=("Arial", 30, "bold"), width=250, fill="white")
canvas.grid(column=0, row=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(column=0, row=1)








window.mainloop()