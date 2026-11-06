import json
import os

HISTORY_FILE = "history.json"

def store_prompt_to_json(values):
    try:
        # Read existing conversation history
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as file:
                history = json.load(file)

            if not isinstance(history, list):
                raise ValueError("History must contain a JSON array.")

        except FileNotFoundError:
            history = []

        except json.JSONDecodeError:
            print("History file is corrupted. Cannot append safely.")
            return

        # Add the new conversation
        history.append(values)

        # Write to a temporary file
        temp_file = HISTORY_FILE + ".tmp"

        with open(temp_file, "w", encoding="utf-8") as file:
            json.dump(history, file, indent=4)

        # Replace original file
        os.replace(temp_file, HISTORY_FILE)

        print("Conversation saved successfully.")

    except (OSError, TypeError, ValueError) as error:
        print(f"Unable to save conversation: {error}")


def print_history():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            history = json.load(file)

        if not history:
            print("No conversation history found.")
            return

        print("\nConversation History:")

        for message in history:
            print(json.dumps(message, indent=4))

    except FileNotFoundError:
        print("History file not found.")

    except json.JSONDecodeError:
        print("Invalid JSON format. History file may be corrupted.")