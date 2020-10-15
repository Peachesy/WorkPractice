import csv

link = ["www.baidu.com","www,bing.com"]

for i in link:
    with open("WriteCSVTest.csv",'a',newline='') as csvfile:
        writer = csv.writer(csvfile)

        # write cloumns name
        # writer.writerow(["index","a_name","b_name"])

        # write data
        writer.writerows([[i,"en-gb","news today"]])