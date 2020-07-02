import discord



emojis = '🇵🇷ℹ️🇲💊'
poehavshie = {
583991031016456192, 724475443297779722 #zyabl
}


client = discord.Client()

@client.event
async def on_ready():
    print("Запущено.")

@client.event
async def on_message(message):
    if message.author.id in poehavshie:
        for em in emojis:
            await message.add_reaction(em)


token = os.environ.get('BOT_TOKEN') # Получаем токен с heroku который ты указывал в настройках
client.run(str(token)) # запускаем бота
