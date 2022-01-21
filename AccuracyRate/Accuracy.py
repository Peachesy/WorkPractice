import numpy as np
import pandas as pd
import csv


class Accuracy:
    total_s = 0
    total_d = 0
    total_i = 0
    total_w = 0
    total_c = 0
    total_n = 0
    total_para = []
    wer_res:float = 0

    # 计算参数
    def levenshtein_distance(self, hypothesis: list, reference: list):
        """编辑距离
        计算两个序列的levenshtein distance，可用于计算 WER/CER
        参考资料：https://martin-thoma.com/word-error-rate-calculation/


        C: correct
        W: wrong
        I: insert
        D: delete
        S: substitution

        :param hypothesis: Original query list
        :param reference: ASR recognized result list
        :return: 1: 错误操作，所需要的 S，D，I 操作的次数;
                 2: ref 与 hyp 的所有对齐下标
                 3: 返回 C、W、S、D、I 各自的数量
        """
        len_hyp = len(hypothesis)  # 只是列表的长度，而这个列表的元素是一句话，即字符串
        len_ref = len(reference)   # length 计算的不是Query的总字数
        cost_matrix = np.zeros((len_hyp + 1, len_ref + 1), dtype=np.int16)

        # 记录所有的操作，0-equal；1-insertion；2-deletion；3-substitution
        ops_matrix = np.zeros((len_hyp + 1, len_ref + 1), dtype=np.int8)

        # min(i,j)=0
        for i in range(len_hyp + 1):
            cost_matrix[i][0] = i
        for j in range(len_ref + 1):
            cost_matrix[0][j] = j

        # 生成 cost 矩阵和 operation矩阵，i:外层hyp，j:内层ref
        for i in range(1, len_hyp + 1):
            for j in range(1, len_ref + 1):
                if hypothesis[i-1] == reference[j-1]:
                    cost_matrix[i][j] = cost_matrix[i-1][j-1]
                else:
                    substitution = cost_matrix[i-1][j-1] + 1
                    insertion = cost_matrix[i-1][j] + 1
                    deletion = cost_matrix[i][j-1] + 1

                    compare_val = [insertion, deletion, substitution]   # 回溯优先级 I D S
                    min_val = min(compare_val)
                    operation_idx = compare_val.index(min_val) + 1
                    cost_matrix[i][j] = min_val
                    ops_matrix[i][j] = operation_idx

        match_idx = []  # 保存 hyp与ref 中所有对齐的元素下标
        i = len_hyp
        j = len_ref
        nb_map = {"N": len_hyp, "C": 0, "W": 0, "I": 0, "D": 0, "S": 0}
        while i >= 0 or j >= 0:
            i_idx = max(0, i)
            j_idx = max(0, j)

            if ops_matrix[i_idx][j_idx] == 0:     # correct
                if i-1 >= 0 and j-1 >= 0:
                    match_idx.append((j-1, i-1))
                    nb_map['C'] += 1

                # 出边界后，这里仍然使用，应为第一行与第一列必然是全零的
                i -= 1
                j -= 1
            elif ops_matrix[i_idx][j_idx] == 1:   # insert
                i -= 1
                nb_map['I'] += 1
            elif ops_matrix[i_idx][j_idx] == 2:   # delete
                j -= 1
                nb_map['D'] += 1
            elif ops_matrix[i_idx][j_idx] == 3:   # substitute
                i -= 1
                j -= 1
                nb_map['S'] += 1

            # 出边界处理
            if i < 0 and j >= 0:
                nb_map['D'] += 1
            elif j < 0 and i >= 0:
                nb_map['I'] += 1

        match_idx.reverse()
        # print('对齐的元素的下标：',match_idx)
        wrong_cnt = cost_matrix[len_hyp][len_ref]
        nb_map["W"] = wrong_cnt

        self.total_para.append(nb_map)
        print("ASR识别结果: %s" % " ".join(reference))
        print("原始的Query: %s" % " ".join(hypothesis))
        print("nb_map is:",nb_map)
        # print("对齐的元素的下标match_idx: %s" % str(match_idx))
        # print("所有参数列表：", self.total_para)
        print()

        return wrong_cnt, match_idx, nb_map

    # 处理计算各种参数的总数
    def process_para_data(self):
        for i in self.total_para:
            # print("i是：",i)
            # print("i的类型是：",type(i))
            self.total_i = self.total_i + int(i['I'])
            self.total_d = self.total_d + int(i['D'])
            self.total_s = self.total_s + int(i['S'])
            self.total_w = self.total_w + int(i['W'])
            self.total_c = self.total_c + int(i['C'])
            self.total_n = self.total_n + int(i['N'])
        print("N:", self.total_n)
        print("I:",self.total_i)
        print("D:",self.total_d)
        print("S:",self.total_s)
        print("W:",self.total_w)
        print("C:",self.total_c)
        return self.total_n,self.total_c,self.total_w,self.total_d,self.total_s,self.total_i

    # WER字错误率
    def wer(self):
        if self.total_n != 0:
            self.wer_res = (self.total_s + self.total_d + self.total_i) / (self.total_s + self.total_d + self.total_n)
        else:
            print("总字数为0!!!!")
        print()
        print("字错误率WER为：%.2f%%" % (self.wer_res*100))
        wcr = 1-self.wer_res
        print("字准确率WCR为：%.2f%%" % (wcr*100))
        return self.wer_res

    # SER句错误率
    def ser(self, query_list, rec_list):
        cnum = 0
        enum = 0
        for i,j in zip(query_list,rec_list):
            if i == j:
                cnum = cnum +1
            else:
                enum = enum +1
        # print("正确的句数：", cnum)
        # print("错误的句数：", enum)
        if len(query_list) != 0:
            ser_rate = enum/len(query_list)
        print("句错误率SER为：%.2f%%" % (ser_rate * 100))
        print("句准确率SCR为：%.2f%%" % ((1-ser_rate) * 100))




