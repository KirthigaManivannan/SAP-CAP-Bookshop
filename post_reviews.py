
import requests
from collections import defaultdict

BASE_URL = "http://localhost:4004/odata/v4/catalog"

# Step 1: Fetch books from the CAP service
response = requests.get(f"{BASE_URL}/Books")
response.raise_for_status()
books = response.json()["value"]

if len(books) < 2:
    raise RuntimeError("At least two books are required to run this script.")

book1 = books[0]
book2 = books[1]

print("Books selected:")
print(f"1. {book1['title']} (ID: {book1['ID']})")
print(f"2. {book2['title']} (ID: {book2['ID']})")

# Step 2: Prepare three reviews
reviews_to_post = [
    {
        "book_ID": book1["ID"],
        "rating": 5,
        "comment": "Excellent book!"
    },
    {
        "book_ID": book1["ID"],
        "rating": 4,
        "comment": "Very informative."
    },
    {
        "book_ID": book2["ID"],
        "rating": 3,
        "comment": "A good read."
    }
]

# Step 3: Post reviews to the CAP service
for review in reviews_to_post:
    response = requests.post(
        f"{BASE_URL}/Reviews",
        json=review
    )
    response.raise_for_status()
    print(f"Review posted successfully: {review['rating']}/5")

# Step 4: Fetch all reviews
response = requests.get(f"{BASE_URL}/Reviews")
response.raise_for_status()
all_reviews = response.json()["value"]

# Step 5: Group ratings by book ID
ratings_by_book = defaultdict(list)

for review in all_reviews:
    book_id = review.get("book_ID")
    if book_id in (book1["ID"], book2["ID"]):
        ratings_by_book[book_id].append(review["rating"])

# Step 6: Calculate and print average ratings
book_titles = {
    book1["ID"]: book1["title"],
    book2["ID"]: book2["title"]
}

print("\nAverage rating per book:")

for book_id, ratings in ratings_by_book.items():
    average = sum(ratings) / len(ratings)
    print(
        f"{book_titles[book_id]}: "
        f"{average:.2f}/5 "
        f"({len(ratings)} reviews)"
    )
