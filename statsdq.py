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
  # Download ticker and schedule HTML
  html = downloadHTML("http://gamesdonequick.com/ticker")
  soup = BeautifulSoup(html)

  scheduleHTML = downloadHTML("http://gamesdonequick.com/schedule")
  scheduleSoup = BeautifulSoup(scheduleHTML)

  # Extract donations total and goal to get progress bar value
  donTotal = soup.find_all('li')[0].find_all('b')[3].text
  goal = soup.find_all('li')[0].find_all('b')[4].text
  progBarVal = (float(donTotal[1:]) / float(goal[1:])) * 100

  # Lookup ticker game with schedule slot. Convert to lower case because BS4 is case-sensitive by default
  tickerGame = str(soup.find('li','li-blue').find('i').text).lower()
  schedCurrGame = scheduleSoup.find(text=lambda x: x and x.lower()==tickerGame)

  return render_template('index.html', soup=soup, soupSched=scheduleSoup, progBarVal=progBarVal, schedCurrGame=schedCurrGame)

if __name__ == "__main__":
    app.run(debug=True)