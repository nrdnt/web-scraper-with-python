import requests
from bs4 import BeautifulSoup
import telegram
import os
from dotenv import load_dotenv
import asyncio

# Load environment variables from .env file
load_dotenv()

url = os.getenv("URL")
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
    

    
