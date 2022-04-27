import asyncio
import aiohttp
from names import names


url = "https://www.boredapi.com/api/activity"
results = []

# Add tasks to the list
def get_task(session):
    tasks = []
    for _ in range(3):
        tasks.append(asyncio.create_task(session.get(url, ssl=False)))
    return tasks


# main funciton run the tasks
async def get_symbols():
    async with aiohttp.ClientSession() as session:
        tasks = get_task(session)
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        for response in responses:
            results.append(await response.json())


# Event Loop
try:
    asyncio.run(get_symbols())
    print(results)

except Exception:
    print("something wrong occured")
