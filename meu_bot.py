import discord
import openai
import os
from datetime import date 
from datetime import datetime

data_hora_atual = datetime.now()
data_hoje = data_hora_atual.strftime('%d/%m/%Y')
hora_atual = data_hora_atual.strftime('%H:%M')
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} ta ligado!')

    async def on_message(self, message):
        print(f'Mensagem de {message.author}: {message.content}')
        if message.content == '?regras':
            await message.channel.send(f'@{message.author.name} As regras do servidor são: {os.linesep} 1- NÃO HÁ REGRAS ! {os.linesep} 2- NÃO HÁ REGRAS ! {os.linesep} 3- NÃO HÁ REGRAS !')
        if message.content == '?hoje':
            await message.channel.send(f'@{message.author.name} A data de hoje é {data_hoje}')
        if message.content == '?hora':
            await message.channel.send(f'@{message.author.name} Agora são {hora_atual} horas')

print(data_hoje)
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTE3NzM0ODIzMDE5MTc5MjE3OA.Gxf8o-.F1Orv2NYgRKf-rtvwGJ9q1akX1HaEYNrKCixgo')