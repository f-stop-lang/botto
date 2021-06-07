import discord
from discord.ext import commands


class FStopBot(commands.Bot):
    
    def __init__(self) -> None:
        intents = discord.Intents.default()
        intens.members = True
        
        super().__init__(
            command_prefix=commands.when_mentioned_or('?', '!'),
            intents=intents,
            description='A bot for the f-stop Discord server.', 
            case_insensitive=True,
            color=0x2F3136,
        )
        
 if __name__ == '__main__':
    botto = FStopBot()
    botto.run('token')
