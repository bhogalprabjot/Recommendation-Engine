#################################
#IMPORTS
#################################
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#HELPER FUNCTIONS

def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
    return df[df.title == title]["index"].values[0]

#Step 1: Read CSV file
df = pd.read_csv("movie_dataset.csv")
#df.head()
#df.columns

#Step 2: Select features
features = ['keywords','cast', 'genres','director']

#Step 3: Create a column in DF which combines all selected features
for feature in features:
    df[feature] = df[feature].fillna('')

def combine_features(row):
    try:
        return row['keywords'] + " " + row['cast'] + " " + row['genres'] + " " + row['director']
    except:
        print("Error", row)

df["combined_features"] = df.apply(combine_features, axis = 1)

#Step 4: Create count matrix from this new combined column
vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(df["combined_features"])
count_matrix_array = count_matrix.toarray()

#Step 5: Compute the Cosine Similarity based on the count_matrix
cosine_sim = cosine_similarity(count_matrix)
# print("Enter your favourite movie: ")
# read(movie_user_likes)
movie_user_likes = "Harry Potter and the Half-Blood Prince"

#Step 6: Get  index of this movie from its title
movie_index = get_index_from_title(movie_user_likes)
similar_movies = list(enumerate(cosine_sim[movie_index]))

#Step 7: Get a list of similar movies in descending order of similarity score
sorted_similar_movies = sorted(similar_movies, key = lambda x:x[1], reverse = True)


# Step 8: Print 10 similar movie
i=0
print("\nList of similar movies: \n")
for movie in sorted_similar_movies:
    print(get_title_from_index(movie[0]))
    i+=1
    if i>1  0:
        break
