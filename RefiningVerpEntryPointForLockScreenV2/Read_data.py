import pandas as pd

# http://stcav-867/news/search?q=&setmkt=en-us&setlang=en-us&form=m4021s

domain = "http://stcav-867/news/search?q="

# 读取数据文件
data = pd.read_csv("data.csv")
# print(data)
# print(type(data))
True_market = data['True market'].tolist()

# print("True market的值：", True_market)

# 拼接链接
links = []
key = []
forms = ["m4021s", "m4021t","m4021u","m4021v","m4021w","m4021x"]

# FormCode list: "m4021s", "m4021t","m4021u","m4021v","m4021w","m4021x"

for n in forms:
    for i in True_market:
        # print(i)
        # print("i:",type(i))
        temp_str = domain + "&mkt=" + i + "&setlang=" + i + "&form=" + n
        links.append(temp_str)
        key.append(i)

# print("链接: ", links)
# print("key: ", key)
# print("form参数", forms)

union_key = []

# 在每个key后面增加一个-form，作为字典的key
for i in forms:
    for j in True_market:
        temp = j + "-" + i
        union_key.append(temp)

# print("组合后的key：", union_key)


# 把读取的数据拼接为字典
market_data = dict(zip(union_key, links))
print("拼接后的字典：",market_data)


