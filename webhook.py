from urllib.request import urlopen
import json
from dotenv import load_dotenv
import os 
from discord_webhook import DiscordWebhook, DiscordEmbed

load_dotenv()
API =os.getenv("API_URL")
url = API # Pega a url e seta a API

response = urlopen(url) # Faz uma requisição a API

data_json = json.loads(response.read()) # Faz um parse dos dados em JSON 

nome = data_json["USDBRL"]["name"]
data = data_json["USDBRL"]["create_date"]
valor_compra = data_json["USDBRL"]["bid"] # Extrai os dados que foram escolhidos da API
valor_venda = data_json["USDBRL"]["ask"]
variacao = data_json["USDBRL"]["varBid"]


WEBHOOK_URL = os.getenv("WEBHOOK_URL")
webhook = DiscordWebhook(WEBHOOK_URL) # Cria a instancia do webhook com o uso da url gerada no discord para o webhook

embed = DiscordEmbed(title='COTAÇÃO', description='%s em %s' %(nome, data), color='03b2f8')
embed.set_author(name='Cotador Angolano', icon_url='https://p2.trrsf.com/image/fget/cf/774/0/images.terra.com/2022/07/15/1022644453-1657836252493.jpg')
embed.add_embed_field(name='Valor de Compra',value='%s' %(valor_compra)) # Variáveis escolhidas para aparecer na mensagem enviada ao discord
embed.add_embed_field(name='Valor de Venda',value='%s' %(valor_venda))
embed.add_embed_field(name='Variação',value='%s' %(variacao))

    
webhook.add_embed(embed) # Adiciona as variáveis acima ao webhook

response = webhook.execute(embed) # Executa o webhook

