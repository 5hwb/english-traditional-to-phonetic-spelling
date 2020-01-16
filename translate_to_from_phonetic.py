import re
from file_io import load_file_to_str

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

def convert_to_from_phonetic(input, dict_mapping):
    '''
    Translate a string of text in 1 orthography into the other one.
    dict_mapping is a dictionary that contains the appropriate mappings. 
    '''
    regex_format = "['a-zāàéèŧēúíòōáśđŵĝĥùūóźŋâA-ZĀÀÉÈŦĒÚÍÒŌÁŚĐŴĜĤÙŪÓŹŊÂ]"
    regex_prog = re.compile(regex_format)
    output = ""

    word_start = -1 # Index of the 1st char in the word
    word_end = -1 # Index of the last char in the word
    recording_word = False # True if the current char is part of a word. Used to help extract individual words
    has_start_quotemark = False
    has_end_quotemark = False

    for i in range(0, len(input)):
        is_match = regex_prog.match(input[i])
        #print("CHAR={}".format(char))

        # Is the current char a letter of a word?
        if is_match:
            #print("{} {} MATCH FOUN.".format(char, i))
            if not recording_word:
                word_start = i
                recording_word = True

                # Check if word starts with quotation mark.
                if input[word_start] == "'":
                    has_start_quotemark = True
                    word_start += 1

        # Otherwise, slice the word off the input using the recorded indexes
        else:
            #print("{} {} END OF WORD?".format(char, i))
            if recording_word:
                word_end = i

                # Check if word ends with quotation mark.
                if input[word_end-1] == "'":
                    has_end_quotemark = True
                    word_end -= 1

                word = input[word_start:word_end]
                #print("start={} end={} word={}".format(word_start, word_end, word))

                # Append output
                output += "'" if has_start_quotemark else ""
                output += get_word_from_dict(word, dict_mapping)
                output += "'" if has_end_quotemark else ""

                # Reset everything
                word_start = -1
                word_end = -1
                recording_word = False
                has_start_quotemark = False
                has_end_quotemark = False

            # Append the non-letter punctuation
            output += input[i]

        #print("OUTPUT: {}".format(output))

    # Handle case where the last word goes to the end of the text
    if recording_word:
        word_end = len(input)

        # Check if word ends with quotation mark.
        if input[word_end-1] == "'":
            has_end_quotemark = True
            word_end -= 1

        word = input[word_start:word_end]
        #print("start={} end={} word={}".format(word_start, word_end, word))

        # Append output
        output += "'" if has_start_quotemark else ""
        output += get_word_from_dict(word, dict_mapping)
        output += "'" if has_end_quotemark else ""

    return output


trad_to_ebeo_str = load_file_to_str("trad_to_ebeo.txt")
dict_content = convert_dict(trad_to_ebeo_str)
input_str = """'This is a test, always a 'test'. Here's another sentence for 'tests'"""
output_str = convert_to_from_phonetic(input_str, dict_content["to_ebeo"])
output_str2 = convert_to_from_phonetic(output_str, dict_content["to_trad"])

print(output_str)
print(output_str2)
