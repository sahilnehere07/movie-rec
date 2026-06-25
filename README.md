🎬 Movie Recommendation System


A full-stack AI-powered movie recommendation web app — search any movie and instantly get smart recommendations, posters, genres, and details.



🚀 Live App: movie-rec-gdej6hwq7udlzkxqt255k2.streamlit.app

🔗 Backend API: movie-rec-asqx.onrender.com


✨ Features


🔍 Smart Search — Type any movie keyword and get instant dropdown suggestions
🤖 TF-IDF Content-Based Recommendations — ML algorithm finds similar movies based on content
🎭 Genre-Based Recommendations — Discover more movies in the same genre via TMDB
🖼️ Movie Posters & Details — Real-time posters, overview, release date, genres
🏠 Home Feed — Browse Trending, Popular, Top Rated, Now Playing, Upcoming movies
📱 Responsive UI — Clean, wide-layout interface built with Streamlit



🛠️ Tech Stack

LayerTechnologyFrontendStreamlit (Python)Backend APIFastAPI (Python)ML AlgorithmTF-IDF + Cosine Similarity (scikit-learn)Movie DataTMDB API (The Movie Database)Backend DeploymentRenderFrontend DeploymentStreamlit Cloud


🧠 How It Works

User searches a movie
       ↓
Streamlit frontend sends request
       ↓
FastAPI backend receives request
       ↓
TF-IDF model finds similar movies (local dataset)
       ↓
TMDB API fetches real-time posters & details
       ↓
Results displayed to user with posters

Two Types of Recommendations:


TF-IDF (Content-Based) — Compares movie descriptions using cosine similarity to find the most similar movies from the local dataset
Genre-Based (TMDB) — Uses TMDB Discover API to fetch popular movies in the same genre



📁 Project Structure

movie-rec/
├── main.py              # FastAPI backend — all API routes
├── app.py               # Streamlit frontend — UI and interactions
├── requirements.txt     # Python dependencies
├── df.pkl               # Movie dataset (preprocessed DataFrame)
├── indices.pkl          # Title-to-index mapping for TF-IDF
├── tfidf_matrix.pkl     # Precomputed TF-IDF matrix
├── tfidf.pkl            # TF-IDF vectorizer object
└── .python-version      # Python version for Render


🔌 API Endpoints

MethodEndpointDescriptionGET/healthHealth checkGET/homeHome feed (trending, popular, etc.)GET/tmdb/searchSearch movies by keywordGET/movie/id/{tmdb_id}Get full movie detailsGET/movie/searchGet TF-IDF + Genre recommendations bundleGET/recommend/genreGenre-based recommendationsGET/recommend/tfidfTF-IDF recommendations only


⚙️ Run Locally

1. Clone the repo

bashgit clone https://github.com/sahilnehere07/movie-rec.git
cd movie-rec

2. Install dependencies

bashpip install -r requirements.txt

3. Add your TMDB API key

Create a .env file:

TMDB_API_KEY=your_tmdb_api_key_here

Get your free API key at themoviedb.org

4. Run the backend

bashuvicorn main:app --reload

5. Run the frontend

bashstreamlit run app.py


🌐 Deployment

ServicePlatformLinkBackend (FastAPI)Rendermovie-rec-asqx.onrender.comFrontend (Streamlit)Streamlit CloudLive App


👨‍💻 Author

Sahil Nehere

GitHub: @sahilnehere07

