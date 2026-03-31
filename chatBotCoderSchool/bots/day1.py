import json
import os
from os import name

print("🐘Booting Elephant Bot...")

profile_file = "user_profile.json"

if os.path.exists(profile_file):
    with open(profile_file, "r") as file:
        user_profile = json.load(file)
    print(f"Bot: Welcome back, {user_profile["name"]} I remember your favorite color"
          f"is {user_profile["color"]}")
else:
    user_profile = {"name": None, "color": None}
    print("Bot: Hello! I don't think we have met. Although the only way I will know about you is a json file.")
while 1==1:
    user_input = input("You: ")

    if user_input == "Goodbye!":
        print("Bot: Goodbye! I will remember you next time.")
        break
    elif "my name is" in user_input:
        name = user_input.replace("my name is", "").strip().capitalize()
        user_profile["name"] = name

        with open(profile_file, "w") as file:
            json.dump(user_profile, file, indent=4)

        print(f"Bot: Nice to meet you, {name}! I have told Mr. JSON all about it.")
    elif "my favorite color is" in user_input:
        color = user_input.replace("my favorite color is", "").strip().capitalize()
        user_profile["color"] = color

        with open(profile_file, "w") as file:
            json.dump(user_profile, file, indent=4)

        print(f"Bot: {color.capitalize()} is a great color! I have told Mr. JSON all about it.")
    elif user_input == "who am i":
        if user_profile["name"] is not None:
            print(f"Bot: I'm surprised you don't your own name but it's {str(user_profile[name])}")
        else:
            print(f"I can't tell you your name if you never told me! And anyway, you should know your own name!!!")
    else:
        print("Tell me name or favorite color")
