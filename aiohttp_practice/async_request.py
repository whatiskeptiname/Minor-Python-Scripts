import asyncio
import aiohttp
from names import names
import json


url = "https://httpbin.org/anything?key={}"
results = []


# Add tasks to the list
def get_task(session, names):
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


async def collect_results(names):
    async with aiohttp.ClientSession() as session:
        tasks = get_task(session, names)
        done, pending = await asyncio.wait(tasks)

        for task in done:
            if task.exception():
                print(str(task.exception()))
            else:
                result = await task.result().json()
                args = task.args
                print("Collected: ", args, "\n")
                # print("args: " + args + "\n", result, "\n~~~~~~~~~~~~~~~")
                data[args] = result
                f.seek(0)
                json.dump(data, f)

        for task in pending:
            print("pending: ", task)


with open("data.json", "r+") as f:
    try:
        data = json.load(f)
        last_fetched_name = list(data)[-1]
        index_last_fetched_name = names.index(last_fetched_name)
    except:
        data = {}
        index_last_fetched_name = -1

    for i in range(index_last_fetched_name + 1, index_last_fetched_name + 10, 2):
        final_names = names[i : i + 2]
        asyncio.run(collect_results(final_names))
