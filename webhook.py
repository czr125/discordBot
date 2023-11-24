from urllib.request import urlopen
import json
import schedule
import time

from discord_webhook import DiscordWebhook, DiscordEmbed

url = "https://economia.awesomeapi.com.br/last/USD-BRL"

response = urlopen(url)

data_json = json.loads(response.read())

nome = data_json["USDBRL"]["name"]
data = data_json["USDBRL"]["create_date"]
valor_compra = data_json["USDBRL"]["bid"]
valor_venda = data_json["USDBRL"]["ask"]
variacao = data_json["USDBRL"]["varBid"]


webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1177372572162195537/MBvl4aCGpADhylghRzRTugPAQryavsCY3RRPCQb0t3Wsa9ihzUwJHDH2fOyu9DNi-Mla')
embed = DiscordEmbed(title='COTAÇÃO', description='%s em %s' %(nome, data), color='03b2f8')
embed.set_author(name='Cotador Angolano', icon_url='https://p2.trrsf.com/image/fget/cf/774/0/images.terra.com/2022/07/15/1022644453-1657836252493.jpg')
embed.add_embed_field(name='Valor de Compra',value='%s' %(valor_compra))
embed.add_embed_field(name='Valor de Venda',value='%s' %(valor_venda))
embed.add_embed_field(name='Variação',value='%s' %(variacao))

    
webhook.add_embed(embed)
response = webhook.execute(embed)

