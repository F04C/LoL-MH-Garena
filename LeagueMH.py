import json
from urllib.request import urlopen


def getAccountID(name_input):
    response = urlopen(
        "https://acs-garena.leagueoflegends.com/v1/players?name=" + name_input + "&region=PH").read().decode(
        'utf-8')
    responseJson = json.loads(response)
    return responseJson.get("accountId")


name_input = input("Enter IGN: ")
account_id_scraped = str(getAccountID(name_input))

print(name_input)
print(getAccountID(name_input))


# def getAccountIDScraped(account_id_scraped):
#     response = urlopen(
#         "https://acs-garena.leagueoflegends.com/v1/stats/player_history/PH/" + accountIdScraped + "?begIndex=0&endIndex=20&").read().decode(
#         'utf-8')
#     responseJson1 = json.loads(response)
#     for win in responseJson1['games']:
#         print(win['win'])
