import discord
import asyncio
from discord.utils import get
from discord.ext import commands
import time



# create préfix
bot = commands.Bot(command_prefix='/')
bot.remove_command("help")

# detected when the bot is online
@bot.event
async def on_ready():
    print("Bot is ready")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("/help"))
                


#help menu 
@bot.command(pass_context=True)
async def help (ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name='Help menu')
    embed.add_field(name='/ping', value='returns the ping |', inline=True)
    embed.add_field(name='/informations', value='Show informations about this bot |', inline=True)
    embed.add_field(name='/clear', value='specify a number after /clear to delete messages |', inline=False)
    await ctx.send(author, embed=embed)


# ping
@bot.command()
async def ping(ctx):
    await ctx.send(f'My ping is {bot.latency}!')


# clear messages
@bot.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount):
              messages.append(message)
    await channel.delete_messages(messages)
    await ctx.send(f'{amount} Messaged deleted', delete_after = 3)


# informations 
@bot.command()
async def informations(ctx):
    embed=discord.Embed(title="Informations", description="bot create by @greenpix | host Adkynet.com", color=0x5836e2)
    embed.set_author(name="JERRY BOT ")
    embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/totallyspies/images/0/0f/Jerry_remastered.png/revision/latest?cb=20180217214536")
    embed.add_field(name="add the bot in your server", value="https://nondispo.com", inline=False)
    embed.set_footer(text="carab0uille#5636")
    await ctx.send(embed=embed)


# kick 
@bot.command()
async def kick(ctx, member : discord.Member, *,reason=None):
    await ctx.send(f'{member} is kick for {reason}')
    await member.send(f'you have kick for {reason}', delete_after = 3)
    await member.kick(reason=reason)

    
#ban 
@bot.command()
async def ban(ctx, member : discord.Member, *,reason=None):
    await ctx.send(f'{member.mention} is ban for {reason}', delete_after = 3)
    await member.send(f'you have ban for {reason}')
    await member.ban(reason=reason)


# unban
@bot.command()
async def unban(ctx, *,member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}', delete_after = 3)
            return




# when the bot starting
print("bot is starting..")

# token
bot.run("Your token here")
