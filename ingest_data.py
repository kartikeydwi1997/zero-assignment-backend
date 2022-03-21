import pandas as pd
from tqdm import tqdm

from mongo_connection import get_collection


if __name__ == "__main__":

    #Fetch county and zipcode from county_data.csv and population and zipcode from population_data.csv
    
    COUNTY_FILE = "data/county_data.csv"
    POPULATION_FILE = "data/population_data.csv"

    county_df = pd.read_csv(COUNTY_FILE)
    pop_df = pd.read_csv(POPULATION_FILE)

    county_df = county_df[['zip', 'county']]
    county_df.columns = ['zipcode', 'county']

    #Group by zipcode with total population of all zipcode.
    pop_df = pop_df[['zipcode', 'population']]
    pop_df = pop_df.groupby('zipcode', as_index=False).sum()

    #Fill the zip code with 0 if length is less than 5.
    pop_county_df = pd.merge(county_df, pop_df, on='zipcode')
    pop_county_df['zipcode'] = pop_county_df['zipcode'].apply(
        lambda zipcode: str(zipcode).zfill(5))
    print(f"Got {len(pop_county_df)} records!")

    collection = get_collection('zip_county_data')

    #Insert the data into the database row by row.
    for _, row in tqdm(pop_county_df.iterrows()):
        collection.insert_one(row.to_dict())
