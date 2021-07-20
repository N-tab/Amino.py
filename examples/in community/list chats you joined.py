import amino
import asyncio

async def main():
    client = amino.Client()
    await client.login(email="YOUR EMAIL", password="YOUR PASSWORD")
    subclient = await amino.SubClient(aminoId="AMINO ID", profile=client.profile)

    chats = await subclient.get_chat_threads()
    for chatName, chatId in zip(chats.title, chats.chatId):
        print(chatName, chatId)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())