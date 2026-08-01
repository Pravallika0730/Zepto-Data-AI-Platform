# Data Pipeline

## Objective

This module builds an end-to-end data pipeline by scraping book data from BooksToScrape, cleaning the data, converting prices from GBP to INR, storing the cleaned data in a normalized SQLite database, and querying the database using SQL and pandas.

---

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- SQLite

---

## Dataset

Source:

https://books.toscrape.com/

Books Scraped:

- First 5 pages
- 100 books

Fields:

- Title
- Price
- Rating
- Availability
- Category

---

## Data Cleaning

Performed the following:

- Removed the GBP currency symbol.
- Converted price to float (`price_gbp`).
- Converted ratings (One–Five) to integers (1–5).
- Converted availability into boolean (`in_stock`).
- Converted GBP to INR using the fixed conversion rate:

```
1 GBP = 105.50 INR
```

- Saved cleaned data as `cleaned_books.csv`.

---

## Database Design

### Categories Table

- category_id (Primary Key)
- category_name

### Books Table

- book_id (Primary Key)
- title
- price_gbp
- price_inr
- rating
- in_stock
- category_id (Foreign Key)

---

## SQL Features Demonstrated

- SELECT
- WHERE
- ORDER BY
- LIMIT
- DISTINCT
- BETWEEN
- JOIN

---

## Output Files

- raw_books.csv
- cleaned_books.csv
- books.db

---

## Run Order

1. scraper.py
2. cleaner.py
3. database.py
4. queries.py
Project completed as part of the Zepto AI/ML Capstone Project.