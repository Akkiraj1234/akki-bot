import asyncio
from aiohttp import web
from pathlib import Path

_shutdown_event = asyncio.Event()

def create_app():
    app = web.Application()
    root_dir = Path(__file__).parent.parent
    app.router.add_static('/static/', root_dir / 'webpage/static', name='static')
    app.router.add_static('/resource/', root_dir / 'resource', name='resource')

    async def index(request):
        return web.FileResponse(root_dir / 'webpage/index.html')
    app.router.add_get('/', index)
    return app

async def start_server():
    app = create_app()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', port=8000)
    await site.start()
    print("🌐 Aiohttp server running at http://localhost:8000")

    try:
        await _shutdown_event.wait()  # Wait until shutdown is triggered
    finally:
        print("🛑 Server shutting down...")
        await runner.cleanup()

def stop_server():
    _shutdown_event.set()
    
    
if __name__ == "__main__":
    import asyncio
    try:
        asyncio.run(start_server())
    except KeyboardInterrupt:
        print("🧹 Server stopped manually.")

