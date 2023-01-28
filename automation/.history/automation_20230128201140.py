from credenrials import mobile_number
import requests

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': mobile_number,
        'message': 'Hello from Python!',
        'key': 'textbelt',

    })
    print(resp.json())