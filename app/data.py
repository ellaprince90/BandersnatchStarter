from os import getenv

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

    def seed(self, amount):
        pass

    def reset(self):
        pass

    def count(self) -> int:
        pass

    def dataframe(self) -> DataFrame:
        pass

    def html_table(self) -> str:
        pass
