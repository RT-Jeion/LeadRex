import nodriver as nd
import asyncio


from pathlib import Path

user_data = Path("./browser_data")
user_data.mkdir(exist_ok=True)


async def main():
    link = "https://sontrungleddsinc.blogspot.com/"
    try:
        browser = await nd.start(headless=False, user_data_dir=user_data)

        page = await asyncio.wait_for(browser.get(link), timeout=10)

        content = await page.get_content()
        print(content)
        print("Success")
    except asyncio.TimeoutError:
        print("Time Out Error")
    except Exception as e:
        print(e)


asyncio.run(main())
