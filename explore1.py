from slda.topic_models import SLDA

# import os
# import re
# import fnmatch
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
# from sklearn.decomposition import LatentDirichletAllocation

# def vectorize(df):
#     nFeatures=10000
#     tf_vectorizer = CountVectorizer(max_df=0.85, min_df=2,
#                                 max_features=nFeatures,
#                                 stop_words='english', lowercase=True)
#     tf = tf_vectorizer.fit_transform(df)
#     features = tf_vectorizer.get_feature_names()
#     return (tf, features)

# def runLDA(n, iters, wordMat):
#     slda = SLDA(_K, _alpha, _beta, _mu, _nu2, _sigma2, n_iter, seed=42)
#     slda.fit(doc_term_matrix, y)
#     results = slda.phi
#     return results
    
# def print_top_words(model, feature_names, n_top_words):
#     for topic_idx, topic in enumerate(model.components_):
#         print("Topic #%d:" % topic_idx)
#         print(" ".join([feature_names[i]
#                         for i in topic.argsort()[:-n_top_words - 1:-1]]))
#     print()

# reviews=[]
# for file in os.listdir('dataset/reviews/ps3'):
#     with open('dataset/reviews/ps3/'+file, 'r') as ip:
#         data=ip.read()
#         review=re.findall(r':::Review:::(.*?):::User Reviews:::', data, re.DOTALL)
#         review=str(review)
#         reviews.append(review)

# n=10
# iters=5
# nWords=10

# wordMat, features=vectorize(reviews)
# lda=runLDA(n, iters, wordMat)
# print_top_words(lda, features, nWords)