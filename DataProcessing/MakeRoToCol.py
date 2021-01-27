import csv
from collections import defaultdict

FilePath = r"E:\OneDrive - Microsoft\Desktop\Hitapp\OriginalData.csv"

with open(FilePath,'r+',encoding='utf-8') as f:
    Reader = csv.DictReader(f)
    print(Reader)
    for col in Reader:
        # print("col.items()是什么", col.items())
        d = {}
        for k,v in col.items():
            d[k] = v
        print(d)


a = []
dict = d
for headers in sorted(dict.keys()): # 把字典的键取出来
    a.append(headers)
headers = a   #把列名给提取出来，用列表形式呈现


with open('ProcessedData.csv','a',newline='',encoding='utf-8') as f:
    writer = csv.DictWriter(f,fieldnames=headers) # 提前预览列名，当下面代码写入数据时会将其一一对应
    writer.writeheader() # 写入列名
    writer.writerows(d) # 写入数据
print("数据写入成功！")