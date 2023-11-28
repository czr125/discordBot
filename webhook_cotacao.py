from urllib.request import urlopen
import json
from dotenv import load_dotenv
import os 
from discord_webhook import DiscordWebhook, DiscordEmbed

load_dotenv()
url_dolar = 'https://economia.awesomeapi.com.br/last/USD-BRL' # Pega a url e seta a API
url_euro = 'https://economia.awesomeapi.com.br/last/EUR-BRL'
url_peso = 'https://economia.awesomeapi.com.br/last/ARS-BRL'
url_btc = 'https://economia.awesomeapi.com.br/last/BTC-BRL'
url_eth= 'https://economia.awesomeapi.com.br/last/ETH-BRL'

response_dolar = urlopen(url_dolar) # Faz uma requisição a API
response_euro = urlopen(url_euro)
response_peso = urlopen(url_peso)
response_btc = urlopen(url_btc)
response_eth = urlopen(url_eth)

data_json_dolar = json.loads(response_dolar.read()) # Faz um parse dos dados em JSON 
data_json_euro = json.loads(response_euro.read())
data_json_peso = json.loads(response_peso.read())
data_json_btc = json.loads(response_btc.read())
data_json_eth = json.loads(response_eth.read())

# Area Dólar
nome_dolar = data_json_dolar["USDBRL"]["name"]
data_dolar = data_json_dolar["USDBRL"]["create_date"]
valor_compra_dolar = data_json_dolar["USDBRL"]["bid"] # Extrai os dados dólar que foram escolhidos da API
valor_venda_dolar = data_json_dolar["USDBRL"]["ask"]
variacao_dolar = data_json_dolar["USDBRL"]["varBid"]
# Area Euro
nome_euro = data_json_euro["EURBRL"]["name"]
valor_compra_euro = data_json_euro["EURBRL"]["bid"] # Extrai os dados euro que foram escolhidos da API
valor_venda_euro = data_json_euro["EURBRL"]["ask"]
# Area Peso Argentino
nome_peso = data_json_peso["ARSBRL"]["name"]
valor_compra_peso = data_json_peso["ARSBRL"]["bid"] # Extrai os dados peso que foram escolhidos da API
valor_venda_peso = data_json_peso["ARSBRL"]["ask"]
# Area Bitcoin
nome_btc = data_json_btc["BTCBRL"]["name"]
valor_compra_btc = data_json_btc["BTCBRL"]["bid"] # Extrai os dados bitcoin que foram escolhidos da API
valor_venda_btc = data_json_btc["BTCBRL"]["ask"]
# Area Ethereum
nome_eth = data_json_eth["ETHBRL"]["name"]
valor_compra_eth = data_json_eth["ETHBRL"]["bid"] # Extrai os dados bitcoin que foram escolhidos da API
valor_venda_eth = data_json_eth["ETHBRL"]["ask"]

WEBHOOK_URL2 = os.getenv("WEBHOOK_URL2")
webhook = DiscordWebhook(WEBHOOK_URL2) # Cria a instancia do webhook com o uso da url gerada no discord para o webhook

embed = DiscordEmbed(title='COTAÇÃO', description='%s em %s' %(nome_dolar, data_dolar), color='03b2f8')
embed.set_author(name='Cotador Angolano', icon_url='https://p2.trrsf.com/image/fget/cf/774/0/images.terra.com/2022/07/15/1022644453-1657836252493.jpg')
embed.add_embed_field(name='Valor de Compra',value='%s' %(valor_compra_dolar)) # Variáveis escolhidas para aparecer na mensagem enviada ao discord
embed.add_embed_field(name='Valor de Venda',value='%s' %(valor_venda_dolar))
embed.add_embed_field(name='Variação',value='%s' %(variacao_dolar))

    
webhook.add_embed(embed) # Adiciona as variáveis acima ao webhook

response = webhook.execute(embed) # Executa o webhook

