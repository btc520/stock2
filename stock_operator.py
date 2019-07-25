import json

def open_log ():
	with open('data.json') as json_file:
		data = json.load(json_file)
	return data

def open_summary ():
	with open('summary_data.json') as json_file:
		data = json.load(json_file)
	return data
	
def save_summary (summary_data):
	with open('summary_data.json', 'w') as outfile:
		json.dump(summary_data, outfile)
		
def stock_name_list ():
	with open('data.json') as json_file:
		data = json.load(json_file)
	stock_list = data.keys()
	return stock_list
	
def summary():
	log_data = open_log()
	stock_list = log_data.keys()
	summary_data = {}
	
	for x in stock_list: # dict
		total_value = 0
		total_share = 0 
		summary_data[x] = {}# data in a list, create empty
		for y in log_data[x]: # list of share and price
			
			total_share = round(total_share + float(y['share']),3)
				
			total_value = round( total_value + float(y['share']) * float(y['price']),3)
				
			summary_data[x]['total_price'] = total_value
			summary_data[x]['total_share'] = total_share
				
			avr_price = round(total_value / total_share, 3)
			summary_data[x]['avr_price'] = avr_price
				
	with open('summary_data.json', 'w') as outfile:
                json.dump(summary_data, outfile)



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



def create_db ():
	data = {
			'DBC' :  [ {'date': 20190725, 'price':14.3,     'share':5}          ], \
			'BLV':   [ {'date': 20190725, 'price':89.01191, 'share':10}      ], \
			'EWM' :  [ {'date': 20190725, 'price':29.31,    'share':1}         ], \
			'IGLB' : [ {'date': 20190725, 'price':60.16,    'share':1}        ], \
			'IHY' :  [ {'date': 20190725, 'price':24.78,    'share':1}         ], \
			'MORT' : [ {'date': 20190725, 'price':23.06,    'share':1}        ], \
			'SPXU' : [ {'date': 20190725, 'price':28.59,    'share':2}        ], \
			'SRET' : [ {'date': 20190725, 'price':14.91,    'share':1}        ], \
			'VNM' :  [ {'date': 20190725, 'price':16.72,    'share':1}         ]
	}
	
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