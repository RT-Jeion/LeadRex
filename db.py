from pymongo import MongoClient, UpdateOne

client = MongoClient("mongodb://localhost:27017/")
db = client["LeadRex"]


def update_database(leads_lst, col_name, unique_key):
    print("\n=> Updating Database.")
    print(f"\n===| {col_name} |===\n")
    print(f"-> Unique Key: {unique_key}")
    leads_col = db[col_name]
    operations = [
        UpdateOne({"URL": lead[unique_key]}, {"$setOnInsert": lead}, upsert=True)
        for lead in leads_lst
    ]

    if operations:
        result = leads_col.bulk_write(operations)
        print("Match Found:", result.matched_count)
        print("Upsert Count:", result.upserted_count)
        print()
    return result.upserted_count, result.matched_count


def get_leads_from_db(col_name):
    print(db.list_collection_names())

    places_collection = db[col_name]

    print("Total Documents in Collection:", places_collection.count_documents({}))
    print("Enter Database Leads range.")
    mini = int(input("Enter first index: "))
    maxi = int(input("Enter Last index: "))

    result = []

    for i, l in enumerate(places_collection.find()):
        i += 1

        if i >= mini and i <= maxi:
            result.append(l)

    return result


if __name__ == "__main__":
    places = db["Leads_Brave-Search_Places"]
    print(places.count_documents({}))
    links = db["Links_and_Mails"]
    print(links.count_documents({}))
    emtpy = db["Empty_mail_leads"]
    print(emtpy.count_documents({}))

    leads_left = (links.count_documents({}) + emtpy.count_documents({})) - 2000

    print(leads_left)
