# Imports 
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances, manhattan_distances
from scipy.stats import pearsonr
from scipy.spatial import distance
from gensim.models import KeyedVectors

# loading GloVe model

model = KeyedVectors.load_word2vec_format(r"D:\Downloads\MIA\Task2\glove.6B\glove.6B.100d.txt", binary=False, no_header=True)

# Define traits for Hassan and the teams
hassan_traits = ["speed", "aggression", "adaptability", "technical_skill", "teamwork", "risk_taking", "consistency"]
team_traits = {
    'Red Bull': ["speed", "aggression", "adaptability", "technical_skill", "teamwork", "risk_taking", "inconsistency"],
    'Ferrari': ["passion", "emotion", "adaptability", "technical_skill", "teamwork", "risk_taking", "inconsistency"],
    'Mercedes': ["precision", "discipline", "adaptability", "technical_skill", "teamwork", "control", "consistency"]
}

# Convert a list of words to their average embedding vector.

def average_vector(words):
    vectors = [model[word.lower()] for word in words if word.lower() in model]
    return np.mean(vectors, axis=0) if vectors else np.zeros(model.vector_size)

# apply method to hassan and teams
hassan_vec = average_vector(hassan_traits)
team_vecs = {name: average_vector(traits) for name, traits in team_traits.items()}

# Compute semantic similarity scores
semantic_scores = {name: cosine_similarity([hassan_vec], [vec])[0][0] for name, vec in team_vecs.items()}

# --------------------------------- #

# numeric part 

Hassan = np.array([9, 8, 7, 6, 7, 8, 6])
teams_numeric = {
    'Red Bull': np.array([10, 9, 6, 7, 6, 9, 5]),
    'Ferrari': np.array([9, 7, 6, 6, 7, 7, 5]),
    'Mercedes': np.array([8, 6, 8, 9, 9, 5, 9])
}

# === Numeric Similarity Metrics ===
def similarity_metrics(base, comparison):
    #Useful when you care about the pattern/relative importance of traits
    cosine = cosine_similarity(base.reshape(1, -1), comparison.reshape(1, -1))[0][0]
    #Measures the straight-line distance between vectors in feature space
    euclidean = 1 / (1 + euclidean_distances(base.reshape(1, -1), comparison.reshape(1, -1))[0][0])
    #More robust to outliers than Euclidean, but still captures absolute differences.
    manhattan = 1 / (1 + manhattan_distances(base.reshape(1, -1), comparison.reshape(1, -1))[0][0])
    # Measures linear correlation (strength and direction of relationship).
    # Ignores scale and offset.
    pearson = pearsonr(base, comparison)[0]
    # Useful when relative differences at low values matter more
    canberra = 1 / (1 + distance.canberra(base, comparison))
    return [cosine, euclidean, manhattan, pearson, canberra]

# Making DataFrame for Numeric Metrics
metrics = ['Cosine', 'Euclidean', 'Manhattan', 'Pearson', 'Canberra']
numeric_df = pd.DataFrame(columns=metrics, index=teams_numeric.keys())

# giving values to the DataFrame
for name, vec in teams_numeric.items():
    numeric_df.loc[name] = similarity_metrics(Hassan, vec)

# Adding semantic similarity scores to series 
numeric_df['Semantic'] = pd.Series(semantic_scores)

# Semantic similarity scores (from word embeddings)
print("Semantic Similarity Scores:")
print(pd.Series(semantic_scores))

# Numeric similarity scores (from trait ratings)
print("\nNumeric Similarity Metrics:")
print(numeric_df)

# Final recommendation based on numeric is Ferrari
# Final recommendation based on semantic is Red Bull