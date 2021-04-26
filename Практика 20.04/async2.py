async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await asyncio.gather(
        say_after(10, 'hello'),
        say_after(20, 'world'))
    
    print(f"started at {time.strftime('%X')}")