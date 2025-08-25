from os import getenv

import pandas as pd
from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class MonsterDatabase:

    def __init__(self):
        load_dotenv()
        db_url = getenv("DB_URL")
        self.client = MongoClient(db_url)
        self.db = self.client["database_of_monsters"]
        self.collection = self.db["my_monsters"]

    def seed(self, amount: int) -> bool:
        "Seed database with given number of monsters"
        try:
            monsters = []
            for num in range(amount):
                m = Monster()
                if hasattr(m, "to_dict"):
                    monsters.append(m.to_dict())
                else:
                    monsters.append(m.__dict__)
            self.collection.insert_many(monsters)
            return True
        except Exception as e:
            print(f"Error seeding database: {e}")
            return False

    def reset(self):
        "Delete all monsters from the collection"
        try:
            self.collection.delete_many({})
            return True
        except Exception as e:
            print(f"Error resetting database: {e}")
            return False

    def count(self) -> int:
        "Return the number of monsters in the collection"
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        "Makes a dataframe of all monsters in th collection"
        try:
            documents_list = list(self.collection.find({}, {"_id":0}))
            return pd.DataFrame(documents_list)
        except Exception as e:
            print(f"Error creating dataframe: {e}")
            return DataFrame()

    def html_table(self) -> str:
        "Makes an HTML representation of the dataframe"
        try:
            df = self.dataframe()
            if df.empty:
                return f"No monsters found in database."
            return df.to_html()
        except Exception as e:
            return(f"Error generating HTML table: {e}")
