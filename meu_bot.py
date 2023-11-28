import discord
import os
from datetime import date 
from datetime import datetime
from dotenv import load_dotenv

import webhook_cotacao as cotacao

data_hora_atual = datetime.now()
data_hoje = data_hora_atual.strftime('%d/%m/%Y')
hora_atual = data_hora_atual.strftime('%H:%M')
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} ta ligado!')

    async def on_message(self, message):
        mapa = 'https://www.google.com/maps/d/u/0/viewer?mid=1t9FfcpQj5V9XbvpQq6C1MkO3IaetW2Q&femb=1&ll=-1.3706804561412171%2C-48.21316600000001&z=9'
        print(f'Mensagem de {message.author}: {message.content}')
        if message.content == '?comandos':
            await message.channel.send(f"{message.author.mention} {os.linesep} A lista de comandos disponíveis: {os.linesep} ?regras - Mostra as regras do servidor{os.linesep} ?hoje - Mostra a data de hoje {os.linesep} ?hora - Mostra o horário atual {os.linesep} ?sobrerecycle - {os.linesep} ?reciclagem - Mostra o link do site do projeto 'E-Recycle'{os.linesep} ?locais - Mostra o mapa dos locais para descarte de lixo eletrônico em Belém/PA {os.linesep} ?dolar - Mostra a cotação atual do dólar com o valor de compra e de venda {os.linesep} ?euro - Mostra a cotação atual do euro com o valor de compra e de venda {os.linesep} ?pesoarg - Mostra a cotação atual do peso argentino com o valor de compra e de venda {os.linesep} ?bitcoin - Mostra a cotação atual do bitcoin com o valor de compra e de venda {os.linesep} ?ethereum - Mostra a atual cotação do ethereum com o valor de compra e de venda") 
        if message.content == '?regras':
            await message.channel.send(f"{message.author.mention} {os.linesep} As regras do servidor são: {os.linesep} 1- NÃO HÁ REGRAS ! {os.linesep} 2- NÃO HÁ REGRAS ! {os.linesep} 3- NÃO HÁ REGRAS !")
        if message.content == '?hoje':
            await message.channel.send(f"{message.author.mention} {os.linesep} A data de hoje é {data_hoje}")
        if message.content == '?hora':
            await message.channel.send(f"{message.author.mention} {os.linesep} Agora são {hora_atual} horas")
        if message.content == '?sobrerecycle':
            await message.channel.send(f"{message.author.mention} {os.linesep} O E-Recycle é uma iniciativa que visa promover a reciclagem responsável de lixo eletrônico. {os.linesep} Através deste projeto, pretendemos reduzir o impacto ambiental do descarte inadequado de dispositivos eletrônicos, preservar recursos naturais e criar uma comunidade mais consciente da importância da reciclagem.")
        if message.content == '?reciclagem':
            await message.channel.send(f"{message.author.mention} {os.linesep} Link do nosso projeto 'E-Recycle': https://czr125.github.io/E-Recycle/ ")
        if message.content == '?locais':
            await message.channel.send(f"{message.author.mention} {os.linesep} {mapa}")
        if message.content == '?dolar':
            await message.channel.send(f"{message.author.mention} {os.linesep} {cotacao.nome_dolar}: {os.linesep} Valor de Compra = R${cotacao.valor_compra_dolar} {os.linesep} Valor de Venda = R${cotacao.valor_venda_dolar}.")
        if message.content == '?euro':
            await message.channel.send(f"{message.author.mention} {os.linesep} {cotacao.nome_euro}: {os.linesep} Valor de Compra = R${cotacao.valor_compra_euro} {os.linesep} Valor de Venda = R${cotacao.valor_venda_euro}.")
        if message.content == '?pesoarg':
            await message.channel.send(f"{message.author.mention} {os.linesep} {cotacao.nome_peso}: {os.linesep} Valor de Compra = R${cotacao.valor_compra_peso} {os.linesep} Valor de Venda = R${cotacao.valor_venda_peso}.")
        if message.content == '?bitcoin':
            await message.channel.send(f"{message.author.mention} {os.linesep} {cotacao.nome_btc}: {os.linesep} Valor de Compra = R${cotacao.valor_compra_btc} {os.linesep} Valor de Venda = R${cotacao.valor_venda_btc}.")
        if message.content == '?ethereum':
            await message.channel.send(f"{message.author.mention} {os.linesep} {cotacao.nome_eth}: {os.linesep} Valor de Compra = R${cotacao.valor_compra_eth} {os.linesep} Valor de Venda = R${cotacao.valor_venda_eth}.")
   
    async def on_member_join(self,member):
        guild = member.guild
        if guild.system_channel is not None:
            mensagem = f'{mensagem.author.mention} acabou de entrar no {guild.name}! '
            await guild.system_channel.send(mensagem)

print(data_hoje)
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = MyClient(intents=intents)

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)

