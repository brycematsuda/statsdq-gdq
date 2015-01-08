from flask import Flask, render_template
import requests, json
from bs4 import BeautifulSoup

app = Flask(__name__)

def downloadHTML(url):
  assert url.startswith('http://')
  req = requests.get(url)
  if req.status_code == 200:
    return req.text
  else:
    return ''

def downloadJSON(url):
  assert url.startswith('https://')
  req = requests.get(url)
  if req.status_code == 200:
    return req.content
  else:
    return ''


@app.route("/")
def index():
  html = downloadHTML("http://gamesdonequick.com/ticker")
  soup = BeautifulSoup(html)

  scheduleHTML = downloadHTML("http://gamesdonequick.com/schedule")
  scheduleSoup = BeautifulSoup(scheduleHTML)

  twitchJSON = downloadJSON("https://api.twitch.tv/kraken/channels/gamesdonequick")
  twitchOutput = json.loads(twitchJSON)

  donTotal = soup.find_all('li')[0].find_all('b')[3].text
  goal = soup.find_all('li')[0].find_all('b')[4].text
  progBarVal = (float(donTotal[1:]) / float(goal[1:])) * 100

  return render_template('index.html', soup=soup,json=twitchOutput, soupSched=scheduleSoup, progBarVal=progBarVal)

if __name__ == "__main__":
    app.run(debug=True)