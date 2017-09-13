from tkinter import *
from Quiz import Quiz
from Question import Question
import Resources
import os
import pickle

class Quiz_Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Quiz GUI")
        self.pack(fill=BOTH, expand=1)
        # quit_button = Button(self, text="quit", command=self.client_exit)
        # quit_button.place(x=0, y=0)
        # i = 1
        # for quiz in os.listdir(Resources.quizzes_file_path):
        #     print(quiz)
        #     b = Button(self, text=quiz)
        #     b.place(x=0, y=(20 * i))
        #     i += 1
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

        edit = Menu(menu)
        edit.add_command(label='Show Text', command=self.show_text)
        menu.add_cascade(label='Edit', menu=edit)

        quizzes = Menu(menu)
        for quiz in os.listdir(Resources.quizzes_file_path):
            quizzes.add_command(label=quiz, command=self.quiz_title())
        quizzes.add_cascade(label='Quizzes', menu=quizzes)


    def client_exit(self):
         exit()

    def show_text(self):
        text = Label(self, text='Hello world!')
        text.pack()

    def quiz_title(self):
        text = Label(self, text="Hi")
        text.pack()


root = Tk()
root.geometry("400x300")
app = Quiz_Application(root)
root.mainloop()