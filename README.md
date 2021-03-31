# Transliterate from English to phonetic spelling

This is a set of Python scripts that convert normal English writing into phonetic English writing using the EBEO orthography. It uses the [CMU Pronouncing Dictionary (CMUdict)](http://www.speech.cs.cmu.edu/cgi-bin/cmudict?in=singing+beats) to map normal English words to their phonetic versions.

## How to use the scripts (WIP)

Note: file names are slightly messy, need to organise them better

### How to do frequency analysis of input text and create base mapping

1. Create a file called `input.txt` and paste the input to analyse there.
2. Run `get_word_frequency.py` - this loads `trad_to_ebeo.txt`, which maps traditional English words to their corresponding EBEO spellings (based on American accent in CMUdict), then analyses the contents of `input.txt` and count the frequency of each identified word before placing the output to `frequency-geo-out.txt`.

### Modify base mapping to create final mapping

1. Examine `frequency-geo-out.txt` and modify each element to better fit the nuances of your accent. 
2. Once done, open a text editor with regular expression capabilities and copy the contents of `frequency-geo-out.txt` to a new file called `map_trad_to_geo_basedonfreq.txt`.
3. Open the find/replace field and replace `(.+) \(.+\)\. GEO: (.+)` with `\1 = \2`
4. Add more entries as needed, e.g. 'jump = jámp'. For words with more than 1 pronunciation, wrap them in brackets: 'the = [dhu, dhi]'.

### Transliterate between traditional and phonetic spellings

1. Create a file called `2input.txt` and paste the input to transliterate there.
2. Run `translate_to_from_phonetic.py` = this loads the traditional-to-phonetic mapping in `map_trad_to_geo_basedonfreq.txt` and replaces each found word in `2input.txt` with their corresponding phonetic equivalents, writing the output to `trad_input_converted-2out.txt`.

## TODO

* Fix pronunciation of some words
* Idea: create a 'personalised dict' that only contains the words of the input string to be translated. This could reduce the chance of uncommon words reducing the quality of translation
