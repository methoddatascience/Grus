key = 'DhruboSa-SearchIt-PRD-18bb074f4-4c2900c3'


search = "T-shirt and green"


import json
import requests
searches = []

url = ('http://svcs.ebay.com/services/search/FindingService/v1\
?OPERATION-NAME=findItemsByKeywords\
&sortOrder=PricePlusShippingLowest\
&buyerPostalCode=92128&SERVICE-VERSION=1.13.0\
&SECURITY-APPNAME=' + key +
'&RESPONSE-DATA-FORMAT=JSON\
&REST-PAYLOAD\
&itemFilter(0).name=Condition\
&itemFilter(0).value=New\
&itemFilter(1).paramName=Currency\
&itemFilter(1).paramValue=USD\
&keywords=' + search)
url = url.replace(" ", "%20")
apiResult = requests.get(url)
parseddoc = apiResult.json()
for item in (parseddoc["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"]):
	title = item["title"][0]
	condition = item['condition'][0]['conditionDisplayName'][0]
	price = item['sellingStatus'][0]["convertedCurrentPrice"][0]['__value__']
	print("item description start")
	print("Title is: " +title + " price is: " + price + " condition is :" + condition)



# &itemFilter(1).name=MaxPrice\
# &itemFilter(1).value=' + MaxPrice+\
# '


























