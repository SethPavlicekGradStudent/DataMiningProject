from OpenDotaAPI import OpenDotaAPI
from jsonDataExtractor import JSONDataExtractor
import time
import json 
import pandas as pd
import os 

def main(sleep_time = 2):
    api = OpenDotaAPI(verbose= True)
    data = JSONDataExtractor()
    # df = pd.read_csv('veryLargeAmountsOfData.csv')
    # i = 0
    match_df = pd.read_csv("2022_Match_IDs.csv")
    match_ids = match_df["match_id"].iloc[20000:21000]
    while True:
        
        for recent_match in match_ids:
            match_details = api.get_match_info(recent_match)
            table = None
            if match_details is not None:
                table = data.extractHeroInventory(match_details)
            if table is not None:
                # if not (table.isna().any().any()):
                file_path = 'veryLargeAmountsOfData.csv'
                if os.path.isfile(file_path):
                    # Append the DataFrame to the existing CSV file without overwriting
                    table.to_csv(file_path, mode='a', header=not pd.io.common.file_exists(file_path), index=False)
                    print(table)
                else:
                    # If the file doesn't exist, create a new CSV file
                    table.to_csv(file_path, index=False)  
                
# def filter_matches(matches_list):
#     return list(filter(lambda m: _filter_function(m), matches_list))

# def _filter_function(match):
#     if match['duration'] < 1000 or match['duration'] > 4200:
#         return False
#     else:
#         return True

if __name__ == "__main__":
    main()