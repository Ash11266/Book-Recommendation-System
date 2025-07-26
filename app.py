from flask import Flask, render_template, request
from recommend import recommend_books_for_user

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []
    user_id = None

    if request.method == "POST":
        user_id = request.form.get("user_id")
        if user_id and user_id.isdigit():
            user_id = int(user_id)
            recommendations = recommend_books_for_user(user_id)

    return render_template("index.html", recommendations=recommendations, user_id=user_id)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

