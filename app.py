from bs4 import ElementFilter
from pymongo import results

from browser import instagram_search, places_search
import asyncio


async def main():
    print("Welcome To LeadRex.")
    print("Available Options\n")
    print("1. Website Link From Google Places/Maps Search")
    print("2. Instagram Account Link From Google Search")

    user_input = input("Enter the Number of the serial.\n==>Input: ")

    if user_input == "1":
        await places_search()
    elif user_input == "2":
        await instagram_search()
    elif user_input.lower() == "exit":
        return
    else:
        print("Invalid Input!!!!")


asyncio.run(main=main())
