import json
import os
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 160)
import time


engine.say("Student bot loading...")
engine.runAndWait()

brain_file = "brain.json"

if os.path.exists(brain_file):
    with open(brain_file, "r") as file:
        brain = json.load(file)

    engine.say("Bot: Memory thingamajig loaded.")
    engine.runAndWait()
else:
    brain = {
        "hello" : "Hello dude.",
        "who are you" : "I'm a bot that learns",
        "fav food":"I love the mac M5 chip... and pizza"
    }

    engine.say("Initializing 10%")
    engine.runAndWait()
    engine.say("Initializing 30%")
    engine.runAndWait()
    engine.say("Initializing 50%")
    engine.runAndWait()
    engine.say("Initializing 80%")
    engine.runAndWait()
    engine.say("Initialized")
    engine.runAndWait()

while 1+1 > 1:
    user_input = input("\nYou: ").strip().lower()

    if user_input in ["quit", "exit"]:
        engine.say("Saving my memory thingamajigs")
        engine.runAndWait()
        break

    found_answer = False

    for known_phrase in brain:
        if known_phrase in user_input:
            engine.say(str(brain[known_phrase]))
            engine.runAndWait()


            found_answer = True

    if not found_answer:
        print("Bot: Hmm, I don't know how to respond to that.")
        engine.say(f"Hmm, I don't know how to respond to that.")
        engine.runAndWait()
        engine.say("What should I say when you talk about that?")
        engine.runAndWait()
        engine.say("Teach me:")
        engine.runAndWait()
        new_answer = input("Bot: What should I say when you talk about that?"
                           "\nTeach me: ")


        brain[user_input] = new_answer

    with open(brain_file, "w") as file:
        json.dump(brain, file, indent=4)
    print("Bot: Awesome! I've permanently added that to my brain.")
    # engine.say("Awesome! I've permanently added that to my brain.")
    # engine.runAndWait()
