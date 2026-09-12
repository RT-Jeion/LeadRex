import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

from db import update_database
from llm import groq_answer


def brave_places_saerch():
    query = input("Enter you Search: ")

    queries = groq_answer(query)

    endpoint = "https://api.search.brave.com/res/v1/local/place_search"
    head = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "X-Subscription-Token": os.getenv("BRAVE_API_KEY_SEARCH"),
    }

    print("Total Queries found:", len(queries))
    for i, q in enumerate(queries):
        print(f"{i}. {q['niche']} {q['location']}")

    match_found = 0
    upsert_count = 0

    for i, q in enumerate(queries):
        niche = q["niche"]
        location = q["location"]
        print("Searchin for:", niche)
        print("location:", location)
        params = {"q": niche, "location": location, "count": 100}

        response = requests.get(
            endpoint,
            headers=head,
            params=params,
        ).json()

        result = response["results"]

        result[:]["From Query"] = niche + " " + location

        queries[i]["query"] = queries[i]["niche"] + " " + queries[i]["location"]

        count = update_database(
            leads_lst=result, col_name="Leads_Brave-Search_Places2.0", unique_key="url"
        )

        match_found += count[1]
        upsert_count += count[0]
        print("|--------------------")
        print("|Updating Database: Leads_Brave-Search_Places2.0")
        print("|Total Match:", match_found)
        print("|Total Upsert:", upsert_count)
        print("|--------------------")

    query_reuslt = update_database(
        leads_lst=queries, col_name="Searched_Queries_Brave_Places", unique_key="query"
    )
    print("Query Match Found:", query_reuslt[1])
    print("Query Upser Count:", query_reuslt[0])


if __name__ == "__main__":
    brave_places_saerch()
