import amino
import asyncio

client = amino.Client()

async def main():
    await client.login(email="YOUR EMAIL", password="YOUR PASSWORD")
    await client.session.close()

@client.event("on_text_message")
async def on_text_message(data):
    print(f"{data.message.author.nickname}: {data.message.content}")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
