"""async def f():
    print("ASYNC")

"""

import asyncio

async def main():
    print('Hello')
    await asyncio.sleep(1)
    print('world')

asyncio.run(main())