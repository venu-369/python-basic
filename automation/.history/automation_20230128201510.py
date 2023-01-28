from credentials import mobile_number
import requests
import schedule
import time

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': mobile_number,
        'message': 'Good morning from V!',
        'key': 'textbelt',

    })
    print(resp.json())

schedule.every().day.at("08:30").do(send_message)