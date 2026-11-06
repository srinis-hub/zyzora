import utils
import api_client


def main():
    print("Welcome to Zinda API Integration Manager!")
    print("Type 'exit' to close the application.\n")

    while True:
        prompt = input("Enter a prompt: ").strip()

        if prompt.lower() == "exit":
            print("Exiting the program.")
            break

        if not prompt:
            print("Prompt cannot be empty.")
            continue

        request_payload = {
            "title": "GenAI Learning",
            "body": prompt,
            "userId": 1
        }

        response = api_client.create_post(request_payload)

        if response is None:
            print("API request failed. Conversation was not saved.")
            continue

        print("\nAPI Response:")
        print(f"ID: {response['id']}")
        print(f"Title: {response['title']}")
        print(f"Body: {response['body']}")

        utils.store_prompt_to_json(response)

    print("\nFinal Conversation History:")
    utils.print_history()


if __name__ == "__main__":
    main()