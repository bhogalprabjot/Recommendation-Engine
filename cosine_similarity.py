from sklearn.feature_extraction.text import CountVectorizer

from sklearn.metrics.pairwise import cosine_similarity


txt = ["London Paris London",  "Paris Paris London"]

vectorizer = CountVectorizer()

count_matrix = vectorizer.fit_transform(txt)                                               #Learn the vocabulary dictionary and return term-document matrix.

words = vectorizer.get_feature_names()                                                    #Array mapping from feature integer indices to feature name

count_matrix_array = count_matrix.toarray()

similarity_score = cosine_similarity(count_matrix)

print("\nThe words are\n", words)

print("\nTheir term-document matrix in array representation\n", count_matrix_array)

print("\nThe cosine similarity score:\n", similarity_score)
