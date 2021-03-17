import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(w):
    word = w.lower()
    proper_noun = w.title()
    acronym = w.upper()
    if word in data:
        return data[word]

    elif proper_noun in data:
        return data[proper_noun]
    
    elif acronym in data:
        return data[acronym]

    elif len(get_close_matches(w, data.keys())) > 0:
        confirm = input("Is the word you are looking for %s? Type Y or N for Yes or No:" % get_close_matches(w, data.keys())[0]) 
        if confirm == "Y":
            return data[get_close_matches(w, data.keys())[0]] 
        elif confirm == "N":
            word = input("Enter the Word again:")
            translate(word)    
        else: 
            return "The word is not in the query."
            
    else:
        return "the word you typed is spelt incorrectly or doesn't exist"

word = input("Enter word: ")

output = translate(word)

if type(output) == list:

    for item in output:
        print(item)
else:
    print(output)
