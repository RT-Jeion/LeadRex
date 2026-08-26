import random
from pathlib import Path

from scrapper import landing_page_scrap, instagram_link_scrap
import nodriver as nd
import asyncio


def rnd1():
    slp = random.uniform(2, 4)
    print("Sleeping..... for ", slp)
    return float(slp)


def rnd2():
    slp = random.uniform(5, 7)
    print("Sleeping..... for ", slp)
    return float(slp)


user_data = Path("./browser_data")
user_data.mkdir(exist_ok=True)


async def places_search():

    browser = await nd.start(headless=False, user_data_dir=str(user_data.absolute()))
    await asyncio.sleep(rnd1())

    user_query = input("Enter you search about Leads from google places.\n\nQuery: ")

    query_url = user_query.replace(" ", "+")
    print("Starting Searching Session. Query:", user_query)

    """
   # FOR AUTOMATED PROCESS 
    
    search_steps = int(input("Enter total search steps: "))
    step_gap = 20
    end = search_steps * step_gap
    for start in range(0, end, step_gap):


    """
    start = 0
    while True:
        print("Press Enter to Continue.\nType [exit] to quit.")
        user_res = input()

        serial = (start / 20) + 1
        print("=================================")
        print(f"Searching Interation no.{serial}")
        print("=================================")
        if user_res.lower() == "exit":
            break

        targer_url = f"https://www.google.com/search?q={query_url}&udm=1&start={start}"
        print("Opening Link:", targer_url)

        page = await browser.get(targer_url)

        await asyncio.sleep(rnd2())

        html_content = await page.get_content()

        await asyncio.sleep(rnd1())

        print("Successfully Loaded HTML Content..")
        print("Sending HTML Page for Scrapping.....")

        result = landing_page_scrap(page_content=html_content)

        leads = result[0]
        count = result[1]

        start += 20


async def instagram_search():
    browser = await nd.start(headless=False, user_data_dir=str(user_data.absolute()))
    await asyncio.sleep(rnd1())

    user_query = input("Enter you search for Instagram IDs.\n\nQuery: ")

    query_url = user_query.replace(" ", "+")
    print("Starting Searching Session.\nQuery:", user_query)

    """
   # FOR AUTOMATED PROCESS 
    
    search_steps = int(input("Enter total search steps: "))
    step_gap = 10
    end = search_steps * step_gap
    for start in range(0, end, step_gap):


    """

    start = 0
    while True:
        print("Press Enter to Continue.\nType [exit] to quit.")
        user_res = input()

        serial = (start / 10) + 1
        print("=================================")
        print(f"Searching Interation no.{serial}")
        print("=================================")
        if user_res.lower() == "exit":
            break

        targer_url = f"https://www.google.com/search?q={query_url}+site%3Ainstagram.com&start={start}"
        print("Opening Link:", targer_url)

        page = await browser.get(targer_url)

        await asyncio.sleep(rnd2())

        html_content = await page.get_content()

        await asyncio.sleep(rnd1())

        print("Successfully Loaded HTML Content..")
        print("Sending HTML Page for Scrapping.....")

        result = instagram_link_scrap(page_content=html_content)
        leads = result[0]
        count = result[1]

        start += 10
