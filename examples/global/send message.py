import amino
import asyncio

async def main():
    client = amino.Client()
    await client.login(email="YOUR EMAIL", password="YOUR PASSWORD")

    await client.send_message(chatId="CHAT ID", message="MESSAGE")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())