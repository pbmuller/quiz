from tkinter import *
from Quiz import Quiz
from Question import Question
import Resources
import os

class Quiz_Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Quiz GUI")
        self.pack(fill=BOTH, expand=1)
        quit_button = Button(self, text="quit", command=self.client_exit)
        quit_button.place(x=0, y=0)
        i = 1
        for quiz in os.listdir(Resources.quizzes_file_path):
            print(quiz)
            b = Button(self, text=quiz)
            b.place(x=0, y=(20 * i))
            i += 1

    def client_exit(self):
        exit()


root = Tk()
root.geometry("400x300")
app = Quiz_Application(root)
root.mainloop()