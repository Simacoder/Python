import json
import difflib

def load_dictionary_from_json(json_data):
    return json.loads(json_data)

def get_word_definition(word, dictionary):
    # Convert the word to lowercase to handle case-insensitivity
    word = word.lower()
    
    # Check if the word exists in the dictionary
    if word in dictionary:
        return dictionary[word]
    else:
        # Get a list of closest matches for the misspelled word
        suggestions = difflib.get_close_matches(word, dictionary.keys(), n=3, cutoff=0.6)
        
        if suggestions:
            suggestion_str = ", ".join(suggestions)
            return f"No definition found for '{word}'. Did you mean: {suggestion_str}?"
        else:
            return f"No definition found for '{word}' and no similar words found."

# Example JSON data
json_data = '''
{
    "apple": "A fruit that grows on trees",
    "banana": "A fruit that grows on a banana plant",
    "orange": "A citrus fruit",
    "grape": "A small round fruit",
    "simanga": "Simanga is a student and your classmate"
}
'''

# Load the dictionary from JSON data
dictionary = load_dictionary_from_json(json_data)

# Example usage
word = input("Enter a word: ")
definition = get_word_definition(word, dictionary)
print("Definition:", definition)