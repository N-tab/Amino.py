import amino
import asyncio

async def main():
    client = amino.Client()
    await client.login(email="YOUR EMAIL", password="YOUR PASSWORD")

    objectId = (await client.get_from_code("https://aminoapps.com/p/EXAMPLE")).objectId
    print(objectId)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())