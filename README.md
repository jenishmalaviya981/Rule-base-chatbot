# Rule-base-chatbot
Tools: Python only  , Idea -   Chatbot that answers basic questions like:  "hello" → "Hi!"  , "how are you?" → "I'm fine" ,Concepts:  if-else, string handling

# CODE OF Chatbot 

import time
while True:
    user = input("You: ").lower()

    if "hello" in user:
        print("bot are typing...")
        time.sleep(2)
        print("Bot: Hi!")
    elif "how are you" in user:
        print("bot are typing...")
        time.sleep(2)
        print("Bot: I'm fine!")
    elif "bye" in user:
        print("bot are typing...")
        time.sleep(2)
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I don't understand")
