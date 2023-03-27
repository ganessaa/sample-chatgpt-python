import os
import openai
import sys

openai.api_key = os.getenv("OPENAI_API_KEY")
MODEL_ENGINE = "text-davinci-003"


def generate_response(prompt):
    response = openai.Completion.create(
        engine=MODEL_ENGINE,
        prompt=prompt,
        max_tokens=1024,
        stop=None,
        temperature=0.6,
    )
    message = response.choices[0].text.strip()
    return message


while True:
    # Get user input
    user_input = input("You: ")

    # Exit if user input is bye
    if user_input == "bye":
        print("AI: bye")
        sys.exit()

    # Get AI Response
    response = generate_response(user_input)

    # Show AI Response
    print("AI: " + response)
