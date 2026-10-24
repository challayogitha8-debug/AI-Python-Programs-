
import random
greetings = ['hello', 'hi', 'hey']
greeting_responses = ['Hello!', 'Hi there!', 'Hey!']
questions = ['how are you', 'how is your day', 'what are you doing']

question_responses = [
    'I am doing well!',
    'My day is going great!',
    'I am just chatting with you.'
]

goodbyes = ['bye', 'goodbye', 'see you later']

goodbye_responses = ['Goodbye!', 'See you later!', 'Take care!']

def chatbot(input_string):
    input_string = input_string.lower().strip()

    for word in greetings:
        if word in input_string.split():
            return random.choice(greeting_responses)

    for question in questions:
        if question in input_string:
            return question_responses[questions.index(question)]

    for word in goodbyes:
        if word in input_string:
            return random.choice(goodbye_responses)

    return "I'm sorry, I don't understand. Can you please rephrase that?"

while True:
    user_input = input("You: ")

    if user_input.lower().strip() in ['exit', 'quit']:
        print("Chatbot: Goodbye!")
        break

    response = chatbot(user_input)
    print("Chatbot:", response)

