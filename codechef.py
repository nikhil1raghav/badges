import requests
from selectolax.parser import HTMLParser
def get_codechef(user_id:str):
     # handle when user doesn't exist
    color='#000'
    url=f'https://www.codechef.com/users/{user_id}'
    page=requests.get(url)
    rating = HTMLParser(page.text).css('.rating-number')
    if len(rating)==0:
        return [0,color,0]

    rating = int(rating[0].text())

    if rating <= 1399:
        color = '#666666'
    elif rating <= 1599:
        color = '#1e7d22'
    elif rating <= 1799:
        color = '#3366cc'
    elif rating <= 1999:
        color = '#684273'
    elif rating <= 2199:
        color = '#ffbf00'
    elif rating <= 2499:
        color = '#ff7f00'
    else:
        color = '#ff1b1b'
    
    return [rating, color, 1]
    