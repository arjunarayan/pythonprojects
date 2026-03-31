import json
import os

print("🐘 Booting Elephant Bot...")

profile_file = "user_profile.json"

# --- 1. Load Memory if it exists ---
if os.path.exists(profile_file):
    with open(profile_file, "r") as file:
        user_profile = json.load(file)
    print(f"Bot: Welcome back, {user_profile['name']}! I remember your favorite color is {user_profile['color']}.")
else:
    # If it's a new user, create an empty profile
    user_profile = {"name": None, "color": None}
    print("Bot: Hello stranger! I don't think we have met.")

# --- 2. Main Chat Loop ---
while True:
    user_input = input("You: ").strip().lower()
    # --- check if the user enters "quit". if they do, break the loop.
    if user_input == "quit":
        print("Bot: Goodbye! I will remember you next time.")
        break
    # --- check if user gives his/her name
    elif "my name is" in user_input:
        # Extract the name from the sentence
        name = user_input.replace("my name is", "").strip().capitalize()
        user_profile["name"] = name

        # Save to the hard drive immediately
        with open(profile_file, "w") as file:
            json.dump(user_profile, file, indent=4)

        print(f"Bot: Nice to meet you, {name}! I have saved that to my hard drive.")

    elif "my favorite color is" in user_input:
        color = user_input.replace("my favorite color is", "").strip()
        user_profile["color"] = color

        with open(profile_file, "w") as file:
            json.dump(user_profile, file, indent=4)

        print(f"Bot: {color.capitalize()} is a great color. Memory updated!")

    elif user_input == "who am i?":
        if user_profile["name"]:
            print(f"Bot: You are {user_profile['name']}!")
        else:
            print("Bot: I don't know yet! Tell me 'my name is [your name]'.")

    else:
        print("Bot: Try telling me your name or your favorite color!")