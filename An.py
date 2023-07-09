from art import *
import colorama
from colorama import Fore, Style

# אתחול ספריית colorama
colorama.init()

text = text2art("ediTop")
colored_text = ""
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
color_index = 0

for char in text:
    if char != "\n":
        colored_char = colors[color_index % len(colors)] + char + Style.RESET_ALL
        colored_text += colored_char
        color_index += 1
    else:
        colored_text += "\n"

print(colored_text)

import requests

api_url = 'https://stips.co.il/api'

def send_response(question_id, answer):
    data = f'name=omniobj&rest_action=PUT&omniobj={{"data":{{"askid":{question_id},"name":"תשובה מתאימה לשאלה {question_id}","anonflg":false,"a":"{answer}"}}}}&objType=ans'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        # Add other required headers here
    }

    try:
        response = requests.post(api_url, data=data, headers=headers)
        if response.status_code == 200:
            print(f'Response sent for question {question_id}')
        else:
            print(f'Failed to send response for question {question_id}')
    except requests.exceptions.RequestException as e:
        print(f'Error occurred for question {question_id}: {str(e)}')

def main():
    start_question_id = int(input('Enter the starting question ID: '))
    end_question_id = int(input('Enter the ending question ID: '))
    answer = input('Enter the answer: ')

    for question_id in range(start_question_id, end_question_id + 1):
        send_response(question_id, answer)

if __name__ == '__main__':
    main()
