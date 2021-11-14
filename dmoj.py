import requests

def get_dmoj(user_id:str):
    url = f"https://dmoj.ca/api/user/info/{user_id}"
    response = requests.get(url)
    color = '#000'

    if response.status_code==404:
        return [0, color, 0]

    data = response.json()
    rating = data["contests"]["current_rating"]
    exist = 1
    if rating < 1000:
        color = '#999999'
    elif rating < 1300:
        color = '#00a900'
    elif rating < 1600:
        color = '#0000ff'
    elif rating < 1900:
        color = '#82068c'
    elif rating < 2400:
        color = '#ffb100'
    else:
        color = '#ee0101'

    return [rating, color, exist]

