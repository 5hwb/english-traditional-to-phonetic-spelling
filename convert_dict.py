# This script creates a dictionary that maps traditional words to EBEO ones.
# The output is called 'trad_to-ebeo.txt'.

# Map CMUdict notation to EBEO letters
cmudict_to_ebeo = {
    "AA": "o", "AA0": "e", "AA1": "o", "AA2": "o",
    "AE": "á", "AE0": "e", "AE1": "á", "AE2": "á",
    "AH": "a", "AH0": "e", "AH1": "a", "AH2": "a",
    "AO": "ó", "AO0": "e", "AO1": "ó", "AO2": "ó",
    "AW": "à", "AW0": "e", "AW1": "à", "AW2": "à",
    "AY": "ā", "AY0": "e", "AY1": "ā", "AY2": "ā",
    "B": "b",
    "CH": "c",
    "D": "d",
    "DH": "đ",
    "EH": "é", "EH0": "e", "EH1": "é", "EH2": "é",
    "ER": "er", "ER0": "er", "ER1": "er", "ER2": "er",
    "EY": "ē", "EY0": "e", "EY1": "ē", "EY2": "ē",
    "F": "f",
    "G": "g",
    "HH": "h", "HH0": "e", "HH1": "h", "HH2": "h",
    "IH": "i", "IH0": "i", "IH1": "i", "IH2": "i",
    "IY": "í", "IY0": "i", "IY1": "í", "IY2": "í",
    "JH": "j",
    "K": "k",
    "L": "l",
    "M": "m",
    "N": "n",
    "NG": "ŋ",
    "OW": "ò", "OW0": "e", "OW1": "ò", "OW2": "ò",
    "OY": "ō", "OY0": "e", "OY1": "ō", "OY2": "ō",
    "P": "p",
    "R": "r",
    "S": "s",
    "SH": "ś",
    "T": "t",
    "TH": "ŧ",
    "UH": "u", "UH0": "e", "UH1": "u", "UH2": "u",
    "UW": "ú", "UW0": "e", "UW1": "ú", "UW2": "ú",
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
    
    return new_word

# Open the file with the dictionary
with open('cmudict/cmudict-0.7b', "r+") as file:
    cmudict = file.read()

# Go thru the file
for line in cmudict.split("\n"):
    # Skip comments
    if (line[0:3] == ";;;"):
        continue
        
    # Process the line
    pair = line.split("  ")
    # Is it a valid word-pronunciation pair?
    if len(pair) >= 2:
        print("{} = {}".format(pair[0],
                cmudict_entry_to_word(pair[1])))
    else:
        print("{} = nothing".format(pair[0]))

