from aiohttp import web
from pathlib import Path
import asyncio
import signal

# === Create aiohttp app ===
def create_app():
    app = web.Application()
    root_dir = Path(__file__).parent.parent
    
    # Static file routing (frontend)
    app.router.add_static('/static/', path= root_dir/"webpage/static", name='static')
    app.router.add_static('/resource/', path= root_dir/"resource", name='resource')

    # Index page
    async def index(request):
        return web.FileResponse(root_dir/'webpage/index.html')
    app.router.add_get('/', index)

    return app

# === Run aiohttp server ===
async def start_server():
    app = create_app()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host='0.0.0.0', port=8000)
    await site.start()
    print("🌐 Aiohttp server running at http://localhost:8000")

    # Keep running until interrupted
    stop_event = asyncio.Event()

    # Register shutdown on Ctrl+C
    loop = asyncio.get_running_loop()
    loop.add_signal_handler(signal.SIGINT, stop_event.set)
    loop.add_signal_handler(signal.SIGTERM, stop_event.set)

    await stop_event.wait()
    print("🛑 Shutting down...")

    await runner.cleanup()

if __name__ == "__main__":
    try:
        asyncio.run(start_server())
    except KeyboardInterrupt:
        print("🧹 Server stopped manually.")
