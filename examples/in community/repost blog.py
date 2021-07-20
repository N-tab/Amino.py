import amino
import asyncio

async def main():
    client = amino.Client()
    await client.login(email="YOUR EMAIL", password="YOUR PASSWORD")
    subclient = await amino.SubClient(aminoId="AMINO ID", profile=client.profile)

    await subclient.repost_blog(blogId="BLOG ID", content="CONTENT")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())