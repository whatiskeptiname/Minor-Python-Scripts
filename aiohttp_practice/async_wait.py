import asyncio

from tenacity import retry


async def foo(text):
    raise ValueError
    return text


async def faa():
    await asyncio.sleep(2)
    raise SystemError
    return "faa"


async def bar(text):
    return text


async def main():
    args = ["foo", None, "hello world"]
    task_foo = asyncio.create_task(foo(args[0]))
    task_faa = asyncio.create_task(faa())
    task_bar = asyncio.create_task(bar(args[2]))
    tasks = [task_foo, task_faa, task_bar]

    done, pending = await asyncio.wait(tasks)
    for task in done:
        if task.exception():
            print(type(task.exception()))
        else:
            print(task.result())
    for task in pending:
        print("pending: ", task)


asyncio.run(main())
