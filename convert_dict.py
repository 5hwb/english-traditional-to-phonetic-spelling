import re

# This script creates a dictionary that maps traditional words to EBEO ones.
# The output is called 'trad_to_ebeo.txt'.
# CMUdict obtained from here: https://stackoverflow.com/questions/3794454/where-can-i-obtain-an-english-dictionary-with-structured-data

# Map CMUdict notation to EBEO letters
cmudict_to_ebeo = {
    "OA": "o", "OA0": "e", "OA1": "o", "OA2": "o",
    "AA": "a", "AA0": "e", "AA1": "a", "AA2": "a",
    "AE": "á", "AE0": "e", "AE1": "á", "AE2": "á",
    "AH": "a", "AH0": "e", "AH1": "a", "AH2": "a",
    "AO": "ó", "AO0": "ó", "AO1": "ó", "AO2": "ó",
    "AW": "à", "AW0": "à", "AW1": "à", "AW2": "à",
    "AY": "ā", "AY0": "ā", "AY1": "ā", "AY2": "ā",
    "B": "b",
    "CH": "c",
    "D": "d",
    "DH": "đ",
    "EH": "é", "EH0": "é", "EH1": "é", "EH2": "é",
    "ER": "er", "ER0": "er", "ER1": "er", "ER2": "er",
    "EY": "ē", "EY0": "ē", "EY1": "ē", "EY2": "ē",
    "F": "f",
    "G": "g",
    "HH": "h",
    "IH": "i", "IH0": "i", "IH1": "i", "IH2": "i",
    "IY": "í", "IY0": "i", "IY1": "í", "IY2": "í",
    "JH": "j",
    "K": "k",
    "L": "l",
    "M": "m",
    "N": "n",
    "NG": "ŋ",
    "OW": "ò", "OW0": "ò", "OW1": "ò", "OW2": "ò",
    "OY": "ō", "OY0": "ō", "OY1": "ō", "OY2": "ō",
    "P": "p",
    "R": "r",
    "S": "s",
    "SH": "ś",
    "T": "t",
    "TH": "ŧ",
    "UH": "u", "UH0": "u", "UH1": "u", "UH2": "u",
    "UW": "ú", "UW0": "ú", "UW1": "ú", "UW2": "ú",
    "V": "v",
    "W": "w",
    "Y": "y",
    "Z": "z",
    "ZH": "ź",
}

def cmudict_entry_to_word(entry):
    '''
    Convert a CMUdict pronunciation entry (e.g. 'S AO1 NG' for 'song')
    into a word spelt in EBEO orthography (e.g. 'sóŋ').
    '''
    new_word = ""
    for phoneme in entry.split(" "):
        new_word += cmudict_to_ebeo[phoneme]

    # Fix certain sequences to correct pronunciation
    new_word = new_word.replace("ór", "or")

    return new_word

def load_dict_file(filepath):
    '''
    Read the dictionary file and return its contents as a string
    '''
    with open(filepath, "r+", encoding="utf-8") as file:
        trad_to_ebeo_str = file.read()
    return trad_to_ebeo_str

def save_dict_file(filepath, dict):
    '''
    Write the dictionary contents to a file
    '''
    with open(filepath, "w+", encoding="utf-8") as file:
        file.write(dict)

def convert_dict(dict):
    '''
    Convert the CMUdict dictionary into a mapping
    from traditional English spelling to phonetic spelling
    '''
    dict_converted = ""
    for line in dict.split("\n"):
        # Skip comments
        if (line[0:3] == ";;;"):
            continue

        # Process the line
        pair = line.split("  ")
        # Is it a valid word-pronunciation pair?
        if len(pair) >= 2:
            dict_converted += "{} = {}".format(pair[0],
                    cmudict_entry_to_word(pair[1])) + "\n"
        else:
            dict_converted += "{} = nothing".format(pair[0]) + "\n"

    return dict_converted

def clean_up_pronunciations(dict):
    '''
    Change the pronunciations to fit the EBEO orthographical conventions.
    '''
    #dict = dict.replace("o", "qqZZqq")
    dict = re.sub(r"S = (.+)z\n", r"S = \1s\n", dict) # Replace phonetic -z (plural or case suffix at the end of word) with -s
    return dict

# Open the file with the dictionary
cmudict = load_dict_file("cmudict-no-merger/cmudict-0.7b-no-merger")
# Go thru the file
cmudict_converted = convert_dict(cmudict)
cmudict_converted = clean_up_pronunciations(cmudict_converted)
# Write the converted dict to file
save_dict_file("trad_to_ebeo.txt", cmudict_converted)
