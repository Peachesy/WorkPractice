import csv

import pandas as pd

data = pd.read_csv("./data.csv")

# print(data["问题集合"])
# # 五列： 类别，问题分类，问题集合，文本答案，语音合成答案

text_answer = data["文本答案"].tolist()
composited_answer = data["语音合成答案"].tolist()

# 把问题集合拆分开
question_set = data["问题集合"].tolist()
question_sort = data["问题分类"].tolist()
# print(question_sort)
dict_value = []  # 二维列表

for i in question_set:
    temp_str = i.split("||")
    dict_value.append(temp_str)
print("二维列表是：",dict_value)

# 整理数据，准备一行一行的插入数据，需要一个二维列表
data_list = []







# # 把拼接好的字典存入到CSV文件中
# dataframe = pd.DataFrame({"问题":question_sort,"文本答案":text_answer,"语音合成答案":composited_answer})
# dataframe.to_csv("result.csv", index=True, sep=',')



# [["I.II类户办理","I.II类户怎么办理","这里是文本答案","这里是语音合成答案"],["I.II类户办理","I类户怎么办","这里是答案","这里是语音合成答案"]]
# #一行一行写入
# with open("res.csv","w") as csvfile:
#     writer = csv.writer((csvfile))
#     # 列名
#     writer.writerow(["问题类别","问题","文本答案","语音合成答案")
#     #
#     writer.writerows([["I.II类户办理","I.II类户怎么办理","这里是答案"],["I.II类户办理","I类户怎么办","这里是答案"]])

