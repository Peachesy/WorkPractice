import pandas as pd

domain = "http://stcav-867/news/search?FORM=Z9LH3"

# 读取数据文件
data = pd.read_csv("test.csv")
print(data)
print(type(data))
True_market = data['True market'].tolist()

# 拼接链接
links = []
key = []

for i in True_market:
    print(i)
    print("i:",type(i))
    temp_str = domain + "&mkt=" + i + "&setlang=" + i
    links.append(temp_str)
    key.append(i)

print("链接: ", links)

# 把读取的数据拼接为字典
market_data = dict(zip(key,links))
print("拼接后的字典：",market_data)


