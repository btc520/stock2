import datetime
from yahoo_historical import Fetcher
from stock_operator import *

def find_price (SYB):
	now = datetime.datetime.now()
	time_now = [now.year,now.month,now.day]

	data = Fetcher(SYB, time_now)

	data_get = data.getHistorical()
	#print (data_get)
	
	open = data_get['Open']
	open_price = float(open[0])
	
	#print (SYB, open_price)
	return open_price

def find_all ():
	log_data = open_log()
	stock_list = log_data.keys() # []
	dict_price_today = {}
	for i in stock_list:
		#print(i)
		#find_price(i)
		dict_price_today[i] = find_price(i)
	return dict_price_today
	
def mix_summary():
	dict_price_today = find_all()
	dict_summary  = open_summary()
	for i in dict_price_today:
		for j in dict_summary:
			if i == j:
				dict_summary[j]['today'] = dict_price_today[i]
	for k in dict_summary:
		raw_cal = (dict_summary[k]['today'] - dict_summary[k]['avr_price']) / dict_summary[k]['avr_price'] * 100
		dict_summary[k]['bias'] = round (raw_cal, 3)
	
	save_summary (dict_summary)
	