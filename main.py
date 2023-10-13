# import requests
# from bs4 import BeautifulSoup
# import telegram

# url = "https://canlidoviz.com/"
# response = requests.get(url)
# # print(response.text)
# # Web sayfasından veriyi çekmek için GET isteği gönderin

# # İstek başarılı ise sayfa içeriğini BeautifulSoup ile analiz edin
# if response.status_code == 200:
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Döviz kurlarını içeren tabloyu bulun
#     table = soup.find('table')
#     # print(table)
#     # Tablodaki tüm satırları bulun
#     rows = table.find_all('tr')
#     # print(rows)
#     # İlk satır başlık olduğu için atlanır
#     for row in rows[0:]:
#         # Satırdaki hücreleri bulun
#         cells = row.find_all('td')
#         # print(cells)
#         # Hücrelerden döviz adını, değerini ve değişimini alın
#         currency = cells[0].text.strip()
#         value = cells[1].text.strip()
#         change = cells[2].text.strip()

#         # Elde edilen veriyi kullanın veya yazdırın
#         # print(f"Currency: {currency} Value: {value}, Change: {change}")
#         message = f"Currency: {currency}\nValue: {value}\nChange: {change}"
#         print(message)
# else:
#     print('İstek başarısız oldu.')

# bot_token = 'YOUR_BOT_TOKEN'
# bot = telegram.Bot(token=bot_token)

# bot.send_message(chat_id='YOUR_CHAT_ID', text=message)

import requests
from bs4 import BeautifulSoup
import telegram
import os
from dotenv import load_dotenv
import asyncio

# Load environment variables from .env file
load_dotenv()

url = os.getenv("URL")
# print(url)
# url = "https://canlidoviz.com/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table')
    rows = table.find_all('tr')

    message = ""

    for row in rows[0:]:
        cells = row.find_all('td')
        currency = cells[0].text.strip()
        value = cells[1].text.strip()
        change = cells[2].text.strip()

        message += f"Currency: {currency}\nValue: {value}\nChange: {change}\n\n"
        print(message)

    # # bot_token = 'YOUR_BOT_TOKEN'
    bot_token = os.getenv('BOT_TOKEN')
    chat_id = os.getenv('CHAT_ID')
    print(bot_token)
    print(chat_id)
    bot = telegram.Bot(token=bot_token)
    
    async def send_message():
        await bot.send_message(chat_id=chat_id, text=message)

    asyncio.run(send_message())

else:
    print('Request failed.')
    
#     bot.send_message(chat_id='YOUR_CHAT_ID', text=message)

# else:
#     print('Request failed.')

    
