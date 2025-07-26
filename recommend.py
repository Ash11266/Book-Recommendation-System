# recommend.py

import pandas as pd
from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split

# Load and train SVD model once at module level (to avoid retraining on every request)
print("⏳ Loading data and training model...")

# Load ratings
ratings = pd.read_csv("goodbooks-data/ratings.csv")
books = pd.read_csv("goodbooks-data/books.csv")

# Prepare Surprise dataset
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(ratings[['user_id', 'book_id', 'rating']], reader)

# Train/test split
trainset, _ = train_test_split(data, test_size=0.2, random_state=42)

# Train model
model = SVD()
model.fit(trainset)

print("✅ Model trained.")

# -------- Recommendation Function --------

def recommend_books_for_user(user_id, top_n=5):
    """
    Recommends books to a given user based on collaborative filtering using SVD.
    Returns a list of dicts: [{title, authors, rating}]
    """
    # Get all unique book IDs
    all_book_ids = books['id'].unique()

    # Predict ratings for all books for this user
    predictions = []
    for book_id in all_book_ids:
        try:
            pred = model.predict(user_id, book_id)
            predictions.append((book_id, pred.est))
        except:
            continue  # Ignore books/user combos with issues

    # Sort by predicted rating
    predictions.sort(key=lambda x: x[1], reverse=True)

    # Take top N book IDs
    top_book_ids = [book_id for book_id, _ in predictions[:top_n]]

    # Return details
    recommended_books = books[books['id'].isin(top_book_ids)][['title', 'authors', 'average_rating']]
    return recommended_books.to_dict('records')
