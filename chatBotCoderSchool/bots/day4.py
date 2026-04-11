import csv

import pyttsx3
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
engine = pyttsx3.init()
engine.setProperty('rate', 180)
print("🌐 Booting the Multi-Tool Connected Assistant...")
engine.say("Booting the Multi-Tool Connected Assistant...")
engine.runAndWait()

# --- 1. THE API TOOLKIT ---

def fetch_live_joke():
    try:
        print("Bot: Searching the internet for a joke...")
        response = requests.get("https://official-joke-api.appspot.com/random_joke", timeout=5)
        data = response.json()
        return f"{data['setup']} ... {data['punchline']}"
    except:
        return "My internet connection failed!"

def fetch_cat_fact():
    try:
        print("Bot: Consulting the internet felines...")
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        data = response.json()
        return data['fact']
    except:
        return "Meow... I couldn't reach the cat servers!"


def fetch_pokemon_data(pokemon_name):
    try:
        print(f"Bot: Searching the Pokedex for {pokemon_name}...")
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}", timeout=5)

        # PokeAPI returns a 404 error if the name is spelled wrong
        if response.status_code == 404:
            return f"I couldn't find a Pokemon named {pokemon_name}. Check your spelling!"

        data = response.json()

        # Digging into the nested JSON dictionary
        weight = data['weight'] / 10  # Convert to kg
        base_experience = data['base_experience']

        return f"{pokemon_name.capitalize()} weighs {weight}kg and has a base XP of {base_experience}!"
    except:
        return "Pokedex connection error!"


# --- 2. LOAD THE CSV DATASET ---
dataset_file = "dataset.csv"
known_questions = []
known_answers = []

try:
    with open(dataset_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            known_questions.append(row["Question"])
            known_answers.append(row["Answer"])

    vectorizer = TfidfVectorizer()
    question_vectors = vectorizer.fit_transform(known_questions)
    print("Bot: Online and ready! Ask me a question, or ask for a joke, a cat fact, or Pokemon stats!")
except FileNotFoundError:
    print("Bot: ERROR! Missing 'dataset.csv'.")
    exit()

# --- 3. MAIN CHAT LOOP ---
while True:
    user_input = input("\nYou: ").strip().lower()

    if user_input in ["quit", "exit"]:
        print("Bot: Disconnecting from the mainframe. Bye!")
        break

    # --- API OVERRIDE CHECKS ---

    # 1. Joke API Check
    if "joke" in user_input:
        joke = fetch_live_joke()
        print("Bot: " + joke)
        engine.say(joke)
        engine.runAndWait()
        continue

        # 2. Cat Fact API Check
    elif "cat fact" in user_input:
        fact = fetch_cat_fact()
        print(f"Bot: " + fact)
        engine.say(fact)
        engine.runAndWait()
        continue

    # 3. PokeAPI Check (Looking for a trigger word and the Pokemon name)
    elif "pokemon" in user_input:
        # Split the sentence into words to grab the last word (the name)
        words = user_input.split()
        if len(words) > 1:
            pokemon_name = words[-1]  # Grabs the last item in the list
            print(f"Bot: {fetch_pokemon_data(pokemon_name)}")
            engine.say(fetch_pokemon_data(pokemon_name))
            engine.runAndWait()
        else:
            print("Bot: Which Pokemon? Try typing 'pokemon pikachu'.")
        continue

    # --- STANDARD AI LOGIC ---
    try:
        user_vector = vectorizer.transform([user_input])
        similarity_scores = cosine_similarity(user_vector, question_vectors)

        best_match_index = similarity_scores.argmax()
        best_score = similarity_scores[0][best_match_index]

        if best_score > 0.3:
            print(f"Bot: {known_answers[best_match_index]}")
        else:
            print("Bot: I don't know that one. Ask me for a joke, cat fact, or Pokemon stats!")

    except Exception as e:
        print(f"Bot: I need more training data! Error: {e}")