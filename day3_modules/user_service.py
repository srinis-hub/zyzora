def get_user():
    return {
        "name": "Sri",
        "role": "Generative AI Engineer",
        "experience": 4
    }


def display_user(user):
    print(f"Name: {user['name']}")
    print(f"Role: {user['role']}")
    print(f"Experience: {user['experience']} years")