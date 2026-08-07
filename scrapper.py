import json
from bs4 import BeautifulSoup


def page_scrapper(page_content):
    soup = BeautifulSoup(page_content, "html.parser")
    print("Created Page Soup")

    title = soup.title.string
    print("Page title:", title)

    links = soup.find_all("a")

    with open("leads.json", "r", encoding="utf-8") as f:
        leads = json.load(f)
        len_leads = len(leads)
        print(f"leads.json loeded.. with {len_leads} leads")

    for link in links:
        link_text = link.text.strip()

        link_url = link.get("href")

        if link_text == "Website" and link_url[:4] == "http":
            sub_str = link_url.split(".")
            link_name = sub_str[1]

            print("\nLink Name:", link_name)
            print("Link Url:", link_url)

            lead = {"Name": link_name, "URL": link_url}
            leads.append(lead)

    with open("leads.json", "w", encoding="utf-8") as f:
        json.dump(leads, f, indent=1)
        print("Leads Has been Updated")

    return len(links)


if __name__ == "__main__":
    with open("download.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    page_scrapper(html_content)
