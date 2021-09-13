import pandas as pd

class Data_process:

    processed_title = []
    double_check_link = []
    comment = []


    def Compare_data(self,Market, Links, No_Category_bar, Changed_URL, Query_in_search_box,Title, Top_stories_button):

        # 第一步处理title，把title中带有除top stories之外的信息去掉
        for i in Title:
            if "\n" in i:
                # 处理该元素，去掉\n之后的内容
                res = i.split("\n")
                # 获取元素i对应的索引值
                target_index = Title.index(i)
                Title[target_index] = res[0]
            else:
                return Title


        # 第二步比较数据
        # 1.Changed URL为http://stcav-867/ 的，需要重新拼接链接（http://stcav-867/?mkt=en-us&setlang=en-us）到main.py中进行二次验证，
        # 点击entry point中的news之后是否还继续跳转到HP，如果是，就在comment中追加信息“跳回HP，by design”，如果不是，就在comment中追加“跳回HP，是个bug”


    def Check_double_check(self,market,url,changed_url):
        for i in changed_url:
            Dealed_i = i.strip( )
            if Dealed_i == "http://stcav-867/":
                temp_link = url + "?mkt=" + market + "&setlang=" + market
                self.double_check_link.append(temp_link)
                # print("Need to double check link :", self.double_check_link)
            else:
                self.double_check_link.append(-1)




    def Double_check_result(self, market,Checked_url):

        for i in Checked_url:
            # 去掉字符串中开头和结尾的空格
            Dealed_i = i.strip( )
            if Dealed_i == "http://stcav-867/":
                self.comment.append("Jump back to HP, by design")
            else:
                self.comment.append("Jump back to HP, it's a bug")


    def Save_data_to_CSV(self, Market_Forms, Links, No_Category_bar, Changed_URL, Query_in_search_box,Title, Top_stories_button,comment):

        # 先把列表转换为字典，再写入到CSV
        dict = {'Market & Forms':Market_Forms, 'Original Links':Links, 'No category bar':No_Category_bar, 'Changed URL':Changed_URL,
                'Query in search box':Query_in_search_box, 'Title':Title, 'Text in top stories button':Top_stories_button, 'Comment':comment}

        df = pd.DataFrame(dict)

        # 保存dataframe到CSV
        df.to_csv('result.csv')



    # 2.如果有category bar，检查是否有search query，如果有，就在comment中追加“有search query”，
    # 此时再比较Query_in_search_box,Title, Top_stories_button三者是否一致，一致的话comment追加“且Query_in_search_box,Title, Top_stories_button三者一致”，
    # 不一致的话返回“Query_in_search_box,Title, Top_stories_button三者不一致”
    # 如果没有search query，comment 追加“无search query”