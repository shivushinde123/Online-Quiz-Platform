import tkinter as tk
from tkinter import messagebox

# Quiz Questions
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Chennai", "Kolkata"],
        "answer": "Delhi"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["Python", "HTML", "C", "Java"],
        "answer": "HTML"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "Central Process Unit",
            "Central Processing Unit",
            "Computer Power Unit",
            "Core Processing Unit"
        ],
        "answer": "Central Processing Unit"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/* */", "<!-- -->"],
        "answer": "#"
    },
    {
        "question": "Which company developed Python?",
        "options": ["Microsoft", "Google", "Python Software Foundation", "Oracle"],
        "answer": "Python Software Foundation"
    },
    {
        "question": "Which data type is used to store text in Python?",
        "options": ["int", "float", "str", "bool"],
        "answer": "str"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },
    {
        "question": "Which HTML tag is used for largest heading?",
        "options": ["<h6>", "<h4>", "<h2>", "<h1>"],
        "answer": "<h1>"
    }
]



class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Quiz Platform")
        self.root.geometry("500x400")
        self.root.config(bg="#1e1e2f")

        self.q_index = 0
        self.score = 0

        self.question_label = tk.Label(
            root, text="", font=("Arial", 14, "bold"),
            bg="white", fg="black", wraplength=450, padx=10, pady=10
        )
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()

        self.option_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(
                root, text="", variable=self.var, value="",
                font=("Arial", 12),
                bg="#1e1e2f", fg="white",
                selectcolor="#6a5acd",
                activebackground="#1e1e2f",
                activeforeground="white"
            )
            rb.pack(anchor="w", padx=50)
            self.option_buttons.append(rb)

        self.next_btn = tk.Button(
            root, text="Next",
            font=("Arial", 12, "bold"),
            bg="#6a5acd", fg="white",
            command=self.next_question
        )
        self.next_btn.pack(pady=20)

        self.load_question()

    def load_question(self):
        self.var.set(None)
        q = questions[self.q_index]
        self.question_label.config(text=q["question"])

        for i, option in enumerate(q["options"]):
            self.option_buttons[i].config(text=option, value=option)

    def next_question(self):
        if self.var.get() == "":
            messagebox.showwarning("Warning", "Please select an answer!")
            return

        if self.var.get() == questions[self.q_index]["answer"]:
            self.score += 1

        self.q_index += 1

        if self.q_index < len(questions):
            self.load_question()
        else:
            messagebox.showinfo(
                "Quiz Completed",
                f"Your Score: {self.score}/{len(questions)}"
            )
            self.root.destroy()

# Run App
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
