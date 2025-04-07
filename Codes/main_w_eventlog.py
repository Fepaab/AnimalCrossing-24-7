import asyncio                                                 # Importa a biblioteca asyncio
import datetime                                                # Importa a biblioteca datetime
import discord                                                 # Importa a biblioteca discord 
from discord.ext import commands                               # Importa a biblioteca discord.ext.commands
from discord import FFmpegPCMAudio                             # Importa a biblioteca discord.FFmpegPCMAudio
from apikeys import TOKEN                                      # Importa o token do bot
from intents import get_intents                                # Importa a função get_intents
from musicaandtime import nowplaying, horario, meridiantime    # Importa a função musica e horario

intents = get_intents()
client = commands.Bot(command_prefix='!', intents=intents)

@client.command(name='play')
async def play(ctx):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    
    try:
        while True:  # Loop infinito para manter o bot tocando músicas
            nomemusica = meridiantime()  # Obtém o nome da música com base no horário atual
            source = FFmpegPCMAudio(f'Audios/{nomemusica}.mp3')
            voice.play(source)
            
            # Aguarda até que o horário mude
            while meridiantime() == nomemusica:
                if not voice.is_playing():  # Se a música terminar, reinicia
                    source = FFmpegPCMAudio(f'Audios/{nomemusica}.mp3')
                    voice.play(source)
                await asyncio.sleep(1)
    except Exception as e:
        print(f'{horario()} ERROR    Ocorreu um erro: {e}')
    finally:
        await voice.disconnect()  # Garante que o bot será desconectado ao sair do loop
    
@client.event
async def on_ready():
    print(f'{horario()} INFO     O Bot foi iniciado, logando como: {client.user}')
    print(f'{horario()} --------------------------------------------------------------------')

@client.command(name='musica')
async def musica(ctx):
    await ctx.send(nowplaying())  # Chama a função musica e envia o resultado como mensagem

@client.event
async def on_voice_state_update(member, before, after):
    channel = client.get_channel(ID_CANAL_AQUI)

    # Entrou no canal
    if before.channel is None and after.channel is not None:
        try:
            print(f'{horario()} INFO     {member.name} entrou no canal de voz: {after.channel.name}')
            if channel:
                await channel.send(f'[{horario()}] {member.name} entrou no canal de voz: {after.channel.name}')
        except Exception as e:
            print(f'{horario()} ERROR    Ocorreu um erro: {e}')

    # Saiu do canal
    elif before.channel is not None and after.channel is None:
        try:
            print(f'{horario()} INFO     {member.name} saiu do canal de voz: {before.channel.name}')
            if channel:
                await channel.send(f'[{horario()}] {member.name} saiu do canal de voz: {before.channel.name}')
        except Exception as e:
            print(f'{horario()} ERROR    Ocorreu um erro: {e}')

    # Mudou de canal
    elif before.channel is not None and after.channel is not None and before.channel != after.channel:
        try:
            print(f'{horario()} INFO     {member.name} mudou de canal de voz: {before.channel.name} -> {after.channel.name}')
            if channel:
                await channel.send(f'[{horario()}] {member.name} mudou de canal de voz: {before.channel.name} -> {after.channel.name}')
        except Exception as e:
            print(f'{horario()} ERROR    Ocorreu um erro: {e}')

    # Verifica se o bot está sozinho no canal de voz
    voice_client = discord.utils.get(client.voice_clients, guild=member.guild)
    if voice_client and voice_client.channel:  # Verifica se o bot está conectado
        if len(voice_client.channel.members) == 1:  # Apenas o bot está no canal
            print(f'{horario()} INFO     O canal de voz {voice_client.channel.name} está vazio. Desconectando...')
            await voice_client.disconnect()

client.run(TOKEN)
