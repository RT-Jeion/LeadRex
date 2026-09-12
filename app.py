from bs4 import ElementFilter
from pymongo import results

from browser import instagram_search, places_search
from brave_search import brave_places_saerch
import asyncio


async def main():
    print("Welcome To LeadRex.")
    print("Available Options\n")
    print("1. Website Link From Google Places/Maps Search")
    print("2. Instagram Account Link From Google Search")
    print("3. Brave Seach Places from Brave API Services")

    user_input = input("Enter the Number of the serial.\n==>Input: ")

    if user_input == "1":
        await places_search()
    elif user_input == "2":
        await instagram_search()
    elif user_input == "3":
        brave_places_saerch()
    elif user_input.lower() == "exit":
        return
    else:
        print("Invalid Input!!!!")


try:
    while True:
        asyncio.run(main=main())
except KeyboardInterrupt:
    print("Stopped By User.")
