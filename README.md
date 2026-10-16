# Netflix Content Analytics

An interactive Streamlit app that explores the Netflix catalog and combines
EDA, machine learning, forecasting, and a recommender system in one dashboard.

## Features

- **Exploratory Data Analysis:** content split (Movies vs TV Shows), top countries, top genres, ratings, and release-year trends.
- **Classification:** compares Logistic Regression, Decision Tree, and Random Forest using Accuracy and weighted F1.
- **Forecasting:** compares Linear Regression and Holt's exponential smoothing (additive trend) on yearly title counts, evaluated with MAE and RMSE.
- **Recommender:** content-based recommendations using TF-IDF on director, genre (`listed_in`), and country, ranked by cosine similarity.
- **Business Insights:** key takeaways drawn from the analysis.

## Tech Stack

Python, Pandas, NumPy, scikit-learn, statsmodels, Streamlit

## Project Structure

```
netflix-content-analytics/
├── main.py               # Streamlit app
├── netflix_titles.csv    # Dataset
├── requirements.txt
└── README.md
```

## Dataset

Columns used: `type`, `title`, `director`, `country`, `rating`, `duration`, `listed_in`, `release_year`.

## Installation

```bash
git clone https://github.com/<your-username>/netflix-content-analytics.git
cd netflix-content-analytics
pip install -r requirements.txt
```

## Run the App

```bash
streamlit run main.py
```

## How the Recommender Works

Each title is converted into a text profile (director + genres + country),
vectorized with TF-IDF, and compared using cosine similarity. The five most
similar titles are shown.

## Results

| Task           | Best Model | Metric |
|----------------|------------|--------|
| Classification | _fill in_  | _fill in_ |
| Forecasting    | _fill in_  | _fill in_ |

## Future Improvements

- Add the `description` and `cast` columns for richer recommendations.
- Hyperparameter tuning with cross-validation.
- Deploy on Streamlit Community Cloud.

## Author

Your Name · [GitHub](https://github.com/<your-username>)
