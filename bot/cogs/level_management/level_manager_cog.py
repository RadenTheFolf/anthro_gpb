from discord.ext import commands
from discord import app_commands

import discord
import bot.data_manager.objects.word as WordManager
import bot.data_manager.objects.user as UserManager


def get_level_from_xp(xp):
    xp_scale = 0.25
    growth_rate = 3
    return round(xp_scale*(xp ** (1/growth_rate)))


class LevelManagerCog(commands.Cog):

    level_icons = [
        "",
        "https://i.imgur.com/EeE3sWA.png",
        "https://i.imgur.com/8p1eoHG.png",
        "https://i.imgur.com/18q0iVF.png",
        "https://i.imgur.com/6Kx5ZID.png",
        "https://i.imgur.com/yfkU1dy.png",
        "https://i.imgur.com/3GhRuJc.png",
        "https://i.imgur.com/0b1yeOX.png",
        "https://i.imgur.com/nwBGBq6.png",
        "https://i.imgur.com/lZ7Yhtx.png",
        "https://i.imgur.com/Fxmt0km.png",
        "https://i.imgur.com/NZ5TNXx.png",
        "https://i.imgur.com/KSN0mOl.png",
        "https://i.imgur.com/g7eecAn.png",
        "https://i.imgur.com/SFT6AZZ.png",
        "https://i.imgur.com/oHb8E4D.png",
        "https://i.imgur.com/08zP6sX.png",
        "https://i.imgur.com/v1z02IS.png",
        "https://i.imgur.com/m3VBmgO.png",
        "https://i.imgur.com/rwpbvx7.png",
        "https://i.imgur.com/TJaFnwD.png"
    ]

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener("on_message")
    async def update_levels(self, message: discord.Message) -> None:
        if message.author == self.bot.user:
            return

        words = message.content.split()
        words_processed = 0
        earned_xp = 0
        for word in words:
            if words_processed > 30:
                break
            earned_xp += WordManager.get_word(word).xp
            words_processed += 1

        user = UserManager.get_user(message.author.id)
        if user:
            user.XP += earned_xp
        else:
            author = message.author
            user = UserManager.AGPBUser(author.id, author.name, author.nick, author.joined_at)
            user.XP = earned_xp

        if user.LEVEL < get_level_from_xp(user.XP):
            user.LEVEL += 1
            current_rank = user.LEVEL
            roles = message.guild.roles
            if current_rank > 1:

                for role in roles:
                    if role.name == "Rank {0}".format(current_rank - 1):
                        await message.author.remove_roles(role)
                    if role.name == "Rank {0}".format(current_rank):
                        await message.author.add_roles(role)
            else:
                for role in roles:
                    if role.name == "Rank {0}".format(current_rank):
                        await message.author.add_roles(role)

            embed = discord.Embed()
            embed.title = "{0} has reached Rank {1}".format(message.author.display_name, current_rank)
            embed.set_thumbnail(url=self.level_icons[current_rank])
            embed.set_image(url=message.author.display_avatar.url)
            embed.colour = 0x00f7ff
            embed.description = "Congratulations {0}".format(message.author.display_name)
            await self.bot.get_channel(1062385845790834820).send(content=message.author.mention, embed=embed)
