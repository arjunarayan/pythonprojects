import os
import json
from groq import Groq

# REMINDER: Paste your TEMPORARY workshop API key here before class!
client = Groq(api_key="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")
history_file = "chat_history.json"

print("⚡ Booting the Groq AI Assistant...")

# --- THE MEMORY SYSTEM ---
system_instruction = {
    "role": "system",
    "content": "be nice!!!"
}

# 1. Try to load the saved transcript from the hard drive
if os.path.exists(history_file):
    with open(history_file, "r") as file:
        chat_history = json.load(file)
    print("Bot: Neural pathways reconnected. I remember our past conversations!")
else:
    # 2. If no file exists, start fresh with the system instructions
    chat_history = [system_instruction]
    print("Bot: System initialized. Hello, new friend!")

# --- THE CHAT LOOP ---
while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() in ["quit", "exit"]:
        print("Bot: Powering down. Your memories are safely stored on the hard drive.")
        break

    # Append the user's message
    chat_history.append({"role": "user", "content": user_input})

    try:
        # Ask Groq (Using the latest Llama 3.1 model)
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=chat_history
        )

        # Extract and print the reply
        bot_reply = response.choices[0].message.content
        print(f"\nBot: {bot_reply}")

        # Append the bot's reply to the transcript
        chat_history.append({"role": "assistant", "content": bot_reply})

        # 3. SAVE TO JSON: Overwrite the hard drive file with the updated transcript
        with open(history_file, "w") as file:
            json.dump(chat_history, file, indent=4)

    except Exception as e:
        print(f"Bot: Whoops! My neural connection dropped. Error: {e}")