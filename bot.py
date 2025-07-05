# bot.py
import os
import re
import requests
import psycopg2
import discord
from discord.ext import commands

# DB Setup
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
c = conn.cursor()

# Table creation
c.execute('''
CREATE TABLE IF NOT EXISTS github (
    user_id TEXT PRIMARY KEY,
    url TEXT
)
''')
c.execute('''
CREATE TABLE IF NOT EXISTS leetcode (
    user_id TEXT PRIMARY KEY,
    url TEXT
)
''')
conn.commit()

# Intents & Bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# URL Validator
def is_valid_url(url: str, pattern: str):
    if not re.match(pattern, url):
        return False
    try:
        res = requests.get(url, timeout=5)
        return res.status_code == 200
    except:
        return False

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}')

@bot.command()
async def setgithub(ctx, url: str = None):
    if not url or not is_valid_url(url, r'^https://github\.com/[A-Za-z0-9_-]+/?$'):
        return await ctx.send('❌ Invalid GitHub URL. Format: `https://github.com/username`')
    c.execute(
        'INSERT INTO github(user_id, url) VALUES(%s, %s) ON CONFLICT (user_id) DO UPDATE SET url = EXCLUDED.url',
        (str(ctx.author.id), url)
    )
    conn.commit()
    await ctx.send(f'✅ GitHub saved: {url}')

@bot.command()
async def github(ctx, member: discord.Member = None):
    user = member or ctx.author
    c.execute('SELECT url FROM github WHERE user_id = %s', (str(user.id),))
    row = c.fetchone()
    if row:
        await ctx.send(f'🔗 {user.display_name}’s GitHub: {row[0]}')
    else:
        await ctx.send(f'⚠️ {user.display_name} has not set a GitHub yet.')

@bot.command()
async def setleetcode(ctx, url: str = None):
    if not url or not is_valid_url(url, r'^https://leetcode\.com/[A-Za-z0-9_-]+/?$'):
        return await ctx.send('❌ Invalid LeetCode URL. Format: `https://leetcode.com/username`')
    c.execute(
        'INSERT INTO leetcode(user_id, url) VALUES(%s, %s) ON CONFLICT (user_id) DO UPDATE SET url = EXCLUDED.url',
        (str(ctx.author.id), url)
    )
    conn.commit()
    await ctx.send(f'✅ LeetCode saved: {url}')

@bot.command()
async def leetcode(ctx, member: discord.Member = None):
    user = member or ctx.author
    c.execute('SELECT url FROM leetcode WHERE user_id = %s', (str(user.id),))
    row = c.fetchone()
    if row:
        await ctx.send(f'🧠 {user.display_name}’s LeetCode: {row[0]}')
    else:
        await ctx.send(f'⚠️ {user.display_name} has not set a LeetCode yet.')
