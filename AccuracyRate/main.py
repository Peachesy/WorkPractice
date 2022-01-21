from Accuracy import *
from WashData import *

def main():
    file = r'test.csv'
    with open(file, encoding='utf-8') as f:
        data = np.loadtxt(f, str, delimiter=",")
        query_list = data[:, 0]  # original query
        res_list = data[:, 1]  # asr recognized result
        print(query_list)
        print(res_list)

    # 去掉文本中的标点符号
    wd = WashData()
    wd.wash_data(query_list, res_list)

    new_query_list = []
    new_rec_list = []
    for i in wd.washed_query_list:
        new_query_list.append(list(i))
    # print(new_query_list)
    for j in wd.washed_rec_list:
        new_rec_list.append(list(j))
    # print(new_rec_list)

    result = Accuracy()
    # 计算距离
    for i, j in zip(new_rec_list, new_query_list):
        result.levenshtein_distance(j, i)
    # 处理数据
    result.process_para_data()
    # 计算字错误率
    result.wer()
    # 计算句错误率
    result.ser(wd.washed_query_list, wd.washed_rec_list)


if __name__ == '__main__':
    main()