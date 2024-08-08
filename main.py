import tkinter as tk
from tkinter import ttk
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = '''
Answer the question below:

Here is the conversation history: {context}

Question: {question}
Answer: 
'''
model = OllamaLLM(model='llama3')
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

def handle_conversation():
    context = ''
    user_input = f"Generate {num_questions_var.get()} MCQ’s for class {class_var.get()} on the topic of {topic_name_var.get()}"
    result = chain.invoke({'context': context, 'question': user_input})
    context += f"\nUser: {user_input}\nAI: {result}"
    print(user_input)   
    print(result)
    
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, result)
    output_text.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Input Form")

font = ("Roboto", 16)

tk.Label(root, text="Select Class:", font=font).grid(row=0, column=0, padx=20, pady=20)
class_var = tk.StringVar()
class_dropdown = ttk.Combobox(root, textvariable=class_var, values=[f"Class {i}" for i in range(1, 11)], font=font)
class_dropdown.grid(row=0, column=1, padx=20, pady=20)
class_dropdown.current(0)

tk.Label(root, text="Number of Questions:", font=font).grid(row=1, column=0, padx=20, pady=20)
num_questions_var = tk.IntVar()
num_questions_entry = tk.Entry(root, textvariable=num_questions_var, font=font)
num_questions_entry.grid(row=1, column=1, padx=20, pady=20)

tk.Label(root, text="Topic Name:", font=font).grid(row=2, column=0, padx=20, pady=20)
topic_name_var = tk.StringVar()
topic_name_entry = tk.Entry(root, textvariable=topic_name_var, font=font)
topic_name_entry.grid(row=2, column=1, padx=20, pady=20)

submit_button = tk.Button(root, text="Submit", font=font, command=handle_conversation)
submit_button.grid(row=3, column=0, columnspan=2, pady=20)

tk.Label(root, text="Output:", font=font).grid(row=4, column=0, padx=20, pady=20)
output_frame = tk.Frame(root)
output_frame.grid(row=4, column=1, padx=20, pady=20)

output_text = tk.Text(output_frame, wrap=tk.WORD, width=80, height=20, font=font, state=tk.DISABLED)
output_text.grid(row=0, column=0, sticky="nsew")

scrollbar = tk.Scrollbar(output_frame, command=output_text.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
output_text.config(yscrollcommand=scrollbar.set)

root.mainloop()
