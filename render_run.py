from threading import Thread
import asyncio

print("🚀 Starting AkkiBot system...")

# === Run server ===
def run_server():
    import server.app  # Import only inside to avoid threading issues
    asyncio.run(server.app.start_server())

# === Run bot ===
def run_bot():
    from akkibot.bot import run_bot_main
    run_bot_main()

# === Start both ===
Thread(target=run_server).start()
run_bot()  # Runs in main thread
