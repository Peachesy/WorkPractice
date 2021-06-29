import pandas as pd

domain = "http://stcav-867/"

# 读取数据文件
data = pd.read_csv("test.csv")
# print("读取的数据结果：",data)
# 通过pandas DataFrame values把读取的CSV结果转为list
mapping_market = data.values.tolist()  # 二维列表

key = []
for i in data['Mapping market']:
    key.append(i)

# 拼接链接
links = []
# 取出二维列表data中的第0列
market_col = [x[0] for x in mapping_market]
for i in market_col:
    # print("i:",type(i))
    temp_str = domain + "?mkt=" + i + "&setlang=" + i
    links.append(temp_str)
# print(links)

# 把读取的数据拼接为字典
market_data = dict(zip(key,links))
# print("拼接后的字典：",market_data)


