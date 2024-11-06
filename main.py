
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import time


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
    print("Welcome!!! Type 'exit' to quit.")
    while True:
        start_time = time.time()
        user_input = input("You: ")
        if user_input == 'exit':
            break
        result =chain.invoke({'context': context, 'question': user_input})
        end_time = time.time()
        total_time = end_time - start_time
        print("Bot  : ",result ,"\n")
        print(f"Time taken : {total_time}")
        print("\n")
        context+= f"\nUser: {user_input}\nAI: {result}"

if __name__ == '__main__':
    handle_conversation()






