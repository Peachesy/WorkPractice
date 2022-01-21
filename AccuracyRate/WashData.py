import re


class WashData:
    washed_query_list = []
    washed_rec_list = []

    # 去掉文本中的标点符号
    def wash_data(self,query_list,rec_list):
        # r='[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'
        r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\n。！，]+'
        for i,j in zip(query_list,rec_list):
            tempi = re.sub(r, '', i)
            tempj = re.sub(r,'',j)
            self.washed_query_list.append(tempi)
            self.washed_rec_list.append(tempj)

        print("清洗后的Query列表：", self.washed_query_list)
        print("清洗后的rec列表：", self.washed_rec_list)

        return self.washed_query_list, self.washed_rec_list
