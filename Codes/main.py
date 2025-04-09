import asyncio                                                 # Biblioteca para operações assíncronas
import datetime                                                # Biblioteca para manipulação de datas e horários
import discord                                                 # Biblioteca principal para interação com o Discord
from discord.ext import commands                               # Extensão para criar comandos no bot
from discord.ui import View, Select                            # Para criar menus suspensos e views
from discord import FFmpegPCMAudio                             # Para reprodução de áudio via FFmpeg
from apikeys import TOKEN, ID_CANAL_VOZ                        # Importa o token e o ID do canal de voz
from intents import get_intents                                # Importa a função para configurar intents do bot
from musicaandtime import nowplaying, horario, meridiantime    # Funções auxiliares para música e horário

# Configura os intents do bot
intents = get_intents()
client = commands.Bot(command_prefix='!', intents=intents)  # Define o prefixo dos comandos do bot

# Define valores padrão para as variáveis globais
selected_game = "newhorizons"  # Valor padrão inicial para o jogo
selected_weather = "sunny"     # Valor padrão inicial para o clima

# --------------------------------------------------------------------
# Comando: !select
# Exibe menus suspensos para o usuário selecionar um jogo e um clima
# --------------------------------------------------------------------
@client.command(name='select')
async def select(ctx):
    global selected_game, selected_weather  # Permite modificar as variáveis globais

    # Callback para tratar a seleção do menu de jogos
    async def select_callback(interaction):
        global selected_game  # Certifica-se de que a variável global seja usada
        selected_game = menu_select.values[0]  # Atualiza a variável com o valor selecionado
        await interaction.response.send_message(f"Você escolheu o jogo: {selected_game}")
        print(f'{horario()} INFO     O jogo selecionado é: {selected_game}')  # Exibe no terminal

    # Callback para tratar a seleção do menu de climas
    async def weather_callback(interaction):
        global selected_weather  # Certifica-se de que a variável global seja usada
        selected_weather = weather_select.values[0]  # Atualiza a variável com o valor selecionado
        await interaction.response.send_message(f"Você escolheu o clima: {selected_weather}")
        print(f'{horario()} INFO     O clima selecionado é: {selected_weather}')  # Exibe no terminal

    # Cria o menu suspenso com as opções de jogos
    menu_select = Select(
        placeholder="Escolha um jogo: ",
        options=[
            discord.SelectOption(label='Animal Crossing: GameCube', emoji='▶️', value='gamecube'),
            discord.SelectOption(label='Animal Crossing: City Folk/Wild World', emoji='▶️', value='cityfolk'),
            discord.SelectOption(label='Animal Crossing: New Leaf', emoji='▶️', value='newleaf'),
            discord.SelectOption(label='Animal Crossing: New Horizons', emoji='▶️', value='newhorizons')
        ]
    )
    menu_select.callback = select_callback  # Define o callback para o menu de jogos

    # Cria o menu suspenso com as opções de climas
    weather_select = Select(
        placeholder="Escolha um clima: ",
        options=[
            discord.SelectOption(label='Sunny', emoji='☀️', value='sunny'),
            discord.SelectOption(label='Snowy', emoji='❄️', value='snowy'),
            discord.SelectOption(label='Rainy', emoji='🌧️', value='rainy')
        ]
    )
    weather_select.callback = weather_callback  # Define o callback para o menu de climas

    # Cria uma view e adiciona os menus suspensos
    view = View()
    view.add_item(menu_select)
    view.add_item(weather_select)

    # Envia a mensagem com os menus suspensos
    await ctx.send('Escolha um jogo e um clima:', view=view)
    print(f'{horario()} INFO     Menus enviados para {ctx.author.name}.')

# --------------------------------------------------------------------
# Comando: !play
# Conecta o bot ao canal de voz e toca músicas baseadas no horário, jogo e clima selecionados
# --------------------------------------------------------------------
@client.command(name='play')
async def play(ctx):
    global selected_game, selected_weather  # Certifica-se de usar as variáveis globais
    channel = ctx.message.author.voice.channel  # Obtém o canal de voz do autor do comando
    voice = await channel.connect()  # Conecta ao canal de voz
    
    try:
        current_music = None  # Variável para armazenar a música atual
        while True:  # Loop infinito para manter o bot tocando músicas
            nomemusica = meridiantime()  # Obtém o nome da música com base no horário atual
            
            # Se a música atual terminou ou é a primeira execução, troca para a nova música
            if current_music != nomemusica:
                current_music = nomemusica
                print(f'{horario()} INFO     Tocando música: {current_music} do jogo {selected_game} com clima {selected_weather}')
            
            # Se a música não está tocando, reinicia a reprodução
            if not voice.is_playing():
                source = FFmpegPCMAudio(f'Audios/{selected_game}/{selected_weather}/{current_music}.mp3')
                voice.play(source)
            
            # Aguarda um curto intervalo antes de verificar novamente
            await asyncio.sleep(1)
    except Exception as e:
        print(f'{horario()} ERROR    Ocorreu um erro: {e}')
    finally:
        await voice.disconnect()  # Garante que o bot será desconectado ao sair do loop

# --------------------------------------------------------------------
# Comando: !stop
# Desconecta o bot do canal de voz e encerra sua execução
# --------------------------------------------------------------------
@client.command(name='stop')
async def stop(ctx):
    """Comando para parar o bot e desconectá-lo."""
    # Desconecta do canal de voz, se conectado
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice_client and voice_client.is_connected():
        await voice_client.disconnect()
        print(f'{horario()} INFO     O bot foi desconectado do canal de voz.')

    # Envia uma mensagem de confirmação no canal de texto
    await ctx.send("Saindo da call! Até mais!")

# --------------------------------------------------------------------
# Comando: !refresh
# Reinicia a música atual que está sendo tocada
# --------------------------------------------------------------------
@client.command(name='refresh')
async def refresh(ctx):
    global selected_game, selected_weather  # Certifica-se de usar as variáveis globais

    # Obtém o canal de voz do autor do comando
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if not voice_client or not voice_client.is_connected():
        await ctx.send("O bot não está conectado a nenhum canal de voz.")
        return

    try:
        # Obtém a música atual com base no horário
        current_music = meridiantime()
        print(f'{horario()} INFO     Reiniciando música: {current_music} do jogo {selected_game} com clima {selected_weather}')

        # Reinicia a música
        source = FFmpegPCMAudio(f'Audios/{selected_game}/{selected_weather}/{current_music}.mp3')
        voice_client.stop()  # Para a música atual
        voice_client.play(source)  # Reproduz a música novamente

        await ctx.send(f"A música foi reiniciada: {current_music} do jogo {selected_game} com clima {selected_weather}.")
    except Exception as e:
        print(f'{horario()} ERROR    Ocorreu um erro ao reiniciar a música: {e}')
        await ctx.send("Ocorreu um erro ao tentar reiniciar a música.")

# --------------------------------------------------------------------
# Evento: on_ready
# Executado quando o bot é iniciado com sucesso
# --------------------------------------------------------------------
@client.event
async def on_ready():
    print(f'{horario()} INFO     O Bot foi iniciado, logando como: {client.user}')
    print(f'{horario()} --------------------------------------------------------------------')

# --------------------------------------------------------------------
# Comando: !musica
# Exibe a música que está sendo tocada no momento
# --------------------------------------------------------------------
@client.command(name='musica')
async def musica(ctx):
    await ctx.send(nowplaying())  # Envia a música atual como mensagem no canal de texto

# --------------------------------------------------------------------
# Evento: on_voice_state_update
# Verifica mudanças no estado de voz dos usuários e desconecta o bot se ele estiver sozinho
# --------------------------------------------------------------------
@client.event
async def on_voice_state_update(member, before, after):
    channel = client.get_channel(ID_CANAL_VOZ)  # Usa o ID do canal de voz do arquivo apikeys.py
    
    # Verifica se o bot está sozinho no canal de voz
    voice_client = discord.utils.get(client.voice_clients, guild=member.guild)
    if voice_client and voice_client.channel:  # Verifica se o bot está conectado
        if len(voice_client.channel.members) == 1:  # Apenas o bot está no canal
            print(f'{horario()} INFO     O canal de voz {voice_client.channel.name} está vazio. Desconectando...')
            await voice_client.disconnect()

@client.command(name='help')
async def help_command(ctx):
    """Comando para exibir a lista de comandos disponíveis."""
    help_message = (
        "Aqui estão os comandos disponíveis:\n"
        "!select - Escolha um jogo e um clima.\n"
        "!play - Inicia a reprodução de músicas.\n"
        "!stop - Para a reprodução e desconecta do canal de voz.\n"
        "!refresh - Reinicia a música atual.\n"
        "!musica - Exibe a música que está sendo tocada no momento.\n"
        "!help - Exibe esta mensagem de ajuda."
    )
    await ctx.send(help_message)


# --------------------------------------------------------------------
# Inicia o bot com o token fornecido
# --------------------------------------------------------------------
client.run(TOKEN)
