import Pre_process
import collections
import json
import os
import numpy as np
import sklearn  

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
                for value in read_dict['values']:
                        char_dict[char_ID].append(value['raw_score'])


# computed k-means and knn model fits for the personality data and movie IIBCF
char_vec = []
movie_vec = []
Id_finder = collections.defaultdict(int)
for char_ID in char_dict:
	char_vec.append(char_dict[char_ID])

char_vec = np.asarray(char_vec)
kmeans = sklearn.cluster.KMeans(n_clusters=8, *, init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances='deprecated', verbose=0, random_state=None, copy_x=True, n_jobs='deprecated', algorithm='auto').fit(char_vec)

for mov_ID in Pre_process.movieToVec:
	movie_vec.append(char_dict[char_ID])

movie_vec = np.asarray(movie_vec)
knn = sklearn.neighbors.NearestNeighbors(*, n_neighbors=5, radius=1.0, algorithm='auto', leaf_size=30, metric='minkowski', p=2, metric_params=None, n_jobs=None).fit(movie_vec)


