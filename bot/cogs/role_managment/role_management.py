from bot.data_manager import config
from discord.ext import commands
from discord import app_commands
import role_views


class RoleCommands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="PopulateRoleChannel",
                          description="Adds a list of role buttons in the roles channel")
    async def populate_role_channel(self, ctx):
        cid = config.get_role_channel()
        channel = ctx.guild.fetch_channel(cid)
        if ctx.author.guild_permissions.administrator:
            await ctx.message.delete()
            view = role_views.relationshipsview(timeout=None)
            await ctx.send("``` Choose roles to match your current relationship status. ```", view=view)
            view = role_views.gamesview(timeout=None)
            await ctx.send("``` Choose roles to match games you play. ```", view=view)
            view = role_views.socialview(timeout=None)
            await ctx.send("``` Choose roles to match your platforms. ```", view=view)
            view = role_views.hobbiesview(timeout=None)
            await ctx.send("``` Choose roles to match your hobbies. ```", view=view)
            view = role_views.programming_languagesview(timeout=None)
            await ctx.send("``` Choose roles to match your programming languages. ```", view=view)
            view = role_views.sexualalityview(timeout=None)
            await ctx.send("``` Choose roles to represent your sexuality. ```", view=view)
            view = role_views.romanceview(timeout=None)
            await ctx.send("``` Choose roles to represent your romantic views. ```", view=view)
            view = role_views.NSFWRoleView(timeout=None)
            await ctx.send("The Mature role is only intended for those 18 and older and grants access to "
                           "NSFW content. **Minors caught with this role will be banned without exception!**",
                           view=view)

    @app_commands.command(name="PurgeRoleChannel",
                          description="Removes all messages from the role channel")
    async def clear_role_channel(self, ctx):
        cid = config.get_role_channel()
        channel = ctx.guild.fetch_channel(cid)
        if ctx.author.guild_permissions.administrator:
            await channel.purge(limit=10)



