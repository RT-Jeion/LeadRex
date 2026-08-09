from browser import main
import asyncio

query = input("Enter User Query:")

asyncio.run(main(user_query=query))
