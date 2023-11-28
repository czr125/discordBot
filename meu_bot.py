import discord
import os
from datetime import date 
from datetime import datetime
from dotenv import load_dotenv

data_hora_atual = datetime.now()
data_hoje = data_hora_atual.strftime('%d/%m/%Y')
hora_atual = data_hora_atual.strftime('%H:%M')
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} ta ligado!')

    async def on_message(self, message):
        print(f'Mensagem de {message.author}: {message.content}')
        if message.content == '?ajuda':
            await message.channel.send(f'@{message.author.name} Bem-vindo ao Nosso Servidor! 🌟 {os.linesep}{os.linesep} Olá {message.author.name}! Estamos felizes por você estar aqui. Se precisar de ajuda ou tiver alguma dúvida, não hesite em perguntar. Nossa comunidade é amigável e sempre pronta para ajudar. {os.linesep}{os.linesep} 📚 Canais Principais:{os.linesep}{os.linesep}#geral: Para bater papo e conhecer outros membros.{os.linesep}#dúvidas: Faça suas perguntas aqui. A equipe e outros membros estarão felizes em ajudar.{os.linesep}{os.linesep}#anúncios: Mantenha-se atualizado com as últimas novidades e eventos.{os.linesep}{os.linesep}🔗 Recursos Adicionais:{os.linesep}{os.linesep}Confira nossos canais de voz para jogos e eventos especiais.{os.linesep}{os.linesep}🤝 Regras da Comunidade:{os.linesep}{os.linesep}Certifique-se de ler as regras no canal #regras para manter nosso ambiente seguro e amigável.{os.linesep}{os.linesep}🛠️ Suporte Técnico:{os.linesep}{os.linesep}Para problemas técnicos ou ajuda específica, entre em contato com a equipe em #suporte.{os.linesep}Agradecemos por fazer parte da nossa comunidade! {os.linesep}Divirta-se e faça novos amigos. {os.linesep}{os.linesep} 🎉Seja respeitoso e aproveite sua estadia!')
        if message.content == '?regras':
            await message.channel.send(f'@{message.author.name} As regras do servidor são: {os.linesep} 1- NÃO HÁ REGRAS ! {os.linesep} 2- NÃO HÁ REGRAS ! {os.linesep} 3- NÃO HÁ REGRAS !')
        if message.content == '?hoje':
            await message.channel.send(f'@{message.author.name} A data de hoje é {data_hoje}')
        if message.content == '?hora':
            await message.channel.send(f'@{message.author.name} Agora são {hora_atual} horas')
        if message.content == '?sobre':
            await message.channel.send(f'@{message.author.name} ')

print(data_hoje)
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)

