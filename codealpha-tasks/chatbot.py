def chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input in ["hi", "hello"]:
            print("Bot: Hi there!")
        elif user_input in ["how are you"]:
            print("Bot: I'm just a program, but I'm doing great 😄")
        elif user_input in ["bye", "exit"]:
            print("Bot: Goodbye! 👋")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()
