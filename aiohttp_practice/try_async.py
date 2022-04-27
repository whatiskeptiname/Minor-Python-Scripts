import asyncio


async def good():
    return "OK"


async def value_error():
    raise ValueError()


async def connection_error():
    raise ConnectionError()


async def main():
    responses = await asyncio.gather(good(), connection_error())
    print(responses)


try:
    asyncio.run(main())
except ValueError:
    print("ValueError")
except ConnectionError:
    print("ConnectionError")
