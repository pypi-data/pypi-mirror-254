import Levenshtein
import pypinyin
import edit_distance_correction.utils as utils
import pandas as pd
import re
import jieba
from itertools import chain
import os

_get_module_path = lambda path: os.path.normpath(os.path.join(os.getcwd(),
                                                 os.path.dirname(__file__), path))
class Corrector:
    def __init__(self):
        self.max_k = 0
        #pinyin:set(word)
        self.pinyin_di = dict()
        self.target_word = dict()
        #start:set(pinyin)
        self.start_pinyin_di = dict()
        self.start_word_di = dict()
        self.correction_dict = dict()
        self.same_stroke_dict = dict()
        self.same_stroke_head = set()
        self.gram = dict()
        self.valid_pinyin = set()
        self._load_correction()
        self._load_same_stroke()
        self._load_valid_pinyin()


    def _load_valid_pinyin(self):
        self.valid_pinyin = utils.read_files(_get_module_path("valid_pinyin"))


    def _load_correction(self):
        correction = pd.read_excel(_get_module_path("correction.xlsx"))
        for original, corr in zip(correction["original"], correction["correction"]):
            if original not in self.correction_dict:
                self.correction_dict[original] = set()
            self.correction_dict[original].add(corr)


    def _load_same_stroke(self):
        with open(_get_module_path("same_stroke.txt")) as f:
            for line in f:
                line = line.strip()
                if line.startswith("#"):
                    continue
                arr = re.split("\s+", line)
                if len(arr) > 1:
                    for i, elem1 in enumerate(arr):
                        for j, elem2 in enumerate(arr):
                            if elem1 not in self.same_stroke_dict:
                                self.same_stroke_dict[elem1] = set()
                            self.same_stroke_dict[elem1].add(elem2)


    def load_target_words(self, target_words):
        for word in target_words:
            if len(word) > self.max_k:
                self.max_k = min(10, len(word))
            res = utils.get_pinyin(word, True)
            if res["pinyin"] not in self.pinyin_di:
                self.pinyin_di[res["pinyin"]] = set()
            self.pinyin_di[res["pinyin"]].add(word)
            if res["start"] not in self.start_pinyin_di:
                self.start_pinyin_di[res["start"]] = set()
            self.start_pinyin_di[res["start"]].add(res["pinyin"])
            if res["start"] not in self.start_word_di:
                self.start_word_di[res["start"]] = set()
            self.start_word_di[res["start"]].add(word)
            if len(word) > 0:
                self.same_stroke_head.add(word[0])
            self.target_word[word] = res["pinyin"]

            for i in range(len(word)):
                if word[i] not in self.gram:
                    self.gram[word[i]] = set()
                if i == len(word) - 1:
                    self.gram[word[i]].add("")
                else:
                    self.gram[word[i]].add(word[i+1])


    def _transform_pinyin(self, pinyin, include_self=False):
        res = utils.replace_char(pinyin, self.correction_dict, max_k=6)
        res = res.union(utils.transform_char(pinyin))
        if include_self:
            res.add(pinyin)
        return res


    def max_backward_match_transform(self, word_list, vocab, max_k=10):
        res = []
        second_res = []
        end = len(word_list)
        while end > 0:
            break_flag = False
            for i in range(max_k):
                start = end - max_k + i
                if start < 0: continue
                temp = "".join(word_list[start:end])
                temp_res = self._transform_pinyin(temp)
                #直接匹配是最好的
                if temp in vocab:
                    res.append([temp, start, end])
                    end = start
                    break_flag = True
                    break
                #其次是有转换的匹配
                else:
                    for second_temp in temp_res:
                        if second_temp in vocab:
                            second_res.append([second_temp, start, end, temp])
            if not break_flag:
                end -= 1
        res.reverse()
        return res, second_res


    def recall_word(self, query):
        #temp_cuts = jieba.lcut(query)
        temp_cuts = utils.cut(query)
        cuts = []
        for cut in temp_cuts:
            if re.search("^[a-zA-Z]+$", cut) is not None:
                res = utils.pinyin_split(cut, self.valid_pinyin)
                if res is None:
                    cuts.append(cut)
                else:
                    cuts.extend(res)
            else:
                cuts.append(cut)

        # cuts_stroke = [utils.get_all([list(self.same_stroke_dict.get(char, [char])) for char in cut]) for cut in cuts]
        # cuts_stroke = utils.get_all_list(cuts_stroke)
        # print(cuts_stroke)
        cuts_stroke = utils.get_stroke_replace(cuts, self.gram, self.same_stroke_dict, self.same_stroke_head)
        cuts_stroke = utils.get_all_list(cuts_stroke)

        query_pinyin, query_start_pinyin, query_pinyin_list = "", "", []
        for cut in cuts:
            qp = utils.get_pinyin(cut, mode="pinyin")
            query_pinyin_list.append(qp)
        #todo:多种召回无法结合：简拼，全拼，全拼转换，形近字
        #todo:目前只取一个，后面考虑怎样展示，多种可能的排列组合？
        res, second_res = self.max_backward_match_transform(query_pinyin_list, self.pinyin_di, max_k=10)
        jianpin_res = utils.max_backward_match(cuts, self.start_word_di, max_k=1)
        stroke_res = [utils.max_backward_match(elem, self.target_word, max_k=10) for elem in cuts_stroke]
        stroke_res = list(chain(*stroke_res))
        insider = []
        outsider = []
        for elem in res:
            original = "".join(cuts[elem[1]:elem[2]])
            pinyin = "".join(query_pinyin_list[elem[1]:elem[2]])
            candidates = []
            for word in self.pinyin_di.get(pinyin, []):
                transform_words = utils.get_all([[char, utils.get_pinyin(char, "pinyin")] for char in word])
                candidates.append([word, min([Levenshtein.distance(w, original) for w in transform_words]), elem[1], elem[2]])
            #candidates = [[word, min(Levenshtein.distance(word, original), Levenshtein.distance(pinyin, original)), elem[1], elem[2]] for word in self.pinyin_di.get(pinyin, [])]
            candidates = list(filter(lambda x: x[0] != "".join(cuts[x[2]: x[3]]), candidates))
            candidates = sorted(candidates, key=lambda x: x[1])
            # todo: 暂时取一个，实际上应该分析
            candidates = [candidates[0]] if len(candidates) > 0 else []
            # i = len(candidates)
            # if len(candidates) > 1:
            #     for ii in range(1, len(candidates)):
            #         if candidates[ii][1] > candidates[0][1]:
            #             i = ii
            #             break
            # candidates = candidates[:i]
            insider.extend(candidates)
        for elem in second_res:
            original = "".join(cuts[elem[1]:elem[2]])
            pinyin = elem[0]
            candidates = []
            for word in self.pinyin_di.get(pinyin, []):
                transform_words = utils.get_all([[char, utils.get_pinyin(char, "pinyin")] for char in word])
                candidates.append(
                    [word, min([Levenshtein.distance(w, original) for w in transform_words]), elem[1], elem[2]])
            #candidates = [[word, min(Levenshtein.distance(word, original), Levenshtein.distance(pinyin, original)), elem[1], elem[2]] for word in self.pinyin_di.get(pinyin, [])]
            candidates = list(filter(lambda x: x[0] != "".join(cuts[x[2]: x[3]]), candidates))
            candidates = sorted(candidates, key=lambda x: x[1])
            # todo: 暂时取一个，实际上应该分析
            candidates = [candidates[0]] if len(candidates) > 0 else []
            # i = len(candidates)
            # if len(candidates) > 1:
            #     for ii in range(1, len(candidates)):
            #         if candidates[ii][1] > candidates[0][1]:
            #             i = ii
            #             break
            # candidates = candidates[:i]
            outsider.extend(candidates)
        all_candidates = utils.check_conflict(insider, outsider)
        outsider = []
        for elem in jianpin_res:
            # todo: 暂时取一个，实际上应该分析
            outsider.append([list(self.start_word_di[elem[0]])[0], 0, elem[1], elem[2]])
        all_candidates= utils.check_conflict(all_candidates, outsider)

        outsider = []
        for elem in stroke_res:
            correct = elem[0]
            original = query[elem[1]:elem[2]]
            correct_pinyin = self.target_word[correct]
            original_pinyin = utils.get_pinyin(original, mode="pinyin")
            outsider.append([correct, Levenshtein.distance(correct, original) + Levenshtein.distance(correct_pinyin, original_pinyin), elem[1], elem[2]])

        all_candidates = utils.check_conflict(all_candidates, outsider)
        all_candidates = list(filter(lambda x: x[0] != "".join(cuts[x[2] : x[3]]), all_candidates))
        res = utils.get_correct(all_candidates, cuts)
        return res

































