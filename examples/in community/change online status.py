import amino
import asyncio

async def main():
    client = amino.Client()
    await client.login(email="YOUR EMAIL", password="YOUR PASSWORD")
    subclient = await amino.SubClient(aminoId="AMINO ID", profile=client.profile)

    # Online Examples
    # Needs to have "ON" (not case sensitive)
    await subclient.activity_status("ON")
    await subclient.activity_status("on")
    await subclient.activity_status("ONLINE")
    await subclient.activity_status("online")

    # Offline Examples
    # Needs to have "OFF" (not case sensitive)
    await subclient.activity_status("OFF")
    await subclient.activity_status("off")
    await subclient.activity_status("OFFLINE")
    await subclient.activity_status("offline")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())