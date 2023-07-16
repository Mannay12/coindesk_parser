from pymongo import MongoClient
import pandas as pd


def save_df_to_mongo(df, db_name, collection_name):
    client = MongoClient('mongodb://localhost:27017/')
    db = client[db_name]
    collection = db[collection_name]
    collection.insert_many(df.to_dict('records'))


data = pd.read_csv('coindesk.csv')
df = pd.DataFrame(data)
save_df_to_mongo(df, 'pandas_storage', 'news')