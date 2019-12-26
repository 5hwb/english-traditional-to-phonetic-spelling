def get_word_from_dict(word, dict):

    is_capital = word[0].isupper()
    
    # Is the word in the intended dictionary?
    if (word in dict):
        new_word = dict[word]
        if is_capital:
            new_word = new_word[0].toupper() + new_word[1:]
        return new_word

    else:
        return "<{}>".format(word)

# Open the file with the traditional-to-phonetic dictionary
with open('trad_to_ebeo.txt', "r+") as file:
    trad_to_ebeo_str = file.read()

# Put it into 2 dictionaries: 1 for traditional -> phonetic
# and another for phonetic -> traditional
trad_to_ebeo_dict = {}
ebeo_to_trad_dict = {}
for entry in trad_to_ebeo_str.split("\n"):

    # Process the line
    pair = entry.split(" = ")
    # Is it a valid word-pronunciation pair?
    if len(pair) >= 2:
        #print("{} ==== {}".format(pair[0].lower(), pair[1]))
        trad_to_ebeo_dict[pair[0].lower()] = pair[1]
        ebeo_to_trad_dict[pair[1]] = pair[0].lower()
    
input_str = "This is a test always a test"
output_str = ""
for word in input_str.split(" "):
    output_str += get_word_from_dict(word, trad_to_ebeo_dict) + " "

print(output_str)
