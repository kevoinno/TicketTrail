import requests
import json
import os
import psycopg2
from datetime import datetime

url = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey={os.getenv('CONSUMER_KEY')}"

response = requests.get(url)

print(response.json())
