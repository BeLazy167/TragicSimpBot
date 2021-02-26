import discord
from discord.ext import commands
from discfactbot.Resources import joke as jk
import random


def colour_generator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return discord.Colour.from_rgb(r, g, b)


class Joke(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("joke Cog is ready")

    @commands.command(name="joke", aliases=['JOKE', 'JOKe', 'Joke', 'JoKe', 'jOKE', 'joKE', 'jokE', 'jOkE'])
    async def fact(self, message, joke_type ="None"):
        channels = ['joke-and-fact']
        type_of_joke = ['PROGRAMMING', 'MISC', 'DARK', 'PUN', 'SPOOKY', 'CHRISTMAS']
        if message.channel.name in channels:  # bot only run command in joke-only channel
            if joke_type.upper() == "NONE":
                joke = jk.get_joke()
                embed = discord.Embed(description=joke,
                                      colour=0x0000ff)  # this is used to send embed text to discord
                await message.channel.send(embed=embed)
            elif joke_type.upper() in type_of_joke:
                joke = jk.get_joke(joke_type.upper())  # return random joke
                embed = discord.Embed(description=joke, colour=0x0000ff)
                await message.channel.send(embed=embed)
            elif joke_type.upper() == 'DADJOKE':
                joke = jk.get_dad_joke()  # return dad joke
                embed = discord.Embed(description=joke, colour=0x0000ff)
                await message.channel.send(embed=embed)
            else:
                embed = discord.Embed(description="Wrong joke type", colour=0x0000ff)
                await message.channel.send(embed=embed)


def setup(client):
    client.add_cog(Joke(client))
