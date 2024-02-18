import Levenshtein
import pypinyin

#常用替换拼音
def replace_char(char_list, di, max_k=6):
    res = set()
    for j in range(len(char_list)):
        for i in range(max_k):
            if j + i > len(char_list):
                break
            if char_list[j : j + i] in di:
                for rv in di[char_list[j : j + i]]:
                    res.add(char_list[:j] + rv + char_list[j + i:])
    return res


def transform_char(char_list):
    res = set()
    # #去掉一个字母
    # for i in range(len(char_list) - 1):
    #     res.add(char_list[:i] + char_list[i + 1:])
    # #相邻拼音换位
    # for i in range(len(char_list) - 2):
    #     res.add(char_list[:i] + char_list[i + 1] + char_list[i] + char_list[i + 2:])
    #相连重复字母保留一个
    for i in range(len(char_list) - 1):
        if char_list[i] == char_list[i + 1]:
            res.add(char_list[:i] + char_list[i + 1:])
    return res


def read_files(filename, use_list=False):
    res = [] if use_list else set()
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if use_list: res.append(line)
            else: res.add(line)
    return res


def max_backward_match(word_list, vocab, max_k=10):
    res = []
    end = len(word_list)
    while end > 0:
        break_flag = False
        for i in range(max_k):
            start = end - max_k + i
            if start < 0: continue
            temp = "".join(word_list[start:end])
            if temp in vocab:
                res.append([temp, start, end])
                end = start
                break_flag = True
                break
        if not break_flag:
            end -= 1
    res.reverse()
    return res


#所有的组合先生成再计算和判断
def get_all_combinations(query_pinyin_list, max_k=5):
    for i in range(len(query_pinyin_list)):
        end = max_k + 1 if max_k + 1 < len(query_pinyin_list) else len(query_pinyin_list)
        for j in range(1, end):
            res = get_all(query_pinyin_list[i : i + j])
    return res


def get_all(arr):
    i = 1
    temp_res = list(arr[0])
    while i < len(arr):
        res = []
        for elem1 in temp_res:
            for elem2 in arr[i]:
                res.append(elem1 + elem2)
        temp_res = res.copy()
        i += 1
    return temp_res


def get_all_list(arr):
    i = 1
    temp_res = [[elem] for elem in arr[0]]
    while i < len(arr):
        res = []
        for elem1 in temp_res:
            for elem2 in arr[i]:
                elem1_copy = elem1.copy()
                elem1_copy.append(elem2)
                res.append(elem1_copy)
        temp_res = res.copy()
        i += 1
    return temp_res


#每个位置上多种可能（汉字、拼音）的编辑距离之和
def min_distance(original_arr, arr):
    dis = 0
    for elem1, elems in zip(original_arr, arr):
        dis += min([Levenshtein.distance(elem1, elem2) for elem2 in elems])
    return dis


#判断是否冲突
#insider: [[i, j, ..]]  outsider[[i, j, ..]]
def check_conflict(insider, outsider):
    res = insider
    for o in outsider:
        flag = True
        for ins in res:
            if not (o[2] >= ins[3] or o[3] <= ins[2]):
                flag = False
                break
        if flag: res.append(o)
    return res


#候选改正词和分词结果还原得到最终改正结果
def get_correct(candidates, cuts):
    res = ""
    candidates_dict = {cand[2]:{"end": cand[3], "word": cand[0]} for cand in candidates}
    i = 0
    while i < len(cuts):
        if i in candidates_dict:
            res += candidates_dict[i]["word"]
            i = candidates_dict[i]["end"]
        else:
            res += cuts[i]
            i += 1
    return res


def get_pinyin(word, mode="all"):
    word_pinyin = pypinyin.pinyin(word, style=pypinyin.NORMAL)
    if mode == "pinyin_list":
        return [elem[0] for elem in word_pinyin]
    elif mode == "pinyin":
        return "".join([elem[0] for elem in word_pinyin])
    elif mode == "start":
        return "".join([elem[0][0] for elem in word_pinyin])
    res = dict()
    res["pinyin_list"] = [elem[0] for elem in word_pinyin]
    res["pinyin"] = "".join(res["pinyin_list"])
    res["start"] = "".join([elem[0][0] for elem in word_pinyin])
    return res


#长串拼音分割，多种路径
def pinyin_split(pinyin, valid_pinyin):
    res = []
    def split_helper(pinyin, pos, before_res):
        if pos >= len(pinyin):
            res.append(before_res)
        for i in range(pos, len(pinyin)+1):
            if pinyin[pos:i] in valid_pinyin:
                before_res_copy = before_res.copy()
                before_res_copy.append(pinyin[pos:i])
                split_helper(pinyin, i, before_res_copy)
    split_helper(pinyin, 0, [])
    #暂时取最小粒度切分结果，最长的一个
    if len(res) == 0: return None
    return sorted(res, key=lambda x: len(x), reverse=True)[0]


def get_stroke_replace(query, gram, stroke_dict, head):
    last_valid = list(filter(lambda x: x is not None, [None if elem not in head and elem != query[0] else elem for elem in stroke_dict.get(query[0], [query[0]])]))
    res = [last_valid.copy()]
    for i in range(1, len(query)):
        last_valid_copy = last_valid.copy()
        last_valid = set()
        for first in last_valid_copy:
            for second in stroke_dict.get(query[i], [query[i]]):
                if second in gram.get(first, []) or second in head or second == query[i]:
                    last_valid.add(second)
        res.append(list(last_valid).copy())
    return res


#拼音合一起，其他单独一个字符
def cut(query):
    res = []
    last_char = False
    for char in query:
        if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
            if last_char:
                res[-1] = res[-1] + char
            else:
                res.append(char)
            last_char = True
        else:
            res.append(char)
            last_char = False
    return res




