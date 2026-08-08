import json
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

            print("\nLink Name:", link_name)
            print("Link Url:", link_url)

            lead = {"Name": link_name, "URL": link_url}
            leads.append(lead)

    update_database(leads_lst=leads)

    return len(links)


if __name__ == "__main__":
    with open("download.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    page_scrapper(html_content)
