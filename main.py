from services.ai import ask_ai


def main():
    print("🤖 Real Estate AI Agent is running...")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("AI: Goodbye 👋")
            break
        response = ask_ai(user_input)
        print("AI:", response)


if __name__ == "__main__":
    main()
