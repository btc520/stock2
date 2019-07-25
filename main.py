#input and save
#print and check
#update and print 
#API update current price
 
import json

	
def menu ():
	print("1. input and save. ~2. print and check 3. update 4. create new database 5. del one stock all records 6. print summary")
	
	menu_value = raw_input("select in menu")
	if menu_value == '1':
		IN_SA()
	#elif menu_value == '2':
	#	P_C()		
	elif menu_value == '4':
		create_db()
	elif menu_value == '5':
		del_name()
	elif menu_value == '6':
		summary()
	P_C()

def summary():
        with open('data.json') as json_file:
                data = json.load(json_file)
	stock_list = data.keys()
	total_price = 0
	total_share = 0 
	summary_data = {}
	
	for x in stock_list: # dict
		summary_data[x] = []
		for y in data[x]: # list of share and price
				total_price = total_price + int(y['price'])
				total_share = total_share + int(y['share'])
				summary_data[x].append({'total_price':total_price} )
				summary_data[x].append({'total_share': total_share})
	with open('summary_data.json', 'w') as outfile:
                json.dump(summary_data, outfile)


def del_name ():
	with open('data.json') as json_file:
		data = json.load(json_file)

	name = raw_input('enter the name')

	del data[name]

	with open('data.json', 'w') as outfile:
		json.dump(data, outfile)

def create_db ():
	data = {'APPLE' : [ {'price':1, 'share':1}]}
	with open('data.json', 'w') as outfile:
		json.dump(data, outfile)

	
def IN_SA ():
	with open('data.json') as json_file:
		data = json.load(json_file)
		
	#file = open('data.json', 'w+')
	#data = { "name": 'DBC', "share": 1, "price": 21.43 }

	name = raw_input("Stock name? ")
	share = raw_input("Share? ")
	price = raw_input("price? ")
	date = raw_input("date? e.g. 19700430")

	if data.has_key(name):
		data[name].append({'share':share, 'price': price, 'date': date})
	else:
		data[name] = [{'share':share, 'price': price, 'date': date}]

	with open('data.json', 'w') as outfile:
		json.dump(data, outfile)

def P_C ():
	with open('data.json') as json_file:
		data = json.load(json_file)
	print(json.dumps(data, indent=4, sort_keys=True))



menu()
