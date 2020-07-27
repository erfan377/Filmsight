import collections 
import numpy as np 
import json
import os

path = os.path.dirname(os.path.realpath(__file__))
chars = np.loadtxt(path + "\movie_characters_metadata.txt", dtype = 'str', delimiter= ' +++$+++ ', encoding = 'iso-8859-1', comments = None)
lines = np.loadtxt(path + "\movie_lines.txt", dtype = 'str',  delimiter= ' +++$+++ ', encoding = 'iso-8859-1', comments = None)
#minimume number of words required for each character
word_limit = 600
#List of CharIDs of characters 
charId = []
#A map from CharID to the list of movies they are in 
charToMovie = collections.defaultdict(list)
#A map from CharID to the list of dialogues they have      
charToLine = collections.defaultdict(list)
for fields in chars:
	charId.append(fields[0])
	charToMovie[fields[0]].append(fields[2])
for fields in lines: 
	charToLine[fields[1]].append(fields[4])

# save a json file for each character
for char_id in charToLine.keys():
	char_diag = char_data[char_id]
	char_text = ' '.join(char_diag)
	if len(char_text.split()) > word_limit: # number of words should be more for accurate results
		dict_out = [dict(content = char_text, contenttype = 'text/plain', created = 1, id = "u01", language = "en")]
		with open('character_json/' + str(char_id) + '.json', 'w') as fp:
			fp.write(dumps({'contentItems' : dict_out}, indent=4)+ "\n")
		fp.close()
with open('charToMovie.json', 'w') as fp1:
    json.dump(charToMovie, fp1, sort_keys=True, indent=4)
fp1.close()
