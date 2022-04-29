import asyncio
import random
import aiohttp
from names import names


url = "https://api.nationalize.io?name={}"
results = []

names = random.choices(names, k=3)

# Add tasks to the list
def get_task(session):
    tasks = []
    for name in names:
        tasks.append(asyncio.create_task(session.get(url.format(name), ssl=False)))
    return tasks


# main funciton run the tasks
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = get_task(session)
        done, pending = await asyncio.wait(tasks)

        for task in done:
            if task.exception():
                print(str(task.exception()))
            else:
                print(await task.result().json())
        for task in pending:
            print("pending: ", task)


asyncio.run(main())
