import amino
import asyncio

async def main():
    client = amino.Client()
    await client.login(email="YOUR EMAIL", password="YOUR PASSWORD")

    # Block
    await client.block("USER ID")

    # Unblock
    await client.unblock("USER ID")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())