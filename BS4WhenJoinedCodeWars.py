import requests
from bs4 import BeautifulSoup as bs

def member_since(username):
    try:
        req = requests.get(f'https://www.codewars.com/users/{username}')
        page = bs(req.text, 'html.parser')
        year = page.find_all('div', class_='stat-box mt-1 mb-1 md:mb-0')[1]
        month = year.find('div').text.split(':')[-1]
        return month
    except:
        return 'There is no such user on CodeWars!'


print(member_since(input('Enter username:')))