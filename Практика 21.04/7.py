import asyncio

def read_file(file_name):
    return open(file_name, 'r')

async def main():
    loop = asyncio.get_event_loop()
    d= await loop.run_in_executor(None, read_file, 'text.txt')
    print(d)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())