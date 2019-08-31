#################################
#IMPORTS
#################################
import pandas as pd

import numpy as np

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.metrics.pairwise import cosine_similarity

#################################
#HELPER FUNCTIONS
################################
def get_title_from_index(index):
    return df[df.index == index]["title"].vlaues[0]

def get_index_from_title(title):
    return df[df.title == title]["index"].vlaues[0]

#################################

#Step 1: Read CSV file
data_frame = pd.read_csv("Dataset/imdb.csv")
print(df.head())

#Step 2: Select features

#Step 3: Create a column in DF which combines all selected features

#Step 4: Create count matrix from this new combined column

#Step 5: Compute the Cosine Similarity based on the count_matrix

movie_user_like = "Avatar"

#Step 6: Get  index of this movie from its title

#Step 7: Get a list of similar movies in descending order of similarity score
