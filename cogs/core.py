import discord
from discord import app_commands
from discord.ext import commands

class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f"Pong! {int(self.bot.latency * 1000)}ms"
        )

async def setup(bot):
    await bot.add_cog(Core(bot))
