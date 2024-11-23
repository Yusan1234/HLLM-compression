import pandas as pd
df = pd.read_csv('amazon_books.csv')

sampled_df = df.sample(n=50000)
sampled_df.to_csv('amazon_books_reduced.csv', index=False)

