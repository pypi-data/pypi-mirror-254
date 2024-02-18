import os
import markdown
import json

def fill_gaps_with_underscore(string):
    # Split the string by spaces
    words = string.split()

    # Create a new list to store the modified words
    modified_words = []

    # Iterate over each word
    for word in words:
        # If the word has gaps (multiple consecutive underscores), replace them with a single underscore
        modified_word = word.replace('_', ' ')
        modified_word = modified_word.replace(' ', '_')

        # Add the modified word to the list
        modified_words.append(modified_word)

    # Join the modified words back into a string with spaces
    filled_string = ' '.join(modified_words)

    return filled_string