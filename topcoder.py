import requests
def get_topcoder(user_id:str):
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

