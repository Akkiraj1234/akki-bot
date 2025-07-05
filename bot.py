# bot.py
import os
import re
import psycopg2
import discord
from discord.ext import commands

# ——— Database Setup ———
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS github (
    user_id TEXT PRIMARY KEY,
    url TEXT
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS leetcode (
    user_id TEXT PRIMARY KEY,
    url TEXT
)
''')
conn.commit()

# ——— Bot Setup ———
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# ——— URL Validator ———
def is_valid_url(url: str, pattern: str):
    if not re.match(pattern, url):
        return False

# ——— Events ———
@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}')

# ——— GitHub Commands ———
@bot.command()
async def setgithub(ctx, url: str = None):
    if not url or not is_valid_url(url, r'^https://github\.com/[A-Za-z0-9_-]+/?$'):
        return await ctx.send('❌ Invalid GitHub URL. Format: `https://github.com/username`')

    cursor.execute(
        'INSERT INTO github(user_id, url) VALUES(%s, %s) ON CONFLICT (user_id) DO UPDATE SET url = EXCLUDED.url',
        (str(ctx.author.id), url)
    )
    conn.commit()
    await ctx.send(f'✅ GitHub saved: {url}')

@bot.command()
async def github(ctx, member: discord.Member = None):
    user = member or ctx.author
    cursor.execute('SELECT url FROM github WHERE user_id = %s', (str(user.id),))
    row = cursor.fetchone()

    if row:
        await ctx.send(f'🔗 **{user.display_name}**’s GitHub: {row[0]}')
    else:
        await ctx.send(f'⚠️ {user.display_name} has not set a GitHub profile.')

# ——— LeetCode Commands ———
@bot.command()
async def setleetcode(ctx, url: str = None):
    pattern = r'^https://leetcode\.com(/u)?/[A-Za-z0-9_-]+/?$'
    if not url or not is_valid_url(url, pattern):
        return await ctx.send(
            '❌ Invalid LeetCode URL.\nValid formats:\n- `https://leetcode.com/username`\n- `https://leetcode.com/u/username/`'
        )

    cursor.execute(
        'INSERT INTO leetcode(user_id, url) VALUES(%s, %s) ON CONFLICT (user_id) DO UPDATE SET url = EXCLUDED.url',
        (str(ctx.author.id), url)
    )
    conn.commit()
    await ctx.send(f'✅ LeetCode saved: {url}')

@bot.command()
async def leetcode(ctx, member: discord.Member = None):
    user = member or ctx.author
    cursor.execute('SELECT url FROM leetcode WHERE user_id = %s', (str(user.id),))
    row = cursor.fetchone()

    if row:
        await ctx.send(f'🧠 **{user.display_name}**’s LeetCode: {row[0]}')
    else:
        await ctx.send(f'⚠️ {user.display_name} has not set a LeetCode profile.')
