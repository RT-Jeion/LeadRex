import random
from pathlib import Path
from scrapper import page_scrapper
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


async def main():

    user_query = input("Enter you Search Query\n==>")
    query_url = user_query.replace(" ", "+")
    print("Starting Searching Session. Query:", user_query)

    user_data = Path("./browser_data")
    user_data.mkdir(exist_ok=True)

    browser = await nd.start(headless=False, user_data_dir=str(user_data.absolute()))
    await asyncio.sleep(rnd1())

    for start in range(0, 200, 20):
        targer_url = f"https://www.google.com/search?q={query_url}&udm=1&start={start}"
        print("Opening Link:", targer_url)

        page = await browser.get(targer_url)

        await asyncio.sleep(rnd2())

        act = input("Press Enter to continue or type [exit] to the exit....")

        if act.lower() == "exit":
            print("Exiting Session")
            break

        html_content = await page.get_content()

        await asyncio.sleep(rnd1())

        print("Successfully Loaded HTML Content..")
        print("Sending HTML Page for Scrapping.....")

        links_num = page_scrapper(page_content=html_content)

        print("Links Found:", links_num)


if __name__ == "__main__":
    asyncio.run(main())
