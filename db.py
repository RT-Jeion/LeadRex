from enum import unique

from pymongo import MongoClient, UpdateOne, operations, results

client = MongoClient("mongodb://localhost:27017/")
db = client["LeadRex"]


def update_database(leads_lst, col_name):
    leads_col = db[col_name]
    operations = [
        UpdateOne({"URL": lead["URL"]}, {"$setOnInsert": lead}, upsert=True)
        for lead in leads_lst
    ]

    if operations:
        result = leads_col.bulk_write(operations)
        print(f"Inset count:", result.inserted_count)
        print("Match Found:", result.matched_count)
        print("Upsert Count:", result.upserted_count)


if __name__ == "__main__":
    print(db.list_collection_names())
