from asyncio import sleep

from pymongo import MongoClient

# 1. Connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")
# 2. Retrieve all database names
all_databases = client.list_database_names()

# 3. Print the list

for db in all_databases:
    print("Database:", db)
