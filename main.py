from sql_integration import save_to_sql, query_enriched_data, query_acquisition_trends
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

# EDIT: fixed error. artworks used to be int, artists was string, fixed error by converting both to strings
artworks["ConstituentID"] = artworks["ConstituentID"].astype(str)
artists["ConstituentID"] = artists["ConstituentID"].astype(str)

# merge
merged_data = pd.merge(artworks, artists, on="ConstituentID", how="left")

# print to see the merged data result
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


# sql
def load_data():
    # Use unique names for local variables
    artworks_local = pd.read_csv("data/Artworks.csv")
    artists_local = pd.read_csv("data/Artists.csv")
    return artworks_local, artists_local


def main():
    # loading data
    artworks_local, artists_local = load_data()

    # sql save
    conn = save_to_sql(artworks_local, artists_local)

    # visualize
    enriched_data = query_enriched_data(conn)
    print("\nEnriched Data Sample:")
    print(enriched_data)

    # acquisition trends graph (line graph)
    acquisition_trends = query_acquisition_trends(conn)
    acquisition_trends.plot(kind="line", x="Year", y="ArtworkCount", title="Artwork Acquisitions Over Time")
    plt.ylabel("Number of Artworks")
    plt.show()

    # exit and end
    conn.close()


if __name__ == "__main__":
    main()
