import amino
import asyncio

async def main():
    client = amino.Client()
    await client.login(email="YOUR EMAIL", password="YOUR PASSWORD")
    subclient = await amino.SubClient(aminoId="AMINO ID", profile=client.profile)

    # Send Images
    with open("file.png", "rb") as file:
        await subclient.send_message(chatId="CHAT ID", file=file)
    
    # Send Audios
    with open("file.mp3", "rb") as file:
        await subclient.send_message(chatId="CHAT ID", file=file, fileType="audio")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())