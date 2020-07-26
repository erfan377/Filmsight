import collections 
import numpy as np 
import json

chars = np.loadtxt("movie_characters_metadata.txt", dtype = 'str', delimiter= ' +++$+++ ', encoding = 'iso-8859-1', comments = None)
lines = np.loadtxt("movie_lines.txt", dtype = 'str',  delimiter= ' +++$+++ ', encoding = 'iso-8859-1', comments = None)
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

with open('charToLine.json', 'w') as fp:
    json.dump(charToLine, fp, sort_keys=True, indent=4)
fp.close()
with open('charToMovie.json', 'w') as fp1:
    json.dump(charToMovie, fp1, sort_keys=True, indent=4)
fp1.close()