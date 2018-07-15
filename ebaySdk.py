import datetime
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection

appid = "DhruboSa-SearchIt-PRD-18bb074f4-4c2900c3"
keyword = ""

try:
    api = Connection(appid=appid, config_file=None)
    response = api.execute('findItemsAdvanced', {'keywords': 'white and shirt'})
    # print(response.dict())
    assert(response.reply.ack == 'Success')
    assert(type(response.reply.timestamp) == datetime.datetime)
    assert(type(response.reply.searchResult.item) == list)
    #
    item = response.reply.searchResult.item
    for eachItem in item:
        print("Printing Item : ==>")
        print("Listing Type : "+ eachItem.listingInfo.listingType)
        print("Current Price : "+ str(eachItem.sellingStatus.convertedCurrentPrice))
        print("Show Item URL : " + eachItem.viewItemURL)
    # assert(type(item.listingInfo.endTime) == datetime.datetime)
    # assert(type(response.dict()) == dict)

except ConnectionError as e:
    print(e)
    print(e.response.dict())