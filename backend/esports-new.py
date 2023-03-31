# In progress:
# Ticket System


# Button elements and ticket system credit to Digiwind- https://youtu.be/-oY0k0jU1IE

import discord
from discord import app_commands, utils
from discord.ext import commands
from discord.ext.commands import MissingPermissions

# Button for verification
class verify(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout = None)

    @discord.ui.button(label = "verify", style = discord.ButtonStyle.green, custom_id = "role_button")
    async def verify(self, interaction: discord.Interaction, button: discord.ui.Button):
        if type(client.role) is not discord.Role: client.role = interaction.guild.get_role(1067143291449126993)
        if client.role not in interaction.user.roles:
            await interaction.user.add_roles(client.role)
            await interaction.response.send_message(f"I have given you {client.role.mention}!", ephemeral = True)
        else: await interaction.response.send_message(f"You already have {client.role.mention}!", ephemeral = True)

class launchticket(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout = None)

    @discord.ui.button(label = 'Create a ticket', style = discord.ButtonStyle.blurple, custom_id= 'ticket_button')
    async def ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        ticket = utils.get(interaction.guild.text_channels, name = f'ticket-for-{interaction.user.name}-{interaction.user.discriminator}')
        if ticket is not None: await interaction.response.send_message(f'You already have a ticket open in {ticket.mention}!', ephemeral = True)
        else:
            overwrites = {
                interaction.guild.default_role: discord.PermissionOverwrite(view_channel = False),
                interaction.user: discord.PermissionOverwrite(view_channel = True, send_messages = True, attach_files = True, embed_links = True),
                interaction.guild.me: discord.PermissionOverwrite(view_channel = True, send_messages = True, read_message_history = True)
            }
            channel =  await interaction.guild.create_text_channel(name = f'ticket-for-{interaction.user.name}-{interaction.user.discriminator}', overwrites = overwrites, reason = 
            f'ticket for {interaction.user}')
            await channel.send(f'{interaction.user.mention} created a ticket!', view = main())
            await interaction.response.send_message(f'Ticket opened at {channel.mention}!', ephemeral = True)

class confirm(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout = None)
    
    discord.ui.button(label = 'Confirm', style = discord.ButtonStyle.red, custom_id = 'confirm')
    async def confirm_button(self, interaction, button):
        try: await interaction.channel.delete()
        except: await interaction.response.send_message('Channel deletion failed. Make sure I have the manage_channels permission.', ephemeral = True)

class main(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout = None)
    
    discord.ui.button(label = 'Close Ticket', style = discord.ButtonStyle.red, custom_id = 'close')
    async def close(self, interaction, button):
        embed = discord.Embed(title = 'Are you sure you want to close this ticket?', color = discord.Color.blurple())
        await interaction.response.send_message(embed = embed, view = confirm(), ephemeral = True)

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
            await tree.sync(guild = discord.Object(id = 951611019845840986))
            self.synced = True
        if not self.added:
            self.add_view(verify())
            self.add_view(launchticket())
            self.added = True
        print(f"Successfully booted {self.user}.")

# Variables
client = esportBot()
tree = app_commands.CommandTree(client)

# Only admins can use this command
@tree.command(guild = discord.Object(id = 951611019845840986), name = 'verify_button', description='Launches a button!') #guild specific slash command
@app_commands.checks.has_permissions(administrator = True)
async def launch_button(interaction: discord.Interaction):
   await interaction.response.send_message(view = verify())

@launch_button.error
async def launch_error(interaction: discord.Interaction, error):
   if isinstance(error, app_commands.errors.MissingPermissions):
      await interaction.response.send_message("You do not have permission to use this command.", ephemeral=True)

@tree.command(guild = discord.Object(id = 951611019845840986), name = 'launchticket', description= 'Launches a ticket!')
async def ticketing(interaction: discord.Interaction):
    embed = discord.Embed(title = 'If you need support, click the button below to make a ticket.', color = discord.Color.blue())
    await interaction.channel.send(embed = embed, view = launchticket())
    await interaction.response.send_message('Launched your ticket!', ephemeral = True)
    
@tree.command(guild = discord.Object(id = 951611019845840986), name = 'close', description = 'closes the ticket')
async def close(interaction: discord.Interaction):
    if 'ticket-for-' in interaction.channel.name:
        embed = discord.Embed(title = 'Are you sure you want to close this ticket?', color = discord.Color.blurple())
        await interaction.response.send_message(embed = embed, view = confirm(), ephemeral = True)
    else: await interaction.response.send_message('This is not a ticket!', ephemeral = True)

# Emoji dictionary for reaction roles
emoji = {
    '💚': 'fuck you',
    '<:floppa:1081274713151639582>': 'fuck you'
}

# Finally figured out the goddamn reaction roles
# This one adds a role upon reaction
@client.event
async def on_raw_reaction_add(payload):
    if str(payload.emoji) in emoji.keys() and not payload.member.bot and payload.message_id == 1072215600585244833:
        guild = await client.fetch_guild(payload.guild_id)
        role = discord.utils.get(guild.roles, name = emoji[str(payload.emoji)])
        member = await guild.fetch_member(payload.user_id)
        await member.add_roles(role)

# This one removes a role upon reaction
@client.event
async def on_raw_reaction_remove(payload):
    if str(payload.emoji) in emoji.keys() and payload.message_id == 1072215600585244833:
        guild = await client.fetch_guild(payload.guild_id)
        role = discord.utils.get(guild.roles, name = emoji[str(payload.emoji)])
        member = await guild.fetch_member(payload.user_id)
        await member.remove_roles(role)

client.run('token')
