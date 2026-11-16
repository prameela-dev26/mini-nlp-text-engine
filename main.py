
# Mini NLP Text Understanding Engine
# Version 1: Rule-Based POS Tagger
# Version 2: Machine Learning POS Tagger

from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier


# ==========================================
# METHOD 1: RULE-BASED POS TAGGER
# ==========================================

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
print("\n========== METHOD 1: RULE-BASED POS TAGGER ==========")

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

print("\nNote: This is a dictionary-based POS tagger.")
print("It does not understand sentence context.")


# ==========================================
# METHOD 2: MACHINE LEARNING POS TAGGER
# ==========================================

# Step 1: Prepare labelled training data

training_sentences = [
    [
        ("I", "PRON"),
        ("play", "VERB"),
        ("cricket", "NOUN")
    ],
    [
        ("They", "PRON"),
        ("play", "VERB"),
        ("football", "NOUN")
    ],
    [
        ("She", "PRON"),
        ("reads", "VERB"),
        ("books", "NOUN")
    ],
    [
        ("The", "DET"),
        ("beautiful", "ADJ"),
        ("girl", "NOUN"),
        ("reads", "VERB"),
        ("a", "DET"),
        ("book", "NOUN")
    ]
]


# Step 2: Feature extraction function

def extract_features(words, index):

    previous_word = words[index - 1] if index > 0 else "<START>"

    next_word = words[index + 1] if index < len(words) - 1 else "<END>"

    return {
        "word": words[index],
        "previous_word": previous_word,
        "next_word": next_word
    }


# Step 3: Separate features and correct POS tags

X = []
y = []

for sentence_data in training_sentences:

    words = [word.lower() for word, tag in sentence_data]
    tags = [tag for word, tag in sentence_data]

    for i in range(len(words)):

        features = extract_features(words, i)

        X.append(features)
        y.append(tags[i])


# Step 4: Convert text features into numerical values

vectorizer = DictVectorizer()

X_vectorized = vectorizer.fit_transform(X)


# Step 5: Create and train the Decision Tree model

model = DecisionTreeClassifier(random_state=42)

model.fit(X_vectorized, y)


# Step 6: Predict POS tags for the input sentence

print("\n========== METHOD 2: MACHINE LEARNING POS TAGGER ==========")

new_words = sentence.lower().split()

for i in range(len(new_words)):

    features = extract_features(new_words, i)

    new_features_vectorized = vectorizer.transform([features])

    prediction = model.predict(new_features_vectorized)

    print(new_words[i], "->", prediction[0])


print("\nNote: This model learns from labelled training examples.")
