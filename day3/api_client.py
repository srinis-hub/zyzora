import requests


def create_post(payload):
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.post(
            url,
            json=payload,
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.Timeout:
        print("Request timed out.")

    except requests.exceptions.ConnectionError:
        print("Unable to connect to the server.")

    except requests.exceptions.HTTPError as error:
        print(f"HTTP error: {error}")

    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")

    return None