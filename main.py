import discord
from discord.ext import commands


class FStopBot(commands.Bot):
    
    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.members = True
        self.color = 0x2F3136
        
        super().__init__(
            command_prefix=commands.when_mentioned_or('?', '!'),
            intents=intents,
            description='A bot for the f-stop Discord server.', 
            case_insensitive=True,
        )
        
 if __name__ == '__main__':
    botto = FStopBot()
    botto.run('token')
