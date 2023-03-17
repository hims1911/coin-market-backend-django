from django.conf import settings
from backend.celery import app
import requests
from bs4 import BeautifulSoup
import json

@app.task()
def fetch_coin_market_data():
    url = 'https://coinmarketcap.com/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    table = soup.find_all('table')[0]
    rows = table.find_all('tr')
    data = []
    
    for row in rows[1:11]:
        cols = row.find_all('td')
        name = cols[2].text.strip()
        price = cols[3].text.strip()
        change_1h = cols[4].text.strip()
        change_24h = cols[5].text.strip()
        change_7d = cols[6].text.strip()
        market_cap_raw = cols[7].text.strip()
        market_cap_list = market_cap_raw.split('B')
        market_cap = market_cap_list[1]
        volume_24h = cols[8].text.strip().split()[0]
        circulating_supply = cols[9].text.strip()


        data.append({
            'name': name,
            'price': price,
            'change_1h': change_1h,
            'change_24h': change_24h,
            'change_7d' : change_7d,
            'market_cap' : market_cap,
            'volume_24h' : volume_24h,
            'circulating_supply' : circulating_supply
        })
    
    insert(data)    
    
    
 
def insert(data):    
    url = "http://web:8000/coin/" # Replace with the server URL
    headers = {"Content-type": "application/json"}
    response = requests.post(url, data=json.dumps(data), headers=headers)   
        
    print(response.status_code)
    
