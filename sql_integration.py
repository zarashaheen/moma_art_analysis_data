# later added sql in order to store datasets & perform query analysis..not very refined however
import sqlite3
import pandas as pd

# dataframes --> sqlite database
def save_to_sql(artworks_df, artists_df, db_name="moma.db"):
    conn = sqlite3.connect(db_name)
    artworks_df.to_sql("artworks", conn, if_exists="replace", index=False)
    artists_df.to_sql("artists", conn, if_exists="replace", index=False)
    return conn

# query enriched data (artwork titles, mediums, artist nationalities)
def query_enriched_data(conn):
    query = """
    SELECT a.Title, a.Medium, ar.DisplayName, ar.Nationality
    FROM artworks a
    JOIN artists ar ON a.ConstituentID = ar.ConstituentID
    LIMIT 10
    """
    return pd.read_sql_query(query, conn)

# query acquisition trends over time
def query_acquisition_trends(conn):
    query = """
    SELECT strftime('%Y', DateAcquired) as Year, COUNT(*) as ArtworkCount
    FROM artworks
    WHERE DateAcquired IS NOT NULL
    GROUP BY Year
    ORDER BY Year
    """
    return pd.read_sql_query(query, conn)



