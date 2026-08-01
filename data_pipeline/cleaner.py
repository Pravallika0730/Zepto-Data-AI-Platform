import pandas as pd

# Read the raw CSV file
df = pd.read_csv("data_pipeline/data/raw_books.csv")

# Display first 5 rows
print("Original Data:")
print(df.head())

print("\nData Types Before Cleaning:")
print(df.dtypes)

# -------------------------------
# Convert Price to price_gbp
# -------------------------------

# Remove unwanted characters and convert to float
df["price_gbp"] = (
    df["Price"]
    .str.replace("Â", "", regex=False)
    .str.replace("£", "", regex=False)
    .astype(float)
)

print("\nPrice Conversion:")
print(df[["Price", "price_gbp"]].head())

print("\nData Types After Price Conversion:")
print(df.dtypes)

# -------------------------------
# Convert Rating to Integer
# -------------------------------

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["rating"] = df["Rating"].map(rating_map)

print("\nRating Conversion:")
print(df[["Rating", "rating"]].head())

# -------------------------------
# Convert Availability to Boolean
# -------------------------------

df["in_stock"] = df["Availability"].str.contains("In stock")

print("\nAvailability Conversion:")
print(df[["Availability", "in_stock"]].head())

# -------------------------------
# Convert GBP to INR
# -------------------------------

GBP_TO_INR = 105.50

df["price_inr"] = df["price_gbp"] * GBP_TO_INR

print("\nGBP to INR Conversion:")
print(df[["price_gbp", "price_inr"]].head())

print("\nFinal Data Types:")
print(df.dtypes)

# Save cleaned data
df.to_csv("data_pipeline/data/cleaned_books.csv", index=False)

print("\nCleaned data saved successfully!")