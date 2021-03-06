import asyncio


async def foo(text):
    raise ValueError


async def faa():
    await asyncio.sleep(1)
    raise SystemError


async def bar(text):
    text = text
    # await faa()
    return text, "completed:" + text


async def main():
    args = ["foo", None, "hello world"]
    task_foo = asyncio.create_task(foo(args[0]))
    task_faa = asyncio.create_task(faa())
    task_bar = asyncio.create_task(bar(args[2]))

    results = await asyncio.gather(
        *[task_foo, task_faa, task_bar], return_exceptions=True
    )
    for index, error in enumerate(results):
        if isinstance(error, ValueError):
            print(f"value error at index {index} with parms {args[index]}")
        elif isinstance(error, SystemError):
            print(f"system error at index {index} with parms {args[index]}")


asyncio.run(main())
