#input and save
#print and check
#update and print 
#API update current price
 
import json

	
def menu ():
	print("1. input and save")
	print("2. print log")
	print("~3. update")
	print("4. create new database")
	print("5. del one stock")
	print("6. del one record")
	print("7. print summary")

	menu_value = raw_input("select in menu")
	if menu_value == '1':
		IN_SA()
		P_C()
	elif menu_value == '2':
		P_C()		
	elif menu_value == '4':
		create_db()
		P_C()
	elif menu_value == '5':
		del_name()
	elif menu_value == '6':
		del_record()
		
	elif menu_value == '7':
		summary()
		Pnt_S ()
		
def del_record ():
	with open('data.json') as json_file:
		data = json.load(json_file)

	name = raw_input('enter the name')
	time = raw_input('enter the purchase time')
	
	for i in data: # i=list
		print(i)
		for j in data[i]: # j is dict
			#print(j)
			if j["date"] == str(time):
				print ("index", data[i].index(j))
				position = data[i].index(j)		
				del  data[i][position]

	with open('data.json', 'w') as outfile:
		json.dump(data, outfile)
		
def del_name ():
	with open('data.json') as json_file:
		data = json.load(json_file)

	name = raw_input('enter the name')
	del data[name]

	with open('data.json', 'w') as outfile:
		json.dump(data, outfile)
		
def Pnt_S ():
	with open('summary_data.json') as json_file:
		summary_data = json.load(json_file)
	print(json.dumps(summary_data, indent=4, sort_keys=True))

def summary():
    	with open('data.json') as json_file:
		data = json.load(json_file)
	stock_list = data.keys()

	summary_data = {}
	
	for x in stock_list: # dict
		total_value = 0
		total_share = 0 
		summary_data[x] = [1, 2, 3, 4] # data in a list, create empty
		for y in data[x]: # list of share and price
			
			total_share = round(total_share + float(y['share']),3)
				
			total_value = round( total_value + float(y['share']) * float(y['price']),3)
				
			summary_data[x][0] = {'total_price':total_value} 
			summary_data[x][1] = {'total_share': total_share}
				
			avr_price = round(total_value / total_share, 3)
			summary_data[x][2] = {'avr_price': avr_price}
				
	with open('summary_data.json', 'w') as outfile:
                json.dump(summary_data, outfile)




def create_db ():
	data = {'APPLE' : [ {'date': 19710102, 'price':1, 'share':1}]}
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
