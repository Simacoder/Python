import json
import difflib

# Load dictionary data from JSON file
def load_dictionary_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data

# Function to return definition of a word
def get_definition(word, dictionary):
    word = word.lower()
    if word in dictionary:
        return dictionary[word]
    else:
        # If word not found, suggest similar words
        similar_words = difflib.get_close_matches(word, dictionary.keys(), n=1, cutoff=0.8)
        if similar_words:
            suggestion = similar_words[0]
            suggestion_definition = dictionary[suggestion]
            return f"Word not found. Did you mean '{suggestion}'? Definition: {suggestion_definition}"
        else:
            return "Word not found."

# Main function
def main():
    dictionary = load_dictionary_data()
    while True:
        user_input = input("Enter a word to get its definition (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        definition = get_definition(user_input, dictionary)
        print(definition)

if __name__ == "__main__":
    main()