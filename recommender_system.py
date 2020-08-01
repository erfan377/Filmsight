import collections
import json
import os

# List the json files representing the personality results
path = os.path.dirname(os.path.realpath(__file__))
json_folder = [f for f in os.listdir(path + '/personality_results/')]
char_dict = collections.defaultdict(list)

# read json files and list the results raw scores for each movie character
for json_file in json_folder:
        with open(path + '/personality_results/' + json_file, 'r') as fp:
                char_ID = json_file.split('.')[0]
                read_dict = json.load(fp)
                for big5_score in read_dict['personality']:
                        char_dict[char_ID].append(big5_score['raw_score'])
                for need in read_dict['needs']:
                        char_dict[char_ID].append(need['raw_score'])
                for value  in read_dict['values']:
                        char_dict[char_ID].append(value['raw_score'])
                
