import asyncio

exceptions = [
    ValueError,
    SystemError,
]


async def foo():
    raise ValueError


async def faa():
    await asyncio.sleep(1)
    raise SystemError


async def bar(text):
    text = text
    try:
        await asyncio.sleep(1)
        await faa()
        return text, "completed:" + text
    except SystemError:
        print("Bar Cancelled.")
        return text


async def main():
    task_foo = asyncio.create_task(foo())
    task_faa = asyncio.create_task(faa())
    task_bar = asyncio.create_task(bar(text="hello world"))

    results = await asyncio.gather(
        *[task_foo, task_faa, task_bar], return_exceptions=True
    )
    print(results)
    failed_task = [result for result in results if isinstance(result, Exception)]
    for error in failed_task:
        if isinstance(error, ValueError):
            print("ValueError!!!!!!!!")
        elif isinstance(error, SystemError):
            parms = results[2]
            print("parms:", parms)


asyncio.run(main())
