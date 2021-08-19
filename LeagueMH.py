import json
from urllib.request import urlopen

def getAccountID(name_input):
    response = urlopen(
        "https://acs-garena.leagueoflegends.com/v1/players?name=" + name_input + "&region=PH").read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get("accountId")

name_input = input("Enter IGN: ")

print("Account ID:" + str(getAccountID(name_input)))

account_id_scraped = (getAccountID(name_input))

id = str(account_id_scraped)

def getAccountIDScraped(id):
  response1 = urlopen("https://acs-garena.leagueoflegends.com/v1/stats/player_history/PH/" + id + "?begIndex=0&endIndex=10&").read().decode('utf-8')
  responseJson1 = json.loads(response1)
  return responseJson1.get("games")

data = getAccountIDScraped(id)

data['games']

values = data['games']

for datum in values:
   b = values[0]

rankedindex = datum['gameType']
participants = datum['participants']

for datainparticipants in participants:
  a = participants[0]

winornot = datainparticipants['stats']

eitherwinornot = winornot['win']

def get_matches():
  values = data['games']
  for datum in values:
    participants = datum['participants']
    for datainparticipants in participants:
        winornot = datainparticipants['stats']['win']
        print("Win: " + str(winornot))

get_matches()

#print win based on gameId in data['games']