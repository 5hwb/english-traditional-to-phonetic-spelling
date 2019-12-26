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
    
input_str = "this is a test always a test"
output_str = ""
for words in input_str.split(" "):

    if (words in trad_to_ebeo_dict):
        output_str += trad_to_ebeo_dict[words] + " "
    else:
        output_str += "<{}>".format(words) + " "

print(output_str)
