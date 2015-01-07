from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def downloadHTML(url):
  assert url.startswith('http://')
  req = requests.get(url)
  if req.status_code == 200:
    return req.text
  else:
    return ''

@app.route("/")
def index():
  html = downloadHTML("http://gamesdonequick.com/ticker")
  soup = BeautifulSoup(html)
  return render_template('index.html', soup=soup)

if __name__ == "__main__":
    app.run(debug=True)