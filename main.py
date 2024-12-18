import pandas as pd
import matplotlib.pyplot as plt

# loading data, multiple csv files
artworks = pd.read_csv("data/Artworks.csv")
artists = pd.read_csv("data/Artists.csv")
on_view = pd.read_excel("data/MoMA_OnView.xlsx")  # Excel file requires openpyxl

# previewing data, aka first 5 rows of a dataframe using .head()
print("Artworks Overview:")
print(artworks.head())

print("\nArtists Overview:")
print(artists.head())

print("\nOnView Overview:")
print(on_view.head())


print("Artworks Columns:", artworks.columns)
print("Artists Columns:", artists.columns)

# EDIT: fixed error. artworks was int, artists was string, fixed error by converting both to strings
artworks["ConstituentID"] = artworks["ConstituentID"].astype(str)
artists["ConstituentID"] = artists["ConstituentID"].astype(str)

# merge
merged_data = pd.merge(artworks, artists, on="ConstituentID", how="left")

# print
print("\nMerged Data Overview:")
print(merged_data.head())

# code to find most common mediums used
top_mediums = artworks["Medium"].value_counts().head(10)
print("\nTop 10 Art Mediums:")
print(top_mediums)

# visualization (bar chart)
top_mediums.plot(kind="bar", title="Top 10 Art Mediums")
plt.xlabel("Medium")
plt.ylabel("Number of Works")
plt.tight_layout()
plt.savefig("top_art_mediums.png")
plt.show()

# ending statement to let user know analysis was completed
print("\nanalysis complete. chart saved as 'top_art_mediums.png'.")
