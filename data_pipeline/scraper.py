import requests
from bs4 import BeautifulSoup
import pandas as pd

# Empty list to store all books
books_data = []

# Loop through first 5 pages
for page in range(1, 6):

    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    print(f"Scraping Page {page}...")

    response = requests.get(url)
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        # Extract title
        title = book.h3.a["title"]

        # Get link to the book details page
        book_link = book.h3.a["href"]

        # Convert relative URL to full URL
        book_url = "https://books.toscrape.com/catalogue/" + book_link.replace("../", "")

        # Open book detail page
        book_response = requests.get(book_url)
        book_response.encoding = "utf-8"

        book_soup = BeautifulSoup(book_response.text, "html.parser")

        # Extract category
        breadcrumb = book_soup.find("ul", class_="breadcrumb")
        category = breadcrumb.find_all("li")[2].text.strip()

        # Extract price
        price = book.find("p", class_="price_color").text

        # Extract rating
        rating = book.find("p", class_="star-rating")["class"][1]

        # Extract availability
        availability = book.find(
            "p",
            class_="instock availability"
        ).get_text(strip=True)

        # Store the book details
        books_data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "Category": category
        })

# Convert list into DataFrame
df = pd.DataFrame(books_data)

print(df.head())
print("\nColumns:")
print(df.columns)
print("\nTotal Books Scraped:", len(df))

# Save to CSV
df.to_csv("data_pipeline/data/raw_books.csv", index=False)

print("\nData saved successfully!")