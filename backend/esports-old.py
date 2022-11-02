import discord
import os
from keep_alive import keep_alive


intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event #prints previous in console when bot is logged in
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) 


@client.event #simple command and response
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'): 
        await message.channel.send('Hello!') #responds to $hello command with Hello!

@client.event #event to add a role
async def on_raw_reaction_add(payload):
  message_id = payload.message_id
  if message_id == 1003516910668873838: #Role select reaction check
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds) #checks to only respond within the discord server it received the reaction in

    if payload.emoji.name == 'LeagueofLegends':                     #Checks Descrepency between emoji and role name
      role = discord.utils.get(guild.roles, name='League of Legends Team') #
    elif payload.emoji.name == 'R6':                                #
      role = discord.utils.get(guild.roles, name='Rainbow Six Siege Team')             #
    elif payload.emoji.name == 'Overwatch':                         #
      role = discord.utils.get(guild.roles, name='Overwatch Team')       #
    elif payload.emoji.name == 'SuperSmash':                        #
      role = discord.utils.get(guild.roles, name='Super Smash Brothers Team')      #
    elif payload.emoji.name == 'Valorant':                          #
      role = discord.utils.get(guild.roles, name='Valorant Team')        #
    elif payload.emoji.name == 'RocketLeague':                      #
      role = discord.utils.get(guild.roles, name='Rocket League Team') #

    if role is not None: #checks valid role
      member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members) #finds member ID
      if member is not None:
        await member.add_roles(role) #gives member role
        print("Done")
      else:
        print("Member not found.")
    else:
      print("Role not found.")


  elif message_id == 1003432910881296465:
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds) 
    if payload.emoji.name == 'PSU': 
      role = discord.utils.get(guild.roles, name='Member')
    else:
      role = discord.utils.get(guild.roles, name=payload.emoji.name)

    if role is not None: #checks valid role
      member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members) #finds member ID
      if member is not None:
        await member.add_roles(role) #gives member role
        print("Done")
      else:
        print("Member not found.")
    else:
      print("Role not found.")

  else:
    pass

@client.event #event to remove a role
async def on_raw_reaction_remove(payload):
  message_id = payload.message_id
  if message_id == 1003516910668873838: #checks if the reaction was to the correct message
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds) #checks to only respond within the discord server it received the reaction in

    if payload.emoji.name == 'LeagueofLegends':                     #Checks Descrepency between emoji and role name
      role = discord.utils.get(guild.roles, name='League of Legends Team') #
    elif payload.emoji.name == 'R6':                                       #
      role = discord.utils.get(guild.roles, name='Rainbow Six Siege Team') #
    elif payload.emoji.name == 'Overwatch':                         #
      role = discord.utils.get(guild.roles, name='Overwatch Team')       #
    elif payload.emoji.name == 'SuperSmash':                               #
      role = discord.utils.get(guild.roles, name='Super Smash Brothers Team') #
    elif payload.emoji.name == 'Valorant':                                 #
      role = discord.utils.get(guild.roles, name='Valorant Team')          #
    elif payload.emoji.name == 'RocketLeague':                             #
      role = discord.utils.get(guild.roles, name='Rocket League Team')     #
    else:                                                                  #
      role = discord.utils.get(guild.roles, name=payload.emoji.name)       #

    if role is not None: #checks valid role
      member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members) #finds member ID
      if member is not None:
        await member.remove_roles(role) #removes members role
        print("Done")
      else:
        print("Member not found.")
    else:
      print("Role not found.")



keep_alive()
client.run(os.getenv('TOKEN'))
