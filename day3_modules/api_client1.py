import requests

def get_data_from_api(id):
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  
        data = response.json()
        return data
    except requests.exceptions.Timeout:
        print("Request timed out.")
    except requests.exceptions.ConnectionError:
        print("Unable to connect to the server.")
    except requests.exceptions.HTTPError as error:
        print(f"HTTP error: {error}")
    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")

    return None

 



    # response = requests.get(url, timeout=10)

    # print(f"Status Code: {response.status_code}")

    # if response.status_code == 200:
    #     data = response.json()
    #     return data
    # else:
    #     return None
    
post = get_data_from_api(1)

if post:
    print("Post Data:")
    print(f"User ID: {post['userId']}")
    print(f"ID: {post['id']}")
    print(f"Title: {post['title']}")
    print(f"Body: {post['body']}")
  
def create_post(title, body, user_id):
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": title,
        "body": body,
        "userId": user_id
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.Timeout:
        print("Request timed out.")
    except requests.exceptions.ConnectionError:
        print("Unable to connect to the server.")
    except requests.exceptions.HTTPError as error:
        print(f"HTTP error: {error}")
    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")

    return None
    
post1 = create_post("Learning Generative AI", "I am learning Python REST API integration.", 1)

if post1:
    print("Created Post Data:")
    print(f"User ID: {post1['userId']}")
    print(f"ID: {post1['id']}")
    print(f"Title: {post1['title']}")
    print(f"Body: {post1['body']}")