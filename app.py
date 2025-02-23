from flask import Flask, render_template, request
import requests

app = Flask(__name__)

NEWS_API_KEY = "your_newsapi_key"  # Replace with your API Key
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"

@app.route("/", methods=["GET", "POST"])
def home():
    category = "general"
    country = "us"

    if request.method == "POST":
        category = request.form.get("category")
        country = request.form.get("country")

    params = {
        "apiKey": NEWS_API_KEY,
        "category": category,
        "country": country
    }

    response = requests.get(NEWS_API_URL, params=params)
    news_data = response.json()

    if news_data.get("status") == "ok":
        articles = news_data.get("articles", [])
    else:
        articles = []

    return render_template("index.html", articles=articles)

if __name__ == "__main__":
    app.run(debug=True)
