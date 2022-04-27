import asyncio


async def foo():
    raise ValueError("Foo value error")
    return "Foo finished"


async def bar():
    await asyncio.sleep(1)
    return "Bar finished"


async def main():
    foo_task = asyncio.create_task(foo(), name="Exception_task")
    bar_task = asyncio.create_task(bar(), name="Waiting_task")
    try:
        done, pending = await asyncio.wait(
            [foo_task, bar_task], return_when=asyncio.ALL_COMPLETED
        )
        for task in done:
            name = task.get_name()
            print(f"DONE: {name}")
            exception = task.exception()
            if isinstance(exception, Exception):
                print(f"{name} threw {exception}")
            try:
                result = task.result()
                print(f"{name} returned {result}")
            except ValueError as e:
                print(f"ValueError: {e}")
        for task in pending:
            task.cancel()
    except Exception as e:
        print("Outer Exception")


asyncio.run(main())
