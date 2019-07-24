#input 
#print 
#API update current price
 
import json

file = open('data.json', 'w+')
data = { "name": 'DBC', "share": 1, "price": 21.43 }

json.dump(data, file)
