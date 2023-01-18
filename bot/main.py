import chatgpt
import discord

from discord.ext import commands
from bot.data_manager import config

intents = discord.Intents.default()

intents.message_content = True
intents.members = True

bot = commands.AutoShardedBot(command_prefix='//', intents=intents)


@bot.command(name="welcome")
async def welcome(ctx):
    if ctx.author.guild_permissions.administrator:
        await ctx.message.delete()
        embed = discord.Embed(title="Welcome to VR Furs!", description="hold on while we prepare a spot for you",
                              color=0x00ff33)
        embed.set_thumbnail(
            url="https://cdn.discord.me/server/27f886643e4a4bfa497bb87a4338bd21780d0e049ca3fcc0f20fc8555ccdcf76"
                "/icon_544cd79b3ead9b636e9535f77e724fc0831ef1daffd1a5bb827462ca68a808de.jpg")
        embed.add_field(name="Read The Rule", value="While you wait take the time to look over our server rules",
                        inline=False)
        embed.add_field(name="Who are we?",
                        value="We are a community of furries that enjoy hanging out and playing games.", inline=False)
        embed.add_field(name="Safety",
                        value="User safety is highly important to us. We strive to insure a friendly stress free "
                              "envorment for all of our members. ",
                        inline=False)
        embed.add_field(name="Have Fun",
                        value="Once you enter the server introduce yourself, make friends, and have fun!", inline=True)
        await ctx.send(embed=embed)


last_three_msg_bot_chat = []


@bot.listen()
async def on_message(message):
    if message.channel.id == 1062618416768352266:
        last_three_msg_bot_chat.insert(0, message.content)
        if message.author == bot.user:
            return
        await message.channel.send(chatgpt.get_ai_response(message.content)['choices'][0]['text'])
    if message.author == bot.user:
        return


bot.run(config.get_discord_key())
