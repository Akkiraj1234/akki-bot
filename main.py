# main.py
from flask import Flask
from threading import Thread
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '✅ Flask + Discord bot running.'

# Start bot in a background thread
def run_bot():
    from bot import bot
    bot.run(os.environ['DISCORD_TOKEN'])

if __name__ == '__main__':
    Thread(target=run_bot).start()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
