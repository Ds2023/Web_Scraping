import requests
import json
import pprint

url = "https://binance43.p.rapidapi.com/ticker/24hr"
headers = {"X-RapidAPI-Key": "dd8d6d5f1emshe289baf1f73bee2p1db029jsnf996ba4cfbf2",
	"X-RapidAPI-Host": "binance43.p.rapidapi.com"
}
response = requests.get(url,headers=headers).json()
options = ['market summary','gainers','losers']
user_input = ''
input_message = "Pick an option:\n"
for index, item in enumerate(options):
    input_message += f'{index+1}) {item}\n'
input_message += 'Your choice: '
while user_input.lower() not in options:
    user_input = input(input_message)
    print('You picked: ' + user_input)

for x in response:
    keys = []
    items = []
    keys_to_extract = ["priceChangePercent"]
    change = dict(filter(lambda item: item[0] in keys_to_extract, x.items()))
    values = change.values()
    for i in values:
        keys.append(i)
    keys_2 = ["symbol"]
    change_2 = dict(filter(lambda item: item[0] in keys_2, x.items()))
    values_2 = change_2.values()
    for x in values_2:
        items.append(x)
    new_dict = dict(zip(items,keys))
    gainers = {}
    losers = {}
    def ups():
        for i in new_dict:
            if(float(new_dict[i])) > 0:
                gainers[i] = new_dict[i]
                print(gainers)
    def downs():
        for i in new_dict:
            if(float(new_dict[i])) < 0:
                losers[i] = new_dict[i]
                print(losers)
    if user_input == 'gainers':
        ups()
    elif user_input == 'losers':
        downs()
    elif user_input == 'market summary':
        pairs = input("input a coin pair to view:")
        query_params = {"symbol":pairs}
        response_2 = requests.get(url,headers=headers,params=query_params).json()
        output = {key:response_2[key] for key in response_2.keys()-{'askPrice'}-{'askQty'}-{'bidPrice'}-{'bidQty'}-{'closeTime'}-{'count'}-{'firstId'}-{'lastId'}-{'lastQty'}-{'openTime'}-{'prevClosePrice'}-{'quoteVolume'}}
        pprint.pprint(output)
        break
        
