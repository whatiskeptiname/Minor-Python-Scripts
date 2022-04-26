import asyncio
from asyncio import tasks
import aiohttp
import os


api_key = os.getenv("ALPHAVANTAGE_API_KEY")
url = "https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}"
symbols = [
    "AAPL",
    "GOOG",
    "TSLA",
    "MSFT",
    "PEP",
    "AAPL",
    "GOOG",
    "TSLA",
    "MSFT",
    "PEP",
    "AAPL",
    "GOOG",
    "TSLA",
    "MSFT",
    "PEP",
    "AAPL",
    "GOOG",
    "TSLA",
    "MSFT",
    "PEP",
    "AAPL",
    "GOOG",
    "TSLA",
    "MSFT",
    "PEP",
    "AAPL",
    "GOOG",
    "TSLA",
    "MSFT",
    "PEP",
]
results = []

# Add tasks to the list
def get_task(session):
    tasks = []
    for symbol in symbols:
        tasks.append(
            asyncio.create_task(session.get(url.format(symbol, api_key), ssl=False))
        )
        return tasks


print(tasks)

# main funciton run the tasks
async def get_symbols():
    async with aiohttp.ClientSession() as session:
        tasks = get_task(session)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            results.append(await response.json())


# Event Loop
asyncio.run(get_symbols())
print(results)
