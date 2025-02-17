import itertools
import random

ASCII_ART = """8888888888888888888888888888888888888888888888888888888888888888888888
8888888888888888888888888888888888888888888888888888888888888888888888
888888888888888888888888888888P""  ""988888888888888888888888888888888
888888888888888888888P"88888P          988888"988888888888888888888888
888888888888888888888  "9888            888P"  88888888888888888888888
88888888888888888888888bo "9  d8o  o8b  P" od8888888888888888888888888
88888888888888888888888888bob 98"  "8P dod8888888888888888888888888888
88888888888888888888888888888    db    8888888888888888888888888888888
8888888888888888888888888888888      888888888888888888888888888888888
8888888888888888888888888888P"9bo  odP"9888888888888888888888888888888
8888888888888888888888888P" od88888888bo "9888888888888888888888888888
88888888888888888888888   d88888888888888b   8888888888888888888888888
888888888888888888888888oo8888888888888888oo88888888888888888888888888
8888888888888888888888888888888888888888888888888888888888888888888888"""

def welcome_screen():
    """Displays a welcome screen with ASCII art and some nice formatting."""
    print("\n" + "="*70)
    print(" "*18 + "WELCOME TO THE WORDLIST GENERATOR")
    print("-"*70)
    print(ASCII_ART)
    print("-"*70)
    print(" "*7 + "This tool lets you create wordlists based on user input!")
    print(" "*17 + "Program created by: Benjamin Barish")
    print("="*70)

def leetspeak(word):
    leet_dict = {'a': ['a', '@', '4'], 'b': ['b', '8'], 'e': ['e', '3'], 'i': ['i', '1', '!'], 'l': ['l', '1', '|'], 'o': ['o', '0'], 's': ['s', '$', '5'], 't': ['t', '7']}
    return {''.join(p) for p in itertools.product(*[leet_dict.get(c.lower(), [c]) for c in word])}

def generate_variations(word):
    variations = {word.lower(), word.upper(), word.capitalize()}
    variations.update(leetspeak(word))
    variations.update(generate_mutations(word))
    return variations

def generate_mutations(word):
    mutations = {'123', '!', '@', '2024', '#', '%'}
    return {word + m for m in mutations} | {m + word for m in mutations}

def generate_wordlist(words, target_length):
    wordlist = set()

    # Generate variations for each individual word
    for word in words:
        wordlist.update(generate_variations(word))

    # Generate multi-word combinations
    multi_word_combinations = set()
    for size in range(2, len(words) + 1):
        for combo in itertools.permutations(words, size):
            combined = ''.join(combo)
            multi_word_combinations.add(combined)
            multi_word_combinations.update(generate_variations(combined))
    
    # Add multi-word combinations to the wordlist
    wordlist.update(multi_word_combinations)

    # Return a random sample from the complete wordlist
    return random.sample(list(wordlist), min(len(wordlist), target_length))

def append_to_wordlist(wordlist, filename="generated_wordlist.txt"):
    with open(filename, "a") as file:
        file.write("\n".join(wordlist) + "\n")
    print(f"Wordlist appended to {filename} with {len(wordlist)} entries.")

# Main loop for generating wordlists
while True:
    welcome_screen()
    print("Enter words (type 'DONE' when finished):")
    user_words = []
    while (word := input("Enter a word: ")) != "DONE":
        user_words.append(word)

    # Validate wordlist length input
    while True:
        try:
            list_length = int(input("Enter the desired wordlist length: "))
            if list_length > 0:
                break
            else:
                print("Please enter a number greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    wordlist = generate_wordlist(user_words, list_length)

    append_to_wordlist(wordlist)

    # Ask if the user wants to go again
    continue_choice = input("Would you like to generate another wordlist? (yes/no): ").strip().lower()
    if continue_choice != "yes":
        break

print("Goodbye!")