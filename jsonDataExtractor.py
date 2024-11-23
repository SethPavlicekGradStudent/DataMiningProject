import pandas as pd

class JSONDataExtractor():
    def __init__(self):
        self.valid_df = True

    def extractHeroInventory(self,match):

        try:
            if match is not None:
                data = [
                    {
                        "hero_id": player["hero_id"],
                        "item_0": player["item_0"],
                        "item_1": player["item_1"],
                        "item_2": player["item_2"],
                        "item_3": player["item_3"],
                        "item_4": player["item_4"],
                        "item_5": player["item_5"],
                    }
                    for player in match["players"]
                ]
                return pd.DataFrame(data)
        except Exception as e:
            return None
