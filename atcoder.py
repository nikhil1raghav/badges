import requests
from selectolax.parser import HTMLParser


def get_atcoder(user_id:str):
    url = f"https://atcoder.jp/users/{user_id}"
    page = requests.get(url)
    # page.text is an object ,  page.text() is a string
    table = HTMLParser(page.text).css('.dl-table')
    if len(table)==0:
        return [0, rating, 0]
    rating = int(table[1].css('span')[0].text())
    color = 'black'
    if rating <= 399:
        color = '#7c7c7c'
    elif rating > 399 and rating <= 799:
        color = '#7c3e00'
    elif rating > 799 and rating <= 1199:
        color = '#007c00'
    elif rating > 1199 and rating <= 1599:
        color = '#00c0c0'
    elif rating > 1599 and rating <= 1999:
        color = '#0000f8'
    elif rating > 1999 and rating <= 2399:
        color = '#baba00'
    elif rating > 2399 and rating <= 2799:
        color = '#fe7f00'
    else:
        color = '#ff0000'

    return [rating, color, 1]