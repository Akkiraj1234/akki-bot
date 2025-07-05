# import os
# import psycopg2
# from discord.ext import commands
# from flask import Flask
# from threading import Thread

# # ——— Database Setup ———
# DATABASE_URL = os.environ['DATABASE_URL']
# conn = psycopg2.connect(DATABASE_URL, sslmode='require')
# c = conn.cursor()
# c.execute('''
#   CREATE TABLE IF NOT EXISTS github (
#     user_id TEXT PRIMARY KEY,
#     url TEXT
#   )
# ''')
# conn.commit()

# # ——— Bot Setup ———
# intents = commands.Intents.default()
# intents.message_content = True
# bot = commands.Bot(command_prefix='!', intents=intents)

# @bot.event
# async def on_ready():
#     print(f'Logged in as {bot.user}')

# @bot.command()
# async def setgithub(ctx, url: str = None):
#     if not url:
#         return await ctx.send('⚠️ Usage: `!setgithub https://github.com/yourusername`')
#     c.execute(
#       'INSERT INTO github(user_id,url) VALUES(%s,%s) ON CONFLICT (user_id) DO UPDATE SET url = EXCLUDED.url',
#       (str(ctx.author.id), url)
#     )
#     conn.commit()
#     await ctx.send(f'✅ Saved your GitHub link: {url}')

# @bot.command()
# async def github(ctx, member: commands.MemberConverter = None):
#     user = member or ctx.author
#     c.execute('SELECT url FROM github WHERE user_id = %s', (str(user.id),))
#     row = c.fetchone()
#     if row:
#         await ctx.send(f'🔗 {user.display_name}’s GitHub: {row[0]}')
#     else:
#         await ctx.send(f'⚠️ {user.display_name} has not set a GitHub yet.')

# # ——— Keep-alive Web Server ———
# app = Flask('')

# @app.route('/')
# def home():
#     return 'Bot is running on Render!'

# Thread(target=lambda: app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))).start()

# # ——— Run Bot ———
# bot.run(os.environ['DISCORD_TOKEN'])
import os
import psycopg2
import discord  # ✅ Required for Intents
from discord.ext import commands
from flask import Flask
from threading import Thread

# ——— Database Setup ———
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
c = conn.cursor()
c.execute('''
  CREATE TABLE IF NOT EXISTS github (
    user_id TEXT PRIMARY KEY,
    url TEXT
  )
''')
conn.commit()

# ——— Bot Setup ———
intents = discord.Intents.default()
intents.message_content = True  # Needed to read user messages
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}')

@bot.command()
async def setgithub(ctx, url: str = None):
    if not url:
        return await ctx.send('⚠️ Usage: `!setgithub https://github.com/yourusername`')
    c.execute(
        'INSERT INTO github(user_id, url) VALUES(%s, %s) ON CONFLICT (user_id) DO UPDATE SET url = EXCLUDED.url',
        (str(ctx.author.id), url)
    )
    conn.commit()
    await ctx.send(f'✅ Saved your GitHub link: {url}')

@bot.command()
async def github(ctx, member: discord.Member = None):
    user = member or ctx.author
    c.execute('SELECT url FROM github WHERE user_id = %s', (str(user.id),))
    row = c.fetchone()
    if row:
        await ctx.send(f'🔗 {user.display_name}’s GitHub: {row[0]}')
    else:
        await ctx.send(f'⚠️ {user.display_name} has not set a GitHub yet.')

# ——— Keep-alive Web Server (for Render pinging) ———
app = Flask('')

@app.route('/')
def home():
    return '✅ Bot is running on Render!'

# Start Flask server in a separate thread
Thread(target=lambda: app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))).start()

# ——— Run the Bot ———
bot.run(os.environ['DISCORD_TOKEN'])
