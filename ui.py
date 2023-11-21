
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ('Arial', 15, 'italic')


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('quizlet')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text='Score:0', bg=THEME_COLOR, fg='white')
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.question_text = self.canvas.create_text(150, 126, text="SOMME QUESTION TEXT", font=FONT, fill=THEME_COLOR,
                                                     width=280)

        vrai = PhotoImage(file='images/true.png')
        faux = PhotoImage(file='images/false.png')
        self.true = Button(image=vrai, highlightthickness=0, command=self.true_fun)
        self.true.grid(column=0, row=2)
        self.false = Button(image=faux, highlightthickness=0, command=self.false_fun)
        self.false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f"score: {self.quiz.score}")
            text_q = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=text_q)
        else:
            self.canvas.itemconfig(self.question_text, text="you've reached the end of quiz ")
            self.true.config(state='disabled')
            self.false.config(state='disabled')
    def true_fun(self):
        self.give_feedback(self.quiz.check_answer('true'))

    def false_fun(self):
        self.give_feedback(self.quiz.check_answer('false'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, func=self.get_next_question)
