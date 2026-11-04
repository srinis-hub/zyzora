user = {
    "name": "sri j",
    "role": "GenAi Engineer",
    "experience" : 4
}

topics = ["AI", "Machine Learning", "flutter", "dart",'Python','C++']

question_no = 0
total_ques = 0

def increment_counter():
    global question_no
    global total_ques
    question_no += 1    
    total_ques += 1
    return question_no

def welcome_user(user_name):
    print(f"Welcome {user_name}, to the GenAi platform!")

def get_response(question):   
    question = question.lower()
    if "ai" in question:
        return "AI stands for Artificial Intelligence, which is the simulation of human intelligence in machines."
    elif "machine learning" in question:
        return "Machine Learning is a subset of AI that allows systems to learn and improve from experience without being explicitly programmed."
    elif "flutter" in question:
        return "Flutter is an open-source UI software development toolkit created by Google for building natively compiled applications for mobile, web, and desktop from a single codebase."
    elif "dart" in question:
        return "Dart is a programming language optimized for building mobile, desktop, server, and web applications. It is developed by Google and is used to build Flutter apps."
    elif "python" in question:
        return "Python is a high-level, interpreted programming language known for its simplicity and readability. It is widely used in various domains including web development, data science, and artificial intelligence."
    elif "c++" in question:
        return "C++ is a general-purpose programming language created by Bjarne Stroustrup as an extension of the C programming language. It is known for its performance and efficiency."
    else:
        return "I'm sorry, I don't have information on that topic."
    

print("Welcome to the GenAi platform!")

print(welcome_user(user["name"]))

print("Available topics for discussion:")
for topic in topics:
    print(f"- {topic}")

while True:
    question = input("ask a question (or type 'exit' to quit): ")
    if not question:
        print("Please enter a valid question.")
        continue
    if question.lower() == 'exit':
        print("Thank you for using the GenAi platform. Goodbye!")
        break
    answer = get_response(question)
    print(f"Zinda: {answer}")
    increment_counter()
    print(f"Total questions asked: {question_no}")

print (f"Total questions asked during this session: {total_ques}")