def get_response(question):
    return f"Zinda: You asked: {question}"


def save_conversation(question, response):
    with open("chat_history.txt", "a") as file:
        file.write(f"User: {question}\n")
        file.write(f"Zinda: {response}\n")


def show_history():
    with open("chat_history.txt", "r") as file:
        history = file.read()
        if history:
            print("\nConversation History:")
            print(history)
        else:
            print("\nNo conversation history found.")   

    pass


while True:
    question = input("You: ").strip()
    if question.lower() == "exit":
        break

    if not question:
        print("Please enter a valid question.")
        continue

    response = get_response(question)
    print(response)
    save_conversation(question, response)

show_history()