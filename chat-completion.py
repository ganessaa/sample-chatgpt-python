import os
import openai
import sys

openai.api_key = os.getenv("OPENAI_API_KEY")

MODEL_ENGINE = "gpt-3.5-turbo"
AI_FEATURES = "You are a helpful assistant."
messages = [{"role": "system", "content": AI_FEATURES}]

while True:
    # Get user input
    user_input = input("You: ")

    # Exit if user input is bye
    if user_input == "bye":
        print("AI: bye")
        sys.exit()

    # Add user input to messages
    messages.append({"role": "user", "content": user_input})

    # Get AI Response
    completion = openai.ChatCompletion.create(
        model=MODEL_ENGINE,
        messages=messages
    )

    # Show AI Response
    print("AI: " + completion.choices[0].message.content)

    # Add AI responses to messages
    messages.append(completion.choices[0].message)
