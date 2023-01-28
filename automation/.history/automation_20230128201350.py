from credentials import mobile_number
import requests
import schedule
import time

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': mobile_number,
        'message': 'Hello from Python!',
        'key': 'textbelt',

    })
    print(resp.json())