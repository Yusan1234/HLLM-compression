import pandas as pd

# Load the reduced book dataset
reduced_books = pd.read_csv('../information/amazon_books.csv')  # Replace with your reduced book dataset file name
book_item_ids = reduced_books['item_id'].unique()  # Get unique item IDs from the reduced book dataset

# Load the large user review dataset
user_reviews = pd.read_csv('amazon_books.csv')  # Replace with your user review dataset file name

# Filter the user review dataset to include only reviews for the reduced item IDs
filtered_reviews = user_reviews[user_reviews['item_id'].isin(book_item_ids)]

# Save the filtered user reviews to a new CSV file
filtered_reviews.to_csv('filtered_amazon_books.csv', index=False)

print(f"Original user review dataset size: {len(user_reviews)}")
print(f"Filtered user review dataset size: {len(filtered_reviews)}")

