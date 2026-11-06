
# Mini NLP Text Understanding Engine
# Version 1: Rule-Based POS Tagger

# Step 1: Take input
sentence = input("Enter a sentence: ")

# Step 2: Tokenization
words = sentence.split()

# Step 3: Define word categories
verbs = {"eat", "eats", "run", "runs", "play", "plays", "read", "reads"}
nouns = {"dog", "food", "cat", "book", "girl", "ticket"}
adjectives = {"beautiful", "good", "bad", "big", "small", "happy"}
determiners = {"the", "a", "an", "this", "that"}

# Step 4: POS tagging
print("\nPOS Tagging Results:")

for word in words:
    if word.lower() in verbs:
        print(word, "-> Verb")

    elif word.lower() in nouns:
        print(word, "-> Noun")

    elif word.lower() in adjectives:
        print(word, "-> Adjective")

    elif word.lower() in determiners:
        print(word, "-> Determiner")

    else:
        print(word, "-> Unknown")


# Step 5: Explain the limitation
print("\nNote: This is a dictionary-based POS tagger.")
print("It does not understand sentence context.")
