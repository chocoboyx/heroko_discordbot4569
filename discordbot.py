import discord
import googletrans
from pprint import pprint
# 輸入自己Bot的TOKEN碼
TOKEN = 'ODU0Njk2OTM0NTA0NTI5OTYy.YMnsjA.ccP75JIJTlNH0gjfDIxVPIMu2XI'

client = discord.Client()

# 起動時呼叫
@client.event
async def on_ready():
    print('成功登入')

# 收到訊息時呼叫
@client.event
async def on_message(message):
    # 送信者為Bot時無視
    if message.author.bot:
        return
    
    if client.user in message.mentions: # @判定
        translator = googletrans.Translator()
        robotName = client.user.name
        if translator.detect(message.content) == 'zh-tw':
            return
            
        first, space, content = message.clean_content.partition('@'+robotName+' ')
        
        if content == '':
            content = first
        remessage = translator.translate(content, dest='zh-tw').text
        await message.reply(remessage) 

# Bot起動
client.run(TOKEN)