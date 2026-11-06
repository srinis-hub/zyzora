
import json

conversation = [
    {
        "role": "user",
        "message": "What is Generative AI?"
    },
    {
        "role": "assistant",
        "message": "Generative AI creates new content."
    }
]

with open("history.json", "w") as file:
    json.dump(conversation, file, indent=4)

print("Conversation saved successfully.")

try:
    with open("history.json", "r") as file:
        history = json.load(file)

    for message in history:
        print(message["role"], ":", message["message"])

except FileNotFoundError:
    print("History file not found.")

except json.JSONDecodeError:
    print("Invalid JSON format. History file may be corrupted.")
