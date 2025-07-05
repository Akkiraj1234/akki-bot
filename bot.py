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

# Create tables if they don't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS github (
    user_id TEXT PRIMARY KEY,
    url TEXT
);
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS leetcode (
    user_id TEXT PRIMARY KEY,
    url TEXT
);
''')
conn.commit()
print("✅ PostgreSQL tables ensured.")

# ——— Bot Setup ———
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# ——— URL Validator ———
def is_valid_url(url: str, pattern: str) -> bool:
    match = re.fullmatch(pattern, url)
    is_valid = bool(match)
    print(f"[URL CHECK] {url} → {'VALID' if is_valid else 'INVALID'}")
    return is_valid

# ——— Events ———
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

# ——— GitHub Commands ———
@bot.command()
async def setgithub(ctx, url: str = None):
    print(f"[COMMAND] !setgithub by {ctx.author} | URL: {url}")
    pattern = r'https://github\.com/[A-Za-z0-9_-]+/?'
    if not url or not is_valid_url(url, pattern):
        return await ctx.send(
            '❌ Invalid GitHub URL.\nFormat: `https://github.com/username`'
        )

    cursor.execute(
        '''
        INSERT INTO github (user_id, url)
        VALUES (%s, %s)
        ON CONFLICT (user_id) DO
          UPDATE SET url = EXCLUDED.url
        ''',
        (str(ctx.author.id), url)
    )
    conn.commit()
    print(f"[DATABASE] GitHub URL saved for {ctx.author}")
    await ctx.send(f'✅ GitHub saved: {url}')

@bot.command()
async def github(ctx, member: discord.Member = None):
    user = member or ctx.author
    print(f"[COMMAND] !github by {ctx.author} | Target: {user}")
    cursor.execute(
        'SELECT url FROM github WHERE user_id = %s',
        (str(user.id),)
    )
    row = cursor.fetchone()

    if row:
        await ctx.send(f'🔗 **{user.display_name}**’s GitHub: {row[0]}')
    else:
        await ctx.send(f'⚠️ {user.display_name} has not set a GitHub profile.')

# ——— LeetCode Commands ———
@bot.command()
async def setleetcode(ctx, url: str = None):
    print(f"[COMMAND] !setleetcode by {ctx.author} | URL: {url}")
    # Accept both /username and /u/username/ formats
    pattern = r'https://leetcode\.com(?:/u)?/[A-Za-z0-9_-]+/?'
    if not url or not is_valid_url(url, pattern):
        return await ctx.send(
            '❌ Invalid LeetCode URL.\n'
            'Valid formats:\n'
            '- `https://leetcode.com/username`\n'
            '- `https://leetcode.com/u/username/`'
        )

    cursor.execute(
        '''
        INSERT INTO leetcode (user_id, url)
        VALUES (%s, %s)
        ON CONFLICT (user_id) DO
          UPDATE SET url = EXCLUDED.url
        ''',
        (str(ctx.author.id), url)
    )
    conn.commit()
    print(f"[DATABASE] LeetCode URL saved for {ctx.author}")
    await ctx.send(f'✅ LeetCode saved: {url}')

@bot.command()
async def leetcode(ctx, member: discord.Member = None):
    user = member or ctx.author
    print(f"[COMMAND] !leetcode by {ctx.author} | Target: {user}")
    cursor.execute(
        'SELECT url FROM leetcode WHERE user_id = %s',
        (str(user.id),)
    )
    row = cursor.fetchone()

    if row:
        await ctx.send(f'🧠 **{user.display_name}**’s LeetCode: {row[0]}')
    else:
        await ctx.send(f'⚠️ {user.display_name} has not set a LeetCode profile.')
