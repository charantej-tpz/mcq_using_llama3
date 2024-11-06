
import ollama

print("Welcome!!, Type 'exit' to quit")
while True:
    user_input = input("\nYou : ")
    if user_input == "exit":
        break
    output = ollama.generate(model="llama3", prompt=user_input,stream=True)
    print("Bot: ", end="")
    for chunk in output:
        print(chunk["response"], end='' , flush=True)

