import json
from json2table import convert

#from jso2html import *
	

#json_object = {"key" : "value"}
build_direction = "LEFT_TO_RIGHT"
#table_attributes = {"style" : "width:30%", "border" : 1, "class":"container"}
table_attributes = {"style" : "width:15%", "border" : "1px solid black"}

def build_web ():

	with open('data.json') as json_file:
		data = json.load(json_file)
	with open('summary_data.json') as json_file2:
		summary_data = json.load(json_file2)
		
	html_data = convert(data, build_direction=build_direction, table_attributes=table_attributes)
	html_data2 = convert(summary_data, build_direction=build_direction, table_attributes=table_attributes)
	
	index= open("/var/www/html/stock2/index.html","w")
	
	html_header = '''    
	<!DOCTYPE html>
	<html>
	<head>
		<title>GET ALL STOCK!</title>
		<meta http-equiv="content-type" content="text/html; charset=UTF-8" />
		<link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
		<script src="http://libs.baidu.com/jquery/2.0.0/jquery.min.js"></script>
		<script src="http://libs.baidu.com/bootstrap/3.0.3/js/bootstrap.min.js"></script>
	</head>

	<body>
		
	<div class="container">
		<div class="row clearfix">
			<div class="col-md-4 column">
				<h2>
					Heading
				</h2>
				<p>
					%s
				</p>
				<p>
					 <a class="btn" href="#">View details</a>
				</p>
			</div>
			<div class="col-md-4 column">
				<h2>
					Heading
				</h2>
				<p>
					%s
				</p>
				<p>
					 <a class="btn" href="#">View details</a>
				</p>
			</div>
			<div class="col-md-4 column">
				<h2>
					Heading
				</h2>
				<p>
					Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui.
				</p>
				<p>
					 <a class="btn" href="#">View details</a>
				</p>
			</div>
		</div>
	</div>

	</body>
	</html>
	''' % (html_data, html_data2)
	index.writelines(html_header)
	#index.write(html_data)
	#index.write(html_data2)
	index.close()
	
	#html_data =  json2html.convert(json = data) 

	#with open('/var/www/html/stock2/index.html') as index:
        #index.write("wrwerew")