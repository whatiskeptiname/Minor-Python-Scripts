import asyncio
import aiohttp
from names import names
import json


url = "https://httpbin.org/anything?key={}"
results = []


# Add tasks to the list
def get_task(session, names):
    tasks = []
    for name in names[::-1]:
        task = asyncio.create_task(
            session.get(
                url.format(name), headers={"Cache-Control": "no-cache"}, ssl=False
            )
        )
        task.args = name
        tasks.append(task)
    return tasks


async def collect_results(names, data):
    async with aiohttp.ClientSession() as session:
        tasks = get_task(session, names)
        done, pending = await asyncio.wait(tasks)

        for task in done:
            if task.exception():
                print(str(task.exception()))
            else:
                result = await task.result().json()
                args = task.args
                # print("args: " + args + "\n", result, "\n~~~~~~~~~~~~~~~")
                with open("data.json", "w") as f:
                    data[args] = result
                    json.dump(data, f)
                print("Collected: ", args, "\n")
        for task in pending:
            print("pending: ", task)


def save_results():
    with open("data.json") as f:
        try:
            data = json.load(f)
            last_fetched_name = list(data)[-1]
            index_last_fetched_name = names.index(last_fetched_name)
        except:
            data = {}
            index_last_fetched_name = -1
    final_names = names[index_last_fetched_name + 1 : index_last_fetched_name + 3]
    asyncio.run(collect_results(final_names, data))
    return list(data)


if __name__ == "__main__":
    save_results()
