import asyncio


async def foo():
    raise ValueError("Foo value error.")


async def bar():
    try:
        await asyncio.sleep(1)
        return "Bar finished."
    except asyncio.CancelledError:
        print("Bar Cancelled.")


async def main():

    try:
        results = await asyncio.gather(foo(), bar())
        print(results)
    except ValueError as e:
        print(e)


asyncio.run(main())
