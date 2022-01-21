from Accuracy import *

def main():

    file = r'test.csv'
    with open(file, encoding='utf-8') as f:
        data = np.loadtxt(f, str, delimiter=",")
        query_list = data[:, 0]  # original query
        res_list = data[:, 1]  # asr recognized result
        # print(query_list)
        # print(res_list)

    result = Accuracy()
    # 计算总字数
    result.total_paran(query_list)
    # 计算距离
    result.levenshtein_distance(res_list, query_list)
    # 计算字错误率
    result.wer()





if __name__ == '__main__':
    main()