import tkinter as tk
from tkinter import messagebox

# Sample questions list
questions = [
    {
        "topic": "Loops",
        "question": "What will be the output of this Python code?",
        "code": "for i in range(3):\n    print(i)",
        "options": ["0 1 2", "1 2 3", "0 1 2 3", "1 2"],
        "answer": 0  # Position in the options array (indexing starts from 0)
    },
    {
        "topic": "Strings",
        "question": "What is the output of the following Python code?",
        "code": "'hello'.upper()",
        "options": ["HELLO", "hello", "Error", "None of the above"],
        "answer": 0
    },
    {
        "topic": "Lists",
        "question": "Which method is used to add an element at the end of a list?",
        "code": "my_list.append(5)",
        "options": ["add()", "append()", "insert()", "extend()"],
        "answer": 1
    }
]

# Create the main window
root = tk.Tk()
root.title("Python Quiz Generator")
root.geometry("400x400")

# Add widgets
topic_label = tk.Label(root, text="Enter Python topic:")
topic_label.pack(pady=10)

topic_entry = tk.Entry(root)
topic_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Python Question", command=lambda: generate_question())
generate_button.pack(pady=20)

question_label = tk.Label(root, text="", wraplength=350)
question_label.pack(pady=10)

code_label = tk.Label(root, text="", wraplength=350, font=("Courier", 10))
code_label.pack(pady=5)

options_var = tk.IntVar(value=-1)  # Initialize with -1 (no option selected)
options_frame = tk.Frame(root)
options_frame.pack(pady=10)

submit_button = tk.Button(root, text="Submit", command=lambda: check_answer())
submit_button.pack(pady=20)

# Function to generate a question based on the entered topic
def generate_question():
    topic = topic_entry.get().strip()
    question_found = False
    
    # Clear previous options
    for widget in options_frame.winfo_children():
        widget.destroy()
    
    for question in questions:
        if question["topic"].lower() == topic.lower():
            question_found = True
            question_label.config(text=question["question"])
            code_label.config(text=question["code"])
            
            # Create radio buttons for the options
            for i, option in enumerate(question["options"]):
                rb = tk.Radiobutton(options_frame, text=option, variable=options_var, value=i)
                rb.pack(anchor="w")
            break
    
    if not question_found:
        messagebox.showerror("Error", f"No questions found for topic: {topic}")

# Function to check the answer when the Submit button is clicked
def check_answer():
    selected_option = options_var.get()
    if selected_option == -1:
        messagebox.showerror("Error", "Please select an answer.")
        return
    
    topic = topic_entry.get().strip()
    for question in questions:
        if question["topic"].lower() == topic.lower():
            print(f"Selected Option: {selected_option}, Correct Answer: {question['answer']}")  # Debug print
            
            # Check if selected option matches the correct answer
            if selected_option == question["answer"]:
                messagebox.showinfo("Correct!", "Well done! The answer is correct.")  # Correct message
            else:
                messagebox.showerror("Incorrect", "Incorrect. Try again.")  # Incorrect message
            break

# Start the Tkinter event loop
root.mainloop()
