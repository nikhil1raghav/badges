from fastapi import FastAPI, Response
from topcoder import get_topcoder
from atcoder import get_atcoder
from codeforces import get_codeforces
from codechef import get_codechef
from dmoj import get_dmoj
import uvicorn
import re
import json
import requests
from selectolax.parser import HTMLParser
import pybadges

title={
        "topcoder":"TopCoder",
        "codechef":"Codechef",
        "codeforces":"Codeforces",
        "atcoder":"Atcoder",
        "dmoj":"Dmoj",
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
    elif judge=="dmoj":
        [rating, color, exist]=get_dmoj(user_id)
    else:
        return {"error":"platform not supported"}

    if exist==0:
        return {"error":"user not found"}

    badge = get_badge(rating, color, title[judge], user_id)
    return badge
   
def get_badge(rating:int, color:str, judge:str, user_id:str):
    badge = pybadges.badge(left_text = judge,
            right_text = str(rating),
            right_color = color)
    return Response(content=badge, media_type = 'image/svg+xml')



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)



    





