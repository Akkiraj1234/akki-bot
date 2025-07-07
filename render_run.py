import asyncio
from server.app import start_server
from akkibot.bot import run_bot_main

async def main():
    # Run both server and bot concurrently
    server_task = asyncio.create_task(start_server())
    bot_task = asyncio.create_task(run_bot_main())

    await asyncio.gather(server_task, bot_task)

if __name__ == "__main__":
    print("🚀 Starting AkkiBot system...")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("🛑 AkkiBot system shutdown.")
