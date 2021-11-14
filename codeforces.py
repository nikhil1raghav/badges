import requests, json

def get_codeforces(user_id:str):
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