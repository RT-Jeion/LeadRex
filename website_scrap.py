import asyncio
import random
import re

from bs4 import BeautifulSoup
import nodriver as nd
from websockets import connect

from db import get_leads_from_db, update_database

from pathlib import Path

user_data = Path("./browser_data")
user_data.mkdir(exist_ok=True)


def rnd1():
    slp = random.uniform(1, 2.5)
    print("Sleeping..... for ", slp)
    return float(slp)


def rnd2():
    slp = random.uniform(5, 7)
    print("Sleeping..... for ", slp)
    return float(slp)


async def website_scrapper(links_lst):

    browser = await nd.start(headless=False, user_data_dir=user_data.absolute())

    data = []
    emtpy_mail = []

    for i, link in enumerate(links_lst):
        lst_len = len(links_lst)
        contact = link[1]
        link = link[0]
        print(
            "------------------------------------------------------------------------"
        )
        print(f"==> LINK NO {i + 1} | Links Left {lst_len - i - 1}")
        print(f"===| {link} |===\n")
        try:
            page = await asyncio.wait_for(browser.get(link), timeout=10)
            await asyncio.sleep(rnd1())

            html_content = await page.get_content()

            await asyncio.sleep(rnd1())

            soup = BeautifulSoup(html_content, "html.parser")
            emails1 = re.findall(
                r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", soup.get_text()
            )
            emails2 = [
                a["href"].replace("mailto:", "").split("?")[0]
                for a in soup.find_all("a", href=True)
                if a["href"].startswith("mailto:")
            ]

            emails = emails1 + emails2
            emails = list(set(emails))

            print()
            print("==> Emails  : ", emails)
            print("==> Contact :", contact)

            if len(emails) != 0:
                data.append({"Link": link, "Mail": emails, "Contact": contact})
            else:
                print("### Emtpy Mail Found..")
                emtpy_mail.append({"Link": link, "Mail": emails, "Contact": contact})
            print(
                "------------------------------------------------------------------------"
            )

        except asyncio.TimeoutError:
            print("\n======================")
            print("### Time Out Error ###")
            print("======================\n")
        except Exception as e:
            print(e)

    update_database(leads_lst=data, col_name="Links_and_Mails", unique_key="Link")
    update_database(
        leads_lst=emtpy_mail, col_name="Empty_mail_leads", unique_key="Link"
    )


if __name__ == "__main__":
    leads = get_leads_from_db(col_name="Leads_Brave-Search_Places")
    links = []

    for lead in leads:
        contact = lead.get("contact", "contact not found")
        if contact != "contact not found":
            contact = contact.get("telephone")

        links.append([lead["URL"], contact])

    asyncio.run(website_scrapper(links))
