
# 🎬 Movie Recommendation System using Streamlit
[🌐Visit Website](https://partho-movie-recommender.streamlit.app/)

Welcome to the **Movie Recommendation System** built with Python and Streamlit! This app helps users discover movies similar to their favorites and also explore detailed information about any movie in the dataset. It leverages TMDB data and a content-based similarity model to generate recommendations.

---

## 🚀 Features

- 🔍 **Movie Recommendation Tab**  
  Enter a movie title and get **top 9 similar movies** with poster, director, rating, cast, and overview.

- 🎞️ **Movie Info Tab**  
  Search for any movie in the dataset and view **detailed information** including release year, cast, runtime, and a link to TMDB.

- 🖼️ Posters and Details  
  Poster images fetched from TMDB API and styled using Streamlit’s clean layout.

---

## 📂 Project Structure

```

📁 data/
│   ├── movie\_df\_merged\_all.csv
│   ├── movie\_df\_processed.csv
│   ├── similarity\_vector.npy
│   ├── tmdb\_5000\_credits.csv
│   ├── tmdb\_5000\_movies.csv
│   └── tmdb\_extra\_columns\_12M.csv
📄 movie\_df\_cleaning.ipynb     # Data cleaning and preprocessing
📄 movie\_df\_merging.ipynb      # Dataset merging and feature engineering
📄 movie\_recommender.py        # Main Streamlit app file

````

---

## 🔗 External Dependencies

* Movie poster paths and links use the [TMDB API](https://www.themoviedb.org/).
* Dataset includes data from:

  * `tmdb_5000_movies.csv`
  * `tmdb_5000_credits.csv`
  * Extra columns from `tmdb_extra_columns_12M.csv`

---

## 👤 Author

**Partho Sarothi Das**
Aspiring Data Scientist | Passionate about ML & Visualization
📧 Email: [partho52@gmail.com](mailto:partho52@gmail.com)

---

## 📝 License

This project is licensed under the MIT License. Feel free to use, modify, and share!

---

## 🌟 Acknowledgements

* [Streamlit](https://streamlit.io/)
* [The Movie Database (TMDB)](https://www.themoviedb.org/)

```
