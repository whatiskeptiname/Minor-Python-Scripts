import asyncio
import aiohttp
from futures3 import FIRST_COMPLETED, FIRST_EXCEPTION


url = "https://www.boredapi.com/api/activity"
results = []


# Add tasks to the list
def get_task(session):
    tasks = []
    for _ in range(9):
        tasks.append(asyncio.create_task(session.get(url, ssl=False)))
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
                print(task.result())
        for task in pending:
            print("pending: ", task)


asyncio.run(main())
