import time

print("Simple Chatbot (type 'exit' to stop)")

while True:
    user = input("You: ").lower()

    if "hello" in user:
        print("bot are typing...")
        time.sleep(2)
        print("Bot: Hi!")
    elif "how are you" in user:
        print("Bot: I'm fine!")
    elif "exit" == user:
        print("bot : good bye")
        break
    else:
        print("Bot: I don't understand")
