# Personalized News Aggregator

This is a simple Flask-based News Aggregator that fetches the latest news from NewsAPI.org based on user-selected categories and country preferences.

## Features
- Fetches news headlines based on category and country.
- Uses `Flask` for backend and `requests` for API calls.
- Displays news headlines with images and descriptions.

## Installation

1. Clone the repository or unzip the project folder.
2. Install dependencies:
   ```bash
   pip install flask requests newsapi-python
   ```
3. Replace `your_newsapi_key` in `app.py` with your actual API key from [NewsAPI](https://newsapi.org/).
4. Run the application:
   ```bash
   python app.py
   ```
5. Open `http://127.0.0.1:5000/` in your browser.

## Folder Structure

```
news_aggregator/
├── app.py
├── templates/
│   ├── index.html
├── static/
│   ├── style.css
├── README.md
```

