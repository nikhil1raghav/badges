from fastapi import FastAPI, Response
import re
import json
import requests
from selectolax.parser import HTMLParser
import pybadges

title={
        "topcoder":"TopCoder",
        "codechef":"Codechef",
        "codeforces":"Codeforces",
        "atcoder":"Atcoder"
        }

app=FastAPI()
@app.get("/")
async def root():
    return {"greeting":"Hello API is working"}

@app.get("/{judge}/{user_id}")
async def user(user_id:str, judge: str):
    if judge=="topcoder":
        [rating,color,exist]=get_topcoder(user_id)
    elif judge=="codeforces":
        [rating,color,exist]=get_codeforces(user_id)
    elif judge=="codechef":
        [rating,color,exist]=get_codechef(user_id)
    elif judge=="atcoder":
        [rating,color,exist]=get_atcoder(user_id)

    if exist==0:
        return {"error":"user not found"}

    badge = get_badge(rating, color, title[judge], user_id)
    return badge
   
def get_badge(rating:int, color:str, judge:str, user_id:str):
    badge = pybadges.badge(left_text = judge,
            right_text = str(rating),
            right_color = color)
    return Response(content=badge, media_type = 'image/svg+xml')


def get_topcoder(user_id : str):
    url=f"http://api.topcoder.com/v2/users/{user_id}"
    data=requests.get(url).json()
    color="#000"
    if "error" in data:
        return [0,color,0]
    rating = None
    for kind in data["ratingSummary"]:
        if kind["name"] == "Algorithm":
            rating=kind['rating']

    if rating < 900:
        color = "#8e8e81"
    elif rating < 1200:
        color = "#5cb01e"
    elif rating < 1500:
        color = "#1642e5"
    elif rating < 2200:
        color = "#cfe115"
    else:
        color = "#FF0000"
    return [rating, color, 1]

def get_codeforces(user_id : str):
    url=f"https://codeforces.com/api/user.info?handles={user_id}"
    data=requests.get(url).json()
    rating = 0
    color = "#000"
    if data["status"]!="OK":
        return [rating, color, 0]
    rating = data["result"][0]["rating"]
    
    if rating <= 1199:
        color='#cec8c1'
    elif rating <=1399:
        color='#43a217'
    elif rating <=1599:
        color='#22c4ae'
    elif rating <=1899:
        color='#1427b2'
    elif rating<=2099:
        color='#700cb0'
    elif rating<=2299:
        color='#f9a908'
    elif rating<=2399:
        color='#fbb948'
    else:
        color='#ff0000'

    return [rating, color, 1]


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



        






    





