import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


books = pd.read_csv("goodbooks-data/books.csv")
ratings = pd.read_csv("goodbooks-data/ratings.csv")


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Fill missing titles if any
books['title'] = books['title'].fillna('')

# TF-IDF on book titles
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(books['title'])

# Cosine similarity between all books
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Book index lookup
indices = pd.Series(books.index, index=books['title']).drop_duplicates()

def recommend_books(title, top_n=5):
    idx = indices.get(title)
    if idx is None:
        return "Book not found."
    
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    book_indices = [i[0] for i in sim_scores]
    
    return books.iloc[book_indices][['title', 'authors', 'average_rating']]

# Example:
print(recommend_books("The Hunger Games (The Hunger Games, #1)"))
