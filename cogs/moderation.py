import discord
from discord import app_commands
from discord.ext import commands
import aiosqlite

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="warn")
    async def warn(self, interaction: discord.Interaction, user: discord.Member, reason: str):
        async with aiosqlite.connect("database.sqlite3") as db:
            await db.execute(
                "INSERT INTO warnings (guild_id, user_id, reason) VALUES (?, ?, ?)",
                (interaction.guild.id, user.id, reason)
            )
            await db.commit()
        await interaction.response.send_message(f"{user.mention} warned.")

async def setup(bot):
    await bot.add_cog(Moderation(bot))
