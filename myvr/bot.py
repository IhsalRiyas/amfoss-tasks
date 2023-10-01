import discord
import os
from scraper import get_livescore, livescore_file, team_info
def get_responses(message):   
    
    if message == "/Hello":
        return "Hi thee stranger!"
    elif message == "/roll":
        return "why the hell did you even try that?!"
    elif message == "/help":
        return "like hell I am, just ChatGPT it, you lazy ass"
    elif message == "/help, please?":
        return " I dont get paid enough for this shit."
    else:
        pass
async def send_message(message, user_message, is_private):
    #we do the is_private thing so if user inputs to bot in private, it will also reply in private. kinda not needed but eh.
    try:

        response=get_responses(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
def run_discord_bot():
    token ='MTE1MzcxMjg3MjU1MjE0OTAxMw.G6XnFR.AkYriNHsqOSkGLpmwC_u7Q_8EA4EA8VYwGMAnc'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running probably. idk, i worken on this for too long ')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        # we do this as otherwise, it will essentially be an infinite loop evrytime we ask the bot something
        username= str(message.author)
        user_message = message.content
        # this will be a string either ways. we're doing this just in case there will a error of some sort.
        channel = str(message.channel)

        print(f'{username} said : "{user_message}"({channel})')

        if user_message and user_message[0] == '/':
            await send_message(message, user_message, is_private= False)
        else:
            await send_message(message,user_message, is_private= False)
    client.run(token)
if __name__ == "__main__": # underscores are the bane of my existence.
    run_discord_bot()

