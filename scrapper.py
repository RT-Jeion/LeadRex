import json
from os import name
from bs4 import BeautifulSoup
from db import update_database


def page_scrapper(page_content):
    soup = BeautifulSoup(page_content, "html.parser")
    print("Created Page Soup")

    title = soup.title.string
    print("Page title:", title)

    links = soup.find_all("a")

    leads = []

    for link in links:
        link_text = link.text.strip()

        link_url = link.get("href")

        if link_text == "Website" and link_url[:4] == "http":
            link_name = (
                link_url.split(".com")[0].split("://")[-1].strip("www.").strip("/")
            )
            link_name = link_name.replace(".", " ")
            link_name = link_name.replace("-", " ")
            link_name = link_name.title()

            print("\nLink Name:", link_name)
            print("Link Url:", link_url)

            lead = {"Name": link_name, "URL": link_url}
            leads.append(lead)

    update_database(leads_lst=leads)

    return len(links)


if __name__ == "__main__":
    pass
