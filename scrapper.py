from bs4 import BeautifulSoup
from db import update_database


def landing_page_scrap(page_content):
    soup = BeautifulSoup(page_content, "html.parser")
    print("Created Page Soup")

    title = soup.title.string
    print("Page title:", title)

    links = soup.find_all("a")

    leads = []
    count = 0

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

            count += 1

    update_database(leads_lst=leads, col_name="Leads_Website__Places", unique_key="URL")

    return leads, count


def instagram_link_scrap(page_content):
    soup = BeautifulSoup(page_content, "html.parser")
    print("Created Page Soup")

    title = soup.title.string
    print("Page Title:", title)
    print()

    links = soup.find_all("a")

    count = 0
    leads = []
    for link in links:
        link_text = link.text.strip()
        link_url = link.get("href")

        if link_url:
            lst = link_url.split("/")

            if "www.instagram.com" in lst and lst[3] != "reel":
                fresh_link_url = "/".join(lst[:4])

                count += 1

                lead = {"Text": link_text, "URL": fresh_link_url}

                leads.append(lead)

    update_database(
        leads_lst=leads, col_name="Leads_Instagram__Default", unique_key="URL"
    )

    return leads, count


if __name__ == "__main__":
    with open(
        "/home/rt_jeion/Downloads/instagram_search.html", "r", encoding="utf-8"
    ) as f:
        page = f.read()

    instagram_link_scrap(page)
