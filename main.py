import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Netflix Insights", layout="wide")
st.title(" Netflix Business Insights Dashboard")

@st.cache_data
def load():
    return pd.read_csv(r"D:\Dataset.csv").reset_index(drop=True)

df = load()

st.sidebar.header("Filters")
types = st.sidebar.multiselect("Type", df["type"].unique(), default=list(df["type"].unique()))
y_min, y_max = int(df["release_year"].min()), int(df["release_year"].max())
years = st.sidebar.slider("Release year", y_min, y_max, (2000, y_max))

f = df[df["type"].isin(types) & df["release_year"].between(*years)]


c1, c2, c3 = st.columns(3)
c1.metric("Total titles", len(f))
c2.metric("Movies", int((f["type"] == "Movie").sum()))
c3.metric("TV Shows", int((f["type"] == "TV Show").sum()))

tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Trend & Forecast", "Recommender", "Business Insights"])


with tab1:
    left, right = st.columns(2)

    fig = px.pie(f, names="type", title="Movies vs TV Shows", hole=0.4)
    left.plotly_chart(fig, use_container_width=True)

    countries = (f["country"].dropna().str.split(",").explode().str.strip()
                 .value_counts().head(10).reset_index())
    countries.columns = ["country", "count"]
    fig = px.bar(countries, x="count", y="country", orientation="h", title="Top 10 Countries")
    fig.update_layout(yaxis={"categoryorder": "total ascending"})
    right.plotly_chart(fig, use_container_width=True)

    genres = (f["listed_in"].dropna().str.split(",").explode().str.strip()
              .value_counts().head(10).reset_index())
    genres.columns = ["genre", "count"]
    fig = px.bar(genres, x="count", y="genre", orientation="h", title="Top 10 Genres")
    fig.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig, use_container_width=True)

# ---------- Tab 2: Trend & Forecast ----------
with tab2:
    yearly = df["release_year"].value_counts().sort_index()
    yearly = yearly[(yearly.index >= 2000) & (yearly.index <= 2020)]
    horizon = st.slider("Forecast years", 1, 5, 5)

    model = ExponentialSmoothing(yearly.values, trend="add").fit()
    pred = np.maximum(model.forecast(horizon), 0)
    fut = np.arange(yearly.index.max() + 1, yearly.index.max() + 1 + horizon)

    fig = go.Figure()
    fig.add_scatter(x=yearly.index, y=yearly.values, mode="lines+markers", name="Actual")
    fig.add_scatter(x=fut, y=pred, mode="lines+markers", name="Forecast", line=dict(dash="dash"))
    fig.update_layout(title="Titles per year with forecast", xaxis_title="Year", yaxis_title="Titles")
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    @st.cache_resource
    def build():
        text = (df["director"].fillna("") + " " +
                df["listed_in"].fillna("") + " " + df["listed_in"].fillna("") + " " +
                df["country"].fillna("")).str.lower()
        return TfidfVectorizer(stop_words="english").fit_transform(text)

    feature = build()
    title = st.selectbox("Pick a title", sorted(df["title"].unique()))
    if st.button("Recommend"):
        idx = df.index[df["title"] == title][0]
        scores = cosine_similarity(feature[idx], feature).flatten()
        top = scores.argsort()[::-1][1:6]
        st.table(df.iloc[top][["title", "type", "listed_in"]])