# test.py

from recommend import recommend_books_for_user

# Replace with a real user ID from your dataset
user_id = 123

recommendations = recommend_books_for_user(user_id=user_id, top_n=5)

if not recommendations:
    print("No recommendations found. Maybe the user has no ratings.")
else:
    for i, book in enumerate(recommendations, 1):
        print(f"{i}. {book['title']} by {book['authors']}")
