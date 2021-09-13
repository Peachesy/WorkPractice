
str = "Top stories\nPowered by Microsoft News"
str_list =["en-us-m4021s","Top stories\nPowered by Microsoft News","fr-fr-m4021t","de-de-m4021u"]

if "\n" in str:
    print("发现了回车")

else:
    print("没发现")

for i in str_list:
    if "-m4021" in i:
        print("列表中的元素里有回车")
        res = i.split("-m4021")  # top stories被分割到res[0]中
        print(res)
        print(res[0])
        target_index = str_list.index(i)
        print("%s对应的索引值为：%d"% (i,target_index))
        str_list[target_index] = res[0]
        # str_list[1] = res[0]
        print("处理后的列表：", str_list)
    else:
        print("列表中元素里没发现回车")