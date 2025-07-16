import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


books = pd.read_csv("goodbooks-data/books.csv")
ratings = pd.read_csv("goodbooks-data/ratings.csv")


# Quick look at the data
print(books.shape)
print(ratings.shape)

'''
print(books.info())
print(ratings.info())

print(books.head())
print(ratings.head())

print("Books missing:", books.isnull().sum())
print("Ratings missing:", ratings.isnull().sum())

print("Duplicate books:", books.duplicated().sum())
print("Duplicate ratings:", ratings.duplicated().sum())

'''
# For data cleaning
# Keep users who rated at least 5 books
active_users = ratings['user_id'].value_counts()
ratings = ratings[ratings['user_id'].isin(active_users[active_users >= 5].index)]

# Keep books with at least 10 ratings
popular_books = ratings['book_id'].value_counts()
ratings = ratings[ratings['book_id'].isin(popular_books[popular_books >= 10].index)]

print("After filtering:", ratings.shape)
print("After filtering:", books.shape)


top_books = ratings['book_id'].value_counts().head(10)
top_books_df = books[books['id'].isin(top_books.index)]


# Bar Graph of 10 most popular books according to number of reviews
plt.figure(figsize=(10, 6))
sns.barplot(x=top_books_df['title'], y=top_books.values)
plt.xticks(rotation=45, ha='right')
plt.title("Top 10 Most Rated Books")
plt.xlabel("Book Title")
plt.ylabel("Number of Ratings")
plt.tight_layout()
plt.show()

# plot for distribution of ratings
plt.figure(figsize=(6, 4))
sns.countplot(x='rating', data=ratings, palette='viridis')
plt.title("Distribution of Book Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()



# Average Rating per book
# Filter books with at least 100 ratings
book_ratings = ratings.groupby('book_id').agg({'rating': ['mean', 'count']})
book_ratings.columns = ['avg_rating', 'num_ratings']
popular_books = book_ratings[book_ratings['num_ratings'] >= 100].sort_values(by='avg_rating', ascending=False).head(10)
popular_books = popular_books.merge(books, left_index=True, right_on='id')

plt.figure(figsize=(10, 6))
sns.barplot(x='avg_rating', y='title', data=popular_books, palette='mako')
plt.title("Top Rated Books (100+ Ratings)")
plt.xlabel("Average Rating")
plt.ylabel("Book Title")
plt.show()

# No. of Rating vs avg Ratings
book_ratings['log_num_ratings'] = np.log1p(book_ratings['num_ratings'])

sns.jointplot(
    data=book_ratings,
    x='log_num_ratings',
    y='avg_rating',
    alpha=0.5,
    height=7
)

plt.suptitle("Log(Number of Ratings) vs Average Rating", fontsize=14)
plt.tight_layout()
plt.subplots_adjust(top=0.95)
plt.show()
