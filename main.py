import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def image(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            name = attachment.filename
            url = attachment.url
            await attachment.save(name)
            await ctx.send("Archivo guardado")


            try:
                class_name = get_class("keras_model.h5", "labels.txt", name)
                if class_name == "Palomas":
                    await ctx.send("Esto es una paloma, las palomas suelen comer semillas, granos, frutas, bellotas, tambien insectos como gusanos y hormigas")
                elif class_name == "Gorriones":
                    await ctx.send("Esto es un gorrion, y suelen comer semillas, granos, frutas, bellotas, tambien insectos como gusanos y hormigas")
            except:
                await ctx.send("Ha ocurrido un error, revisa que el formato de la imagen sea correcta: PNG, JPG JPEG")

    else:
        await ctx.send("No hay archivos adjuntos en el mensaje")



bot.run("TOKEN")