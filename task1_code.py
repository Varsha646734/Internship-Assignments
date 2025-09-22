import pandas as pd

# Sample raw data
data = {
    "CustomerID": [1, 2, 2, 3, 4],
    "Name": ["Varsha", "Megha", "Megha", "Rahul", "Ankit"],
    "Gender": ["F", "Female", "Female", "M", "Male"],
    "Age": [20, None, None, 25, 27],
    "Country": ["India", "india", "india", "USA", "U.S.A."],
    "Join_Date": ["12/05/23", "2023-06-01", "2023-06-01", "05-07-2023", "7th July 23"]
}

df = pd.DataFrame(data)

# Handle missing values (fill with 22)
df["Age"].fillna(22, inplace=True)

# Remove duplicates
df = df.drop_duplicates()

# Standardize gender
df["Gender"] = df["Gender"].replace({"F": "Female", "M": "Male"})

# Standardize country names
df["Country"] = df["Country"].str.replace("india", "India", case=False)
df["Country"] = df["Country"].replace({"U.S.A.": "USA"})

# Convert dates to YYYY-MM-DD
df["Join_Date"] = pd.to_datetime(df["Join_Date"], errors="coerce").dt.strftime("%Y-%m-%d")

# Rename columns
df.columns = [col.lower().replace(" ", "_") for col in df.columns]

# Save to CSV
df.to_csv("cleaned_dataset.csv", index=False)
print(df)
