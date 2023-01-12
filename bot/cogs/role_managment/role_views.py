import discord


class NSFWRoleView(discord.ui.View):
    @discord.ui.button(label="Access 18+", style=discord.ButtonStyle.danger)
    async def add_nsfw_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = interaction.guild.get_role(1062502248623657052)
        if interaction.user.get_role(1062502248623657052):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The 'Mature' Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="You have been given the 'Mature' Role",
                ephemeral=True,
                delete_after=60,
            )


class relationshipsview(discord.ui.View):
    def get_role_id_from_name(self, interaction, name):
        roles = interaction.guild.roles
        for role in roles:
            if role.name == "{}".format(name):
                return role
        return

    @discord.ui.button(label="Taken", style=discord.ButtonStyle.primary)
    async def add_Taken_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Taken")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Taken Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Taken Role has been added", ephemeral=True, delete_after=60
            )

    @discord.ui.button(label="Single", style=discord.ButtonStyle.primary)
    async def add_Single_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Single")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Single Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Single Role has been added",
                ephemeral=True,
                delete_after=60,
            )

    @discord.ui.button(label="Looking", style=discord.ButtonStyle.primary)
    async def add_Looking_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Looking")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Looking Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Looking Role has been added",
                ephemeral=True,
                delete_after=60,
            )

    @discord.ui.button(label="Not Looking", style=discord.ButtonStyle.primary)
    async def add_Not_Looking_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Not Looking")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Not Looking Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Not Looking Role has been added",
                ephemeral=True,
                delete_after=60,
            )

    @discord.ui.button(label="Polyamorous", style=discord.ButtonStyle.primary)
    async def add_Polyamorous_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Polyamorous")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Polyamorous Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Polyamorous Role has been added",
                ephemeral=True,
                delete_after=60,
            )


class gamesview(discord.ui.View):
    def get_role_id_from_name(self, interaction, name):
        roles = interaction.guild.roles
        for role in roles:
            if role.name == "{}".format(name):
                return role
        return

    @discord.ui.button(label="VRChat", style=discord.ButtonStyle.secondary)
    async def add_VRChat_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "VRChat")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The VRChat Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The VRChat Role has been added",
                ephemeral=True,
                delete_after=60,
            )

    @discord.ui.button(label="Satisfactory", style=discord.ButtonStyle.secondary)
    async def add_Satisfactory_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Satisfactory")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Satisfactory Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Satisfactory Role has been added",
                ephemeral=True,
                delete_after=60,
            )

    @discord.ui.button(label="Minecraft", style=discord.ButtonStyle.secondary)
    async def add_Minecraft_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Minecraft")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Minecraft Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Minecraft Role has been added",
                ephemeral=True,
                delete_after=60,
            )


class socialview(discord.ui.View):
    def get_role_id_from_name(self, interaction, name):
        roles = interaction.guild.roles
        for role in roles:
            if role.name == "{}".format(name):
                return role
        return

    @discord.ui.button(label="Youtube", style=discord.ButtonStyle.success)
    async def add_Youtube_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Youtube")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Youtube Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Youtube Role has been added",
                ephemeral=True,
                delete_after=60,
            )

    @discord.ui.button(label="Twitch", style=discord.ButtonStyle.success)
    async def add_Twitch_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Twitch")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Twitch Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Twitch Role has been added",
                ephemeral=True,
                delete_after=60,
            )

    @discord.ui.button(label="Streamer", style=discord.ButtonStyle.success)
    async def add_Streamer_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Streamer")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Streamer Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Streamer Role has been added",
                ephemeral=True,
                delete_after=60,
            )


class hobbiesview(discord.ui.View):
    def get_role_id_from_name(self, interaction, name):
        roles = interaction.guild.roles
        for role in roles:
            if role.name == "{}".format(name):
                return role
        return

    @discord.ui.button(label="Animator", style=discord.ButtonStyle.primary)
    async def add_Animator_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Animator")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Animator Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Animator Role has been added",
                ephemeral=True,
                delete_after=60,
            )

    @discord.ui.button(label="2D Artist", style=discord.ButtonStyle.primary)
    async def add_2D_Artist_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "2D Artist")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The 2D Artist Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The 2D Artist Role has been added",
                ephemeral=True,
                delete_after=60,
            )

    @discord.ui.button(label="3D Artist", style=discord.ButtonStyle.primary)
    async def add_3D_Artist_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "3D Artist")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The 3D Artist Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The 3D Artist Role has been added",
                ephemeral=True,
                delete_after=60,
            )

    @discord.ui.button(label="Musician", style=discord.ButtonStyle.primary)
    async def add_Musician_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Musician")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Musician Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Musician Role has been added",
                ephemeral=True,
                delete_after=60,
            )

    @discord.ui.button(label="Programmer", style=discord.ButtonStyle.primary)
    async def add_Programmer_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Programmer")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Programmer Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Programmer Role has been added",
                ephemeral=True,
                delete_after=60,
            )

    @discord.ui.button(label="Game Developer", style=discord.ButtonStyle.primary)
    async def add_Game_Developer_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Game Developer")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Game Developer Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Game Developer Role has been added",
                ephemeral=True,
                delete_after=60,
            )


class programming_languagesview(discord.ui.View):
    def get_role_id_from_name(self, interaction, name):
        roles = interaction.guild.roles
        for role in roles:
            if role.name == "{}".format(name):
                return role
        return

    @discord.ui.button(label="c-c++", style=discord.ButtonStyle.secondary)
    async def add_c_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "c-c++")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The c-c++ Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The c-c++ Role has been added", ephemeral=True, delete_after=60
            )

    @discord.ui.button(label="c#", style=discord.ButtonStyle.secondary)
    async def add_cs_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "c#")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The c# Role has been removed", ephemeral=True, delete_after=60
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The c# Role has been added", ephemeral=True, delete_after=60
            )

    @discord.ui.button(label="Java", style=discord.ButtonStyle.secondary)
    async def add_Java_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Java")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Java Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Java Role has been added", ephemeral=True, delete_after=60
            )

    @discord.ui.button(label="JS", style=discord.ButtonStyle.secondary)
    async def add_JS_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "JS")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The JS Role has been removed", ephemeral=True, delete_after=60
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The JS Role has been added", ephemeral=True, delete_after=60
            )

    @discord.ui.button(label="Lua", style=discord.ButtonStyle.secondary)
    async def add_Lua_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Lua")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Lua Role has been removed", ephemeral=True, delete_after=60
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Lua Role has been added", ephemeral=True, delete_after=60
            )

    @discord.ui.button(label="Python", style=discord.ButtonStyle.secondary)
    async def add_Python_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Python")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Python Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Python Role has been added",
                ephemeral=True,
                delete_after=60,
            )

    @discord.ui.button(label="Rust", style=discord.ButtonStyle.secondary)
    async def add_Rust_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Rust")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Rust Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Rust Role has been added", ephemeral=True, delete_after=60
            )


class sexualalityview(discord.ui.View):
    def get_role_id_from_name(self, interaction, name):
        roles = interaction.guild.roles
        for role in roles:
            if role.name == "{}".format(name):
                return role
        return

    @discord.ui.button(label="Asexual", style=discord.ButtonStyle.success)
    async def add_Asexual_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Asexual")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Asexual Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Asexual Role has been added",
                ephemeral=True,
                delete_after=60,
            )

    @discord.ui.button(label="Bisexual", style=discord.ButtonStyle.success)
    async def add_Bisexual_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Bisexual")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Bisexual Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Bisexual Role has been added",
                ephemeral=True,
                delete_after=60,
            )

    @discord.ui.button(label="Demisexual", style=discord.ButtonStyle.success)
    async def add_Demisexual_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Demisexual")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Demisexual Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Demisexual Role has been added",
                ephemeral=True,
                delete_after=60,
            )

    @discord.ui.button(label="Graysexual", style=discord.ButtonStyle.success)
    async def add_Graysexual_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Graysexual")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Graysexual Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Graysexual Role has been added",
                ephemeral=True,
                delete_after=60,
            )

    @discord.ui.button(label="Pansexual", style=discord.ButtonStyle.success)
    async def add_Pansexual_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Pansexual")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Pansexual Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Pansexual Role has been added",
                ephemeral=True,
                delete_after=60,
            )

    @discord.ui.button(label="Heterosexual", style=discord.ButtonStyle.success)
    async def add_Heterosexual_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Heterosexual")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Heterosexual Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Heterosexual Role has been added",
                ephemeral=True,
                delete_after=60,
            )

    @discord.ui.button(label="Homosexual", style=discord.ButtonStyle.success)
    async def add_Homosexual_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Homosexual")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Homosexual Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Homosexual Role has been added",
                ephemeral=True,
                delete_after=60,
            )

    @discord.ui.button(label="Omnisexual", style=discord.ButtonStyle.success)
    async def add_Omnisexual_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Omnisexual")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Omnisexual Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Omnisexual Role has been added",
                ephemeral=True,
                delete_after=60,
            )

    @discord.ui.button(label="Polysexual", style=discord.ButtonStyle.success)
    async def add_Polysexual_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Polysexual")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Polysexual Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Polysexual Role has been added",
                ephemeral=True,
                delete_after=60,
            )


class romanceview(discord.ui.View):
    def get_role_id_from_name(self, interaction, name):
        roles = interaction.guild.roles
        for role in roles:
            if role.name == "{}".format(name):
                return role
        return

    @discord.ui.button(label="Aromantic", style=discord.ButtonStyle.primary)
    async def add_Aromantic_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Aromantic")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Aromantic Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Aromantic Role has been added",
                ephemeral=True,
                delete_after=60,
            )

    @discord.ui.button(label="Biromantic", style=discord.ButtonStyle.primary)
    async def add_Biromantic_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Biromantic")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Biromantic Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Biromantic Role has been added",
                ephemeral=True,
                delete_after=60,
            )

    @discord.ui.button(label="Heteroromantic", style=discord.ButtonStyle.primary)
    async def add_Heteroromantic_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Heteroromantic")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Heteroromantic Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Heteroromantic Role has been added",
                ephemeral=True,
                delete_after=60,
            )

    @discord.ui.button(label="Homoromantic", style=discord.ButtonStyle.primary)
    async def add_Homoromantic_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Homoromantic")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Homoromantic Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Homoromantic Role has been added",
                ephemeral=True,
                delete_after=60,
            )

    @discord.ui.button(label="Panromantic", style=discord.ButtonStyle.primary)
    async def add_Panromantic_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Panromantic")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Panromantic Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Panromantic Role has been added",
                ephemeral=True,
                delete_after=60,
            )

    @discord.ui.button(label="Polyromantic", style=discord.ButtonStyle.primary)
    async def add_Polyromantic_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Polyromantic")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Polyromantic Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Polyromantic Role has been added",
                ephemeral=True,
                delete_after=60,
            )

    @discord.ui.button(label="Grayromantic", style=discord.ButtonStyle.primary)
    async def add_Grayromantic_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Grayromantic")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Grayromantic Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Grayromantic Role has been added",
                ephemeral=True,
                delete_after=60,
            )

    @discord.ui.button(label="Demiromantic", style=discord.ButtonStyle.primary)
    async def add_Demiromantic_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Demiromantic")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Demiromantic Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Demiromantic Role has been added",
                ephemeral=True,
                delete_after=60,
            )

    @discord.ui.button(label="Omniromantic", style=discord.ButtonStyle.primary)
    async def add_Omniromantic_role(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        role = self.get_role_id_from_name(interaction, "Omniromantic")
        if interaction.user.get_role(role.id):
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                content="The Omniromantic Role has been removed",
                ephemeral=True,
                delete_after=60,
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content="The Omniromantic Role has been added",
                ephemeral=True,
                delete_after=60,
            )
