import pandas as pd
from pandas import DataFrame as df
# http://suz-pc/search?form=QBLH&sp=-1&pq=biden&sc=7-5&qs=n&sk=&cvid=5D78072A1C914DF995440E1317CC12B5&setflight=enopenserp&setmkt=en-gb&q=greg+wise
# temp = "&setmkt=" + key + "&setlang=" + key + "&q=" + value

class ReadData():

    domain = "http://suz-pc/search?form=QBLH&sp=-1&pq=biden&sc=7-5&qs=n&sk=&cvid=5D78072A1C914DF995440E1317CC12B5&setflight=enopenserp"

    data = pd.read_csv('./MarketList.csv')
    print(type(data))

    query = data['Query'].tolist()
    market = data['Market'].tolist()
    print(len(query))
    print(len(market))
    # data_dict = dict(zip(market,query))
    data_dict = dict(map(lambda x,y:[x,y],market,query))
    print(data_dict)
    print(len(data_dict))

