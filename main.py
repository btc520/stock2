#input and save
#update and print 
#API update current price
 
import json

file = open('data.json', 'w+')
#data = { "name": 'DBC', "share": 1, "price": 21.43 }
name = raw_input("Stock name? ")
share = raw_input("Share? ")
price = raw_input("price? ")

new_data = {
	name: [
	{'share':share, 'price': price}
]
}

json.dump(new_data, file)
