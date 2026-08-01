import sqlite3
import pandas as pd

conn = sqlite3.connect("data_pipeline/database/books.db")
cursor = conn.cursor()
query1 = """
SELECT *
FROM books
LIMIT 10;
"""

print("\nQuery 1")
print(pd.read_sql(query1, conn))
query2 = """
SELECT title, rating
FROM books
WHERE rating = 5;
"""

print("\nQuery 2")
print(pd.read_sql(query2, conn))
query3 = """
SELECT title, price_gbp
FROM books
ORDER BY price_gbp DESC
LIMIT 10;
"""

print("\nQuery 3")
print(pd.read_sql(query3, conn))
query4 = """
SELECT DISTINCT category_name
FROM categories;
"""

print("\nQuery 4")
print(pd.read_sql(query4, conn))
query5 = """
SELECT title, price_gbp
FROM books
WHERE price_gbp BETWEEN 20 AND 30;
"""

print("\nQuery 5")
print(pd.read_sql(query5, conn))

query6 = """
SELECT
    b.title,
    c.category_name,
    b.rating,
    b.price_gbp

FROM books b

JOIN categories c

ON b.category_id = c.category_id

ORDER BY b.rating DESC

LIMIT 10;
"""

print("\nQuery 6")
join_df = pd.read_sql(query6, conn)

print(join_df.to_string(index=False))

# Read both tables into pandas
books_df = pd.read_sql("SELECT * FROM books", conn)

categories_df = pd.read_sql("SELECT * FROM categories", conn)

# Merge using pandas
merged_df = books_df.merge(
    categories_df,
    on="category_id"
)

# Select the same columns as SQL JOIN
merged_df = merged_df[[
    "title",
    "category_name",
    "rating",
    "price_gbp"
]]

# Sort the same way as SQL query
merged_df = merged_df.sort_values(
    by="rating",
    ascending=False
).head(10)

print("\nPandas Merge Result")
print(merged_df.to_string(index=False))
print("\nSQL JOIN Result")
print(join_df.to_string(index=False))

conn.close()