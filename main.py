#input and save
#print and check
#update and print 
#API update current price
 
import json

from yahoo import *
from web import *
from stock_operator import *

def menu ():
	print("1. input and save")
	print("2. print log")
	print("3. update")
	print("4. create new database")
	print("5. del one stock")
	print("6. del one record")
	print("7. print summary")
	print("8. output to HTML")
	menu_value = raw_input("select in menu")
	if menu_value == '1':
		IN_SA()
		P_C()
	elif menu_value == '2':
		P_C()		
	elif menu_value == '3':
		mix_summary()	
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

	elif menu_value == '8':
		build_web()

		



menu()
