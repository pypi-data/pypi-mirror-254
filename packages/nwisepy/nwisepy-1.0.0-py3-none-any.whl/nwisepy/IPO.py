import random
from itertools import combinations, product


class Item:
    """
    An encapsulated data structure that stores each value of each parameter and the index
    of the parameter column in which it resides
    """
    @property
    def id(self):
        return self.__item_id

    @property
    def value(self):
        return self.__value

    def __init__(self, item_id, value):
        self.__item_id = item_id
        self.__value = value

    def __str__(self):
        return f"{self.id}: {self.value}"

    def __eq__(self, other):
        if isinstance(other, Item):
            return self.id == other.id and self.value == other.value
        else:
            return False

    def __hash__(self):
        return hash((self.__item_id, self.__value))

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index >= len(self):
            raise StopIteration
        else:
            item = self.get_item(self.__index)
            self.__index += 1
            return item

    def get_item(self, index):
        if index == 0:
            return self
        else:
            raise IndexError("Item index out of range")

    def __len__(self):
        return 1


class Pairwise:
    """
    A class aims to generate a n-wise testing set using in-parameter-order (IPO) algorithm
    """
    def __init__(self, parameters, n=2):
        self._n = n
        self.param = parameters
        self._length = len(parameters)
        self.__validate_param(self.param)
        self.__item_matrix = self.__get_item_matrix(parameters)
        self.__item_result_list = self.__init_res_list()
        self.__result_list = None
        self.__v_set = set()

    def __validate_param(self, parameter):
        if isinstance(parameter, list):
            if len(parameter) < 2:
                raise ValueError("Length of parameter list should be at least two!")
            if self._n > self._length:
                raise ValueError("Length of parameter list should be less than n!")
            for p in parameter:
                if not p:
                    raise ValueError("Each parameter arrays must have at least one item")
        else:
            raise TypeError("You've input a invalid parameter type! Must be a list.")

    def __get_item_matrix(self, parameter_matrix):
        return [
            [
                Item(param_idx, value)
                for _, value in enumerate(value_list)
            ]
            for param_idx, value_list in enumerate(parameter_matrix)
        ]

    def __init_res_list(self):
        return list(product(*self.__item_matrix[:self._n]))

    def result(self):
        if self._length > self._n:
            self.__find_pairwise()
        self.__convert_to_res(self.__item_result_list)

        return self.__result_list

    def __find_pairwise(self):
        for i in range(self._n, self._length, 1):
            extend_waiting_pairs = set()
            l = len(self.__item_matrix[i])
            idx_l = list(combinations([j for j in range(i)], self._n-1))
            for j in idx_l:
                for h in list(product(*[self.__item_matrix[k] for k in j], self.__item_matrix[i])):
                    extend_waiting_pairs.add(h)
            self.__ipo_h_iv(extend_waiting_pairs, l, i)
            if len(extend_waiting_pairs):
                self.__ipo_v(extend_waiting_pairs)
                rm_lst = set()
                for v in self.__v_set:
                    if None not in v[:i+1]:
                        self.__item_result_list.append(v[:i+1])
                        rm_lst.add(v)
                for r in rm_lst:
                    self.__v_set.remove(r)
        for f in self.__v_set:
            self.__item_result_list.append(tuple(f))

    def __convert_to_res(self, item_list: [[]]):
        self.__result_list = [[item.value if item is not None else self.param[idx][random.randint(0, len(self.param[idx])-1)]
                               for idx, item in enumerate(pair)] for pair in item_list]

    def __ipo_h_iv(self, extend, l, i):
        len_i = len(self.__item_result_list)
        num = min(l, len_i)
        for j in range(num):
            self.__item_result_list[j] += tuple(self.__item_matrix[i][j])
            extend -= set(combinations(self.__item_result_list[j], self._n))
        if num == len(self.__item_result_list):
            return
        for j in range(num, len_i):
            pi = set()
            select = None
            for item in self.__item_matrix[i]:
                temp = self.__item_result_list[j] + tuple(item)
                pi_1 = set(combinations(temp, self._n))
                pi_2 = pi_1 & extend
                if len(pi_2) >= len(pi):
                    pi, select = pi_2, item
            self.__item_result_list[j] += tuple(select)
            extend -= pi

    def __ipo_v(self, extend):
        flag = 0
        for pair in extend:
            temp = [None] * len(self.param)
            for item in pair:
                temp[item.id] = item
            for i in self.__v_set:
                sub_flag = 1
                for j in pair:
                    if i[j.id] is not None and i[j.id] != j:
                        sub_flag = 0
                        break
                if sub_flag:
                    flag = 1
                    t = list(i)
                    self.__v_set.remove(i)
                    for k in pair:
                        t[k.id] = k
                    self.__v_set.add(tuple(t))
                    break
            if not flag:
                self.__v_set.add(tuple(temp))
            flag = 0
