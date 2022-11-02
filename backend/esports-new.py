import discord
from discord import app_commands

# Class for initiating the bot
class esportBot(discord.Client):
    def __init__(self) -> None:
        super().__init__(intents=discord.Intents.default())
        intents = discord.Intents.default()
        intents.message_content = True
        self.synced = False
        self.added = False


    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        if not self.added:
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

@tree.event
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


@tree.event
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


client.run('token here')
