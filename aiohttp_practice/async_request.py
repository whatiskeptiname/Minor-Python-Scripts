import asyncio
import random
import aiohttp
from names import names


url = "https://httpbin.org/anything?key={}"
results = []

names = random.choices(names, k=2)

# Add tasks to the list
def get_task(session):
    tasks = []
    for name in names:
        task = asyncio.create_task(
            session.get(
                url.format(name), headers={"Cache-Control": "no-cache"}, ssl=False
            )
        )
        task.args = name
        tasks.append(task)
    return tasks


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = get_task(session)
        done, pending = await asyncio.wait(tasks)

        for task in done:
            if task.exception():
                print(str(task.exception()))
            else:
                result = await task.result().json()
                args = task.args

                print("args: " + args + "\n", result, "\n~~~~~~~~~~~~~~~")

        for task in pending:
            print("pending: ", task)


asyncio.run(main())
