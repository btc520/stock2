#input and save
#update and print 
#API update current price
 
import json

with open('data.json') as json_file:
    data = json.load(json_file)
	
#file = open('data.json', 'w+')
#data = { "name": 'DBC', "share": 1, "price": 21.43 }

name = raw_input("Stock name? ")
share = raw_input("Share? ")
price = raw_input("price? ")

data[name].append = ({'share':share, 'price': price})

json.dump(data, file)
