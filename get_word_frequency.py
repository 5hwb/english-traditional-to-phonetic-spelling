import re
from operator import itemgetter

def load_file(filepath):
    '''
    Read the file and return its contents as a string
    '''
    with open(filepath, "r+", encoding="utf-8") as file:
        file_str = file.read()
    return file_str

def get_word_frequency(input):
    '''
    Create a dictionary that maps a word to its frequency in the input. 
    '''
    regex_format = "['a-zāàéèŧēúíòōáśđŵĝĥùūóźŋâA-ZĀÀÉÈŦĒÚÍÒŌÁŚĐŴĜĤÙŪÓŹŊÂ]"
    regex_prog = re.compile(regex_format)
    
    word_start = -1 # Index of the 1st char in the word
    word_end = -1 # Index of the last char in the word
    recording_word = False # True if 
    
    words = {}
    
    for i in range(0, len(input)):
        char = input[i]
        is_match = regex_prog.match(char)
        
        # Is the current char a letter of a word?
        if is_match:
            if not recording_word:
                word_start = i
                recording_word = True
        
        # Otherwise, slice the word off the input using the recorded indexes 
        else:
            if recording_word:
                word_end = i
                
                word = input[word_start:word_end].lower()
                if word in words:
                    words[word] = words[word] + 1
                else:
                    words[word] = 1
        
                # Reset everything
                word_start = -1
                word_end = -1
                recording_word = False
                
    # Handle case where the last word goes to the end of the text
    if recording_word:
        word = input[word_start:len(input)].lower()
        if word in words:
            words[word] = words[word] + 1
        else:
            words[word] = 1
        
    return words

#input_str = "This is a test, always a test. Here's another sentence"
input_str = load_file("input.txt")
set_of_words = get_word_frequency(input_str).items() # ('the', 4020), etc
set_of_words = sorted(set_of_words, key=itemgetter(0)) # Sort by word
set_of_words = sorted(set_of_words, key=itemgetter(1), reverse=True) # Sort by frequency, backwards
for tup in set_of_words:
    print("{} ({} counts)".format(tup[0], tup[1]))
