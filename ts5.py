from flask import Flask, request
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

@app.get('/currency')
def currency():

    date = datetime.now()
    if "yesterday" in request.args:
        date -= timedelta(days=1)

    d = date.strftime("%Y%m%d")

    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=EUR&date={d}&json"
    rate = requests.get(url).json()[0]["rate"]

    return f"EUR: {rate}"

if __name__ == "__main__":
    app.run(port=8000)
