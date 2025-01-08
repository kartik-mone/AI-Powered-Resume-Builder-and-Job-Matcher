import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Load your dataset
df = pd.read_csv('C:\Users\Karti\Documents\Projects (Kartik)\AI-Powered Resume Builder and Job Matcher\data\jb_df.csv')  # Replace with your dataset path

# Preprocess the data
df['Job Description'] = df['Job Description'].fillna('')  # Handle missing descriptions
X = df['Job Description']
y = df['Job Title']  # Replace with the column name for job titles

# Convert text data to TF-IDF features
vectorizer = TfidfVectorizer(stop_words='english')
X_tfidf = vectorizer.fit_transform(X)

# Train the Naive Bayes classifier
model = MultinomialNB()
model.fit(X_tfidf, y)

# Save the model
with open('models/ml_model.pkl', 'wb') as f:
    pickle.dump(model, f)
