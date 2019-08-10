import json
from difflib import get_close_matches
data = json.load(open("data1.json"))


def meaning(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s ? Enter (Y) or (N). " % get_close_matches(w, data.keys())[0]).upper()
        if yn == "Y":
            return meaning(get_close_matches(w, data.keys())[0])
        elif yn == "N":
            return "No word found"
        else:
            return "Incorrect input"

    else:
        return "No word found"


word = input("Enter a word: ")
output = meaning(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
