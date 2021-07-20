import amino
import asyncio

async def main():
    client = amino.Client()
    await client.login(email="YOUR EMAIL", password="YOUR PASSWORD")

    # Follow
    await client.follow("USER ID")

    # Unfollow
    await client.unfollow("USER ID")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())