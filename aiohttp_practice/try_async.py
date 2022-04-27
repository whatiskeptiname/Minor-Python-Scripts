import asyncio

exceptions = [
    ValueError,
    SystemError,
]


async def foo():
    raise ValueError


async def faa():
    raise SystemError


async def bar():
    try:
        await asyncio.sleep(1)
        return "Bar finished."
    except asyncio.CancelledError:
        print("Bar Cancelled.")


async def main():
    results = await asyncio.gather(foo(), bar(), faa(), return_exceptions=True)
    print(results)
    failed_task = [result for result in results if isinstance(result, Exception)]
    print(failed_task)
    for error in failed_task:
        if isinstance(error, ValueError):
            print("ValueError!!!!!!!!")
        elif isinstance(error, SystemError):
            print("SystemError!!!!!!!!")


asyncio.run(main())
