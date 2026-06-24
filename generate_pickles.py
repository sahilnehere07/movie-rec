import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load your movies CSV
df = pd.read_csv("movies_metadata.csv", low_memory=False)

# Keep only needed columns and drop nulls
df = df[["id", "title", "overview"]].dropna(subset=["title", "overview"])
df = df.drop_duplicates(subset="title").reset_index(drop=True)

# Build TF-IDF matrix on overview
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["overview"])

# Build indices map (title -> row index)
indices = pd.Series(df.index, index=df["title"])

# Save all 4 pickle files
with open("df.pkl", "wb") as f:
    pickle.dump(df, f)

with open("tfidf_matrix.pkl", "wb") as f:
    pickle.dump(tfidf_matrix, f)

with open("tfidf.pkl", "wb") as f:
    pickle.dump(tfidf, f)

with open("indices.pkl", "wb") as f:
    pickle.dump(indices, f)

print("✅ All pickle files generated successfully!")