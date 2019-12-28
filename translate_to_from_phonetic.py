def get_word_from_dict(word, dict):
    '''
    Receive a word string and a dict with the required mapping
    and return its counterpart word
    '''
    is_capital = word[0].isupper()
    
    # Is the word in the intended dictionary?
    if (word.lower() in dict):
        new_word = dict[word.lower()]
        
        # Does the word start with a capital letter?
        if is_capital:
            new_word = new_word[0].upper() + new_word[1:]
        return new_word

    else:
        return "<{}>".format(word)

def load_dict_file(filepath):
    '''
    Read the file with the traditional-to-phonetic dictionary and
    return its contents as a string
    '''
    with open(filepath, "r+") as file:
        trad_to_ebeo_str = file.read()
    return trad_to_ebeo_str
    
def convert_dict(dict_str):
    '''
    Receive a dictionary file string input and put it into 2 dictionaries:
    1 for traditional -> phonetic and another for phonetic -> traditional
    '''
    trad_to_ebeo_dict = {}
    ebeo_to_trad_dict = {}
    for entry in dict_str.split("\n"):

        # Process the line
        pair = entry.split(" = ")
        # Is it a valid word-pronunciation pair?
        if len(pair) >= 2:
            #print("{} ==== {}".format(pair[0].lower(), pair[1]))
            trad_to_ebeo_dict[pair[0].lower()] = pair[1]
            ebeo_to_trad_dict[pair[1]] = pair[0].lower()
    
    # Return new dictionary containing both dicts
    return {
        "to_ebeo": trad_to_ebeo_dict,
        "to_trad": ebeo_to_trad_dict,
    }

def convert_to_from_phonetic(input):
    output = ""
    for word in input.split(" "):
        output += get_word_from_dict(word, dict_content["to_ebeo"]) + " "
    return output


trad_to_ebeo_str = load_dict_file("trad_to_ebeo.txt")
dict_content = convert_dict(trad_to_ebeo_str)
input_str = "This is a test always a test Here's another sentence"
output_str = convert_to_from_phonetic(input_str)

print(output_str)
