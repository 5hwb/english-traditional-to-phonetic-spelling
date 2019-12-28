import re

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

def convert_to_from_phonetic(input, to_phonetic=True):
    regex_format = "['a-zāàéèŧēúíòōáśđŵĝĥùūóźŋâA-ZĀÀÉÈŦĒÚÍÒŌÁŚĐŴĜĤÙŪÓŹŊÂ]"
    regex_prog = re.compile(regex_format)
    output = ""
    dict_to_call = "to_ebeo" if to_phonetic else "to_trad"
    
    word_start = -1 # Index of the 1st char in the word
    word_end = -1 # Index of the last char in the word
    recording_word = False # True if 
    
    for i in range(0, len(input)):
        char = input[i]
        is_match = regex_prog.match(char)
        #print("CHAR={}".format(char))
        
        # Is the current char a letter of a word?
        if is_match:
            #print("{} {} MATCH FOUN.".format(char, i))
            if not recording_word:
                word_start = i
                recording_word = True
        
        # Otherwise, slice the word off the input using the recorded indexes 
        else:
            #print("{} {} END OF WORD?".format(char, i))
            if recording_word:
                word_end = i
                
                word = input[word_start:word_end]
                #print("start={} end={} word={}".format(word_start, word_end, word))

                # Append output            
                output += get_word_from_dict(word, dict_content[dict_to_call])
                
                # Reset everything
                word_start = -1
                word_end = -1
                recording_word = False
            
            # Append the non-letter punctuation
            output += input[i]

        #print("OUTPUT: {}".format(output))
    
    # Handle case where the last word goes to the end of the text
    if recording_word:
        word = input[word_start:len(input)]
        #print("start={} end={} word={}".format(word_start, word_end, word))

        # Append output            
        output += get_word_from_dict(word, dict_content[dict_to_call])

    return output


trad_to_ebeo_str = load_dict_file("trad_to_ebeo.txt")
dict_content = convert_dict(trad_to_ebeo_str)
input_str = "This is a test, always a test. Here's another sentence"
output_str = convert_to_from_phonetic(input_str, True)
output_str2 = convert_to_from_phonetic(output_str, False)

print(output_str)
print(output_str2)
