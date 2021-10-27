import requests
import uvicorn
from googletrans import Translator
from fastapi import FastAPI, Query, Request, Response
from fastapi.responses import HTMLResponse
from starlette.exceptions import HTTPException

translator = Translator()

app = FastAPI()


@app.exception_handler(HTTPException)
async def custom_http_exception_handler(_request, exc):
    # url = 'https://vtt-c.udemycdn.com/36329760/en_US/2021-09-21_14-03-06-152ae44c63a52f1574b230a34c3cdf55.vtt?Expires=1633928636&Signature=VGaze81c0QREue-z1DwaJFNj5xC4bvGqY8DgHLy3kBpHnWBsFQnMdAnm6Xe0-9FnDjlBMdBy-xeCsdDbE-vDPvxrFspRbFQoapL1TVzly7FUy6UKf4g77w9oZhsyjdV6kRdqSfJlYtIlifFHgb0qctbRxwXkH3GmAuNOrj3vwloi2ihgRWdhPS2ftlifuIKcoMN3ovD0hMpPeg1ppEsa~EgR7IOq4eFfSskVz5b0kYAwRys0w7ibNv0zMLyFK49QLysBU8UCXHUmR5oCXDT2~c9fhx6wSz6dmJJW8CJl9e-PSxG7UyXNqmniG8AeM~dnvZA7pZrvE9vszaX-JiXxkg__&Key-Pair-Id=APKAITJV77WS5ZT7262A'
    url = _request.url.query
    print(url)

    r = requests.get(url)
    r2 = translator.translate(r.text, src='en', dest='ru').text.replace(': ', ':').replace(' -> ', ' --> ')
    return HTMLResponse(r2, headers={'Content-Type': r.headers['content-type'],
                                     'Access-Control-Allow-Origin': '*'})



if __name__ == "__main__":
    uvicorn.run('main:app',
                host="0.0.0.0",
                port=8080,
                reload=True,
                )
