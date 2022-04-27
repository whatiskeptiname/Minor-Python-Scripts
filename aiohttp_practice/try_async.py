import asyncio


async def good():
    return "OK"


async def bad():
    raise ValueError()


async def main():
    responses = await asyncio.gather(bad(), good(), bad(), return_exceptions=True)
    print(responses)


asyncio.run(main())
