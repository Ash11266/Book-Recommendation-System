# 📚 Book Recommendation System

A collaborative filtering-based book recommender using the [Goodbooks-10k dataset](https://www.kaggle.com/datasets/zygmunt/goodbooks-10k) and Surprise SVD model.

## 💡 Features

- Item-based recommendations using `scikit-surprise`
- Flask web interface for user interaction
- Clean Bootstrap UI

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/yourusername/book-recommender.git
cd book-recommender

# (Optional) Create virtualenv
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run app
python app.py
