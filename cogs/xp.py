import discord
from discord.ext import commands
import aiosqlite

class XP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        async with aiosqlite.connect("database.sqlite3") as db:
            await db.execute("""
            INSERT INTO xp (guild_id, user_id, xp)
            VALUES (?, ?, 10)
            ON CONFLICT(guild_id, user_id)
            DO UPDATE SET xp = xp + 10
            """, (message.guild.id, message.author.id))
            await db.commit()

async def setup(bot):
    await bot.add_cog(XP(bot))
