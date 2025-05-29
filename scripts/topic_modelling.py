import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def extract_topics(input_path, num_topics=5, num_words=10):
    df = pd.read_csv(input_path)
    texts = df['cleaned_text'].dropna().tolist()
    
    vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
    dtm = vectorizer.fit_transform(texts)
    
    lda = LatentDirichletAllocation(n_components=num_topics, random_state=42)
    lda.fit(dtm)
    
    for idx, topic in enumerate(lda.components_):
        print(f"\nTopic {idx + 1}:")
        print([vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-num_words:]])

if __name__ == "__main__":
    extract_topics('data/cleaned_tweets.csv')
