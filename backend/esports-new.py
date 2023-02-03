# TODO:
# How tf do reaction roles work?
# Ticket system


# Button elements credit to Digiwind- https://youtu.be/-oY0k0jU1IE
# Reaction roles credit to Jacob

import discord
from discord import app_commands
from discord.ext.commands import MissingPermissions
# from keep_alive import keep_alive

# Class for initiating the bot
class esportBot(discord.Client):
    def __init__(self) -> None:
        super().__init__(intents=discord.Intents.default())
        intents = discord.Intents.default()
        intents.message_content = True
        self.synced = False
        self.added = False
        self.role = '1067143291449126993'

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #check if slash commands have been synced 
            await tree.sync(guild = discord.Object(id=951611019845840986))
            self.synced = True
        if not self.added:
            self.add_view(verify())
            self.added = True
        print(f"Successfully booted {self.user}.")

# Variables
client = esportBot()
tree = app_commands.CommandTree(client)

# Error handler
@tree.error
async def on_app_command_error(interaction, error):
    if isinstance(error, app_commands.AppCommandError):
        await interaction.response.send_message(error, ephemeral=True)
    else:
        raise error

# Button for verification
class verify(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label = "verify", style = discord.ButtonStyle.green, custom_id = "role_button")
    async def verify(self, interaction: discord.Interaction, button: discord.ui.Button):
        if type(client.role) is not discord.Role: client.role = interaction.guild.get_role(1067143291449126993)
        if client.role not in interaction.user.roles:
            await interaction.user.add_roles(client.role)
            await interaction.response.send_message(f"I have given you {client.role.mention}!", ephemeral = True)
        else: await interaction.response.send_message(f"You already have {client.role.mention}!", ephemeral = True)

# Reaction roles
@client.event
async def on_raw_reaction_add(payload):
  mid = payload.message_id # mid = Message ID
  if mid == 1003516910668873838:
    gid = payload.guild_id # gid = Guild ID
    guild = discord.utils.find(lambda g : g.id == gid, client.guilds) #checks to only respond within the discord server it received the reaction in
    if payload.emoji.name == 'LeagueofLegends':
      role = discord.utils.get(guild.roles, name='League of Legends Team')
    elif payload.emoji.name == 'R6':
      role = discord.utils.get(guild.roles, name='Rainbow Six Siege Team')
    elif payload.emoji.name == 'Overwatch':
      role = discord.utils.get(guild.roles, name='Overwatch Team')
    elif payload.emoji.name == 'SuperSmash':
      role = discord.utils.get(guild.roles, name='Super Smash Brothers Team')
    elif payload.emoji.name == 'Valorant':
      role = discord.utils.get(guild.roles, name='Valorant Team')
    elif payload.emoji.name == 'RocketLeague':
      role = discord.utils.get(guild.roles, name='Rocket League Team')

@client.event
async def on_raw_reaction_remove(payload):
  mid = payload.message_id # mid = Message ID
  if mid == 1003516910668873838:
    gid = payload.guild_id # gid = Guild ID
    guild = discord.utils.find(lambda g : g.id == gid, client.guilds)
    if payload.emoji.name == 'LeagueofLegends':
      role = discord.utils.get(guild.roles, name='League of Legends Team')
    elif payload.emoji.name == 'R6':
      role = discord.utils.get(guild.roles, name='Rainbow Six Siege Team')
    elif payload.emoji.name == 'Overwatch':
      role = discord.utils.get(guild.roles, name='Overwatch Team')
    elif payload.emoji.name == 'SuperSmash':
      role = discord.utils.get(guild.roles, name='Super Smash Brothers Team')
    elif payload.emoji.name == 'Valorant':
      role = discord.utils.get(guild.roles, name='Valorant Team')
    elif payload.emoji.name == 'RocketLeague':
      role = discord.utils.get(guild.roles, name='Rocket League Team')

# Only admins can use this command
@tree.command(guild = discord.Object(id=951611019845840986), name = 'button', description='Launches a button!') #guild specific slash command
@app_commands.checks.has_permissions(administrator = True)
async def launch_button(interaction: discord.Interaction):
   await interaction.response.send_message(view = verify())

@launch_button.error
async def launch_error(interaction: discord.Interaction, error):
   if isinstance(error, MissingPermissions):
      await interaction.response.send_message("You do not have permission to use this command.", ephemeral=True)
      

client.run('token')
