import os, discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot=commands.Bot(command_prefix="!")
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Big Brain has arrived!")

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
                                    f'Hey {member.name}, welcome to our TESTING BOT Channel! Where we love to code and we love rick and morty!'
                                    f'Here is where you can find me on Youtube: https://www.youtube.com/channel/UCQp9MwvONH8ekII1OBJcg7w'
                                )
    role= discord.utils.get(member.guild.roles, name="New User")
    await member.add_roles(role)

    channel=bot.get_channel(CHANNEL_ID)
    print(discord.Colour.orange())
    welcome_chat_embed=discord.Embed(colour = discord.Colour.orange())
    welcome_chat_embed.set_author(name=f'Hey @{member.name}, welcome to our TESTING BOT Channel!')
    await channel.send(embed=welcome_chat_embed)


@bot.command()
async def help(ctx):
    embed=discord.Embed(colour=discord.Colour.orange())
    embed.set_author(name="Help Commands")
    embed.add_field(name="!help", value="This is how you see this screen!")
    await ctx.send(embed=embed)



bot.run(TOKEN)
