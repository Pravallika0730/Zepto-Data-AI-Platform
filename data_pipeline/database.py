import pandas as pd
import sqlite3

df = pd.read_csv("data_pipeline/data/cleaned_books.csv")


# Create database connection

conn = sqlite3.connect("data_pipeline/database/books.db")

cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS categories(

    category_id INTEGER PRIMARY KEY AUTOINCREMENT,

    category_name TEXT UNIQUE

)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS books(

    book_id INTEGER PRIMARY KEY AUTOINCREMENT,

    title TEXT,

    price_gbp REAL,

    price_inr REAL,

    rating INTEGER,

    in_stock INTEGER,

    category_id INTEGER,

    FOREIGN KEY(category_id)

        REFERENCES categories(category_id)

)
""")
# Insert unique categories

categories = df["Category"].unique()

for category in categories:

    cursor.execute("""
    INSERT OR IGNORE INTO categories(category_name)
    VALUES(?)
    """, (category,))
cursor.execute("""
SELECT category_id, category_name
FROM categories
""")

category_dict = {}

for row in cursor.fetchall():

    category_dict[row[1]] = row[0]

print(category_dict)
for _, row in df.iterrows():

    cursor.execute("""
    INSERT INTO books(

        title,
        price_gbp,
        price_inr,
        rating,
        in_stock,
        category_id

    )

    VALUES(?,?,?,?,?,?)

    """,(

        row["Title"],
        row["price_gbp"],
        row["price_inr"],
        row["rating"],
        int(row["in_stock"]),
        category_dict[row["Category"]]

    ))
    conn.commit()

print("Data Inserted Successfully")
cursor.execute("SELECT COUNT(*) FROM books")

print("Books:", cursor.fetchone()[0])

cursor.execute("SELECT COUNT(*) FROM categories")

print("Categories:", cursor.fetchone()[0])

conn.close()