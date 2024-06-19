THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):


        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Amazon meow meow", width=280, fill=THEME_COLOR, font=("Arial", 15, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.right_img = PhotoImage(file="images/true.png")
        self.wrong_img = PhotoImage(file="images/false.png")
        self.true = Button(image=self.right_img, highlightthickness=0, command=self.right_pressed) 
        self.true.grid(column=0, row=2)
        self.false = Button(image=self.wrong_img, highlightthickness=0, command=self.wrong_pressed)
        self.false.grid(column=1,row=2)

        self.label = Label(text="Score:0", highlightthickness=0)
        self.label.config(bg=THEME_COLOR, fg="white")
        self.label.grid(column=1,row=0)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.label.config(text=f"Score: {self.quiz.score}")
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've finished the quiz. Score:{self.quiz.score}")
            self.true.config(state="disabled")
            self.false.config(state="disabled")
    
    def right_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def wrong_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
    
    


    
        

