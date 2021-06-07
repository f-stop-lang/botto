import discord
from discord.ext import commands


class FStopBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='?',
            intents=discord.Intents.all(),
            description='A bot for the f-stop Discord server.'
        )
        
    def run(self):
        super().run('komodo put your token here')
    
    
 if __name__ == '__main__':
    botto = FStopBot()
    botto.run()
