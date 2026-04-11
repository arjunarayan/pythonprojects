import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 180)
print("📊 Booting the Pokédex AI...")
engine.say("Booting the Pokédex AI...")
engine.runAndWait()
# 1. Update the filename
dataset_file = "pokemon.csv"
known_questions = []
known_answers = []

# --- 1. Train on Pokémon Data ---
try:
    with open(dataset_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # We treat the Pokemon Name as the "Question"
            name = row["Name"]
            known_questions.append(name)

            # We build a custom "Answer" string using the other columns
            types = f"{row['Type1']}"
            if row['Type2']:  # Check if there is a second type
                types += f" and {row['Type2']}"

            evolution_text = f"It evolves into {row['Evolution']}." if row[
                'Evolution'] else "It does not evolve further."

            answer = f"{name.capitalize()} is a {types} type Pokémon. {evolution_text}"
            known_answers.append(answer)

    print(f"Bot: Successfully indexed {len(known_questions)} Pokémon!")
except FileNotFoundError:
    print(f"Bot: ERROR! I need the '{dataset_file}' file to read!")
    engine.say(f"ERROR! I need the '{dataset_file}' file to read!")
    engine.runAndWait()
    exit()
except KeyError as e:
    print(f"Bot: Error in CSV headers! Looking for Name/Type1/Type2/Evolution. Missing: {e}")
    engine.say(f"Error in CSV headers! Looking for Name/Type1/Type2/Evolution. Missing: {e}")
    engine.runAndWait()
    exit()

# --- 2. Initialize the Machine Learning Brain ---
print("Bot: Generating vector embeddings...")
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(known_questions)
print("Bot: Pokedex logic initialized. Ask me about a Pokémon!")
engine.say("Pokédex logic initialized. Ask me about a Pokémon!")
engine.runAndWait()
# --- 3. Main Chat Loop ---
while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() in ["quit", "exit"]:
        print("Bot: Shutting down Pokedex. Goodbye!")
        engine.say("Shutting down Pokédex. Goodbye!")
        engine.runAndWait()
        break

    try:
        # Convert user text (e.g., "Tell me about Pikachu") to math
        user_vector = vectorizer.transform([user_input])

        # Compare user math to our list of Pokémon names
        similarity_scores = cosine_similarity(user_vector, question_vectors)

        best_match_index = similarity_scores.argmax()
        best_score = similarity_scores[0][best_match_index]

        # Confidence threshold (0.3 is usually good for keyword matching)
        if best_score > 0.3:
            print(f"Bot: {known_answers[best_match_index]}")
            engine.say(f"{known_answers[best_match_index]}")
            engine.runAndWait()
        else:
            print("Bot: I don't recognize that Pokémon. Check your spelling or try another one!")
            engine.say("I don't recognize that Pokémon. Check your spelling or try another one!")
            engine.runAndWait()
    except Exception as e:
        print(f"Bot: System Error: {e}")
        engine.say(f"Bot: System Error: {e}")
        engine.runAndWait()