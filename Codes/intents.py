import discord

def get_intents():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    intents.guilds = True
    intents.presences = True
    intents.typing = True
    intents.reactions = True
    intents.voice_states = True
    intents.guild_messages = True
    return intents
