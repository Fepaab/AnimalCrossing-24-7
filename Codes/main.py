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
        current_music = None  # Variável para armazenar a música atual
        while True:  # Loop infinito para manter o bot tocando músicas
            nomemusica = meridiantime()  # Obtém o nome da música com base no horário atual
            
            # Se a música atual terminou ou é a primeira execução, troca para a nova música
            if current_music != nomemusica:
                current_music = nomemusica
                print(f'{horario()} INFO     Tocando música: {current_music}')
            
            # Se a música não está tocando, reinicia a reprodução
            if not voice.is_playing():
                source = FFmpegPCMAudio(f'Audios/{current_music}.mp3')
                voice.play(source)
            
            # Aguarda um curto intervalo antes de verificar novamente
            await asyncio.sleep(1)
    except Exception as e:
        printT(f'{horario()} ERROR    Ocorreu um erro: {e}')
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
    channel = client.get_channel(ID_DO_CANAL_AQUI)
    # Verifica se o bot está sozinho no canal de voz
    voice_client = discord.utils.get(client.voice_clients, guild=member.guild)
    if voice_client and voice_client.channel:  # Verifica se o bot está conectado
        if len(voice_client.channel.members) == 1:  # Apenas o bot está no canal
            print(f'{horario()} INFO     O canal de voz {voice_client.channel.name} está vazio. Desconectando...')
            await voice_client.disconnect()

client.run(TOKEN)
