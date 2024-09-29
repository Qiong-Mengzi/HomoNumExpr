'''
# Yumeko的恶臭数字论证器

Homo无处不在(x)

注意：这个东西大概率给不出最简答案（因为我笨蛋）
'''

import json
from copy import deepcopy
from io import TextIOWrapper
import re

class HomoNumberExpr(object):
    OP_SIGN = ('+', '-', '*')
    def __init__(self, homoNumCursed: str = '114514', auto_calc: bool = True, table_load_fp: TextIOWrapper | None = None):
        self.homoNumCursed = homoNumCursed
        self.auto_calc = auto_calc
        self.baseOpResultTable: dict[int, str] = {}
        self._num_key_cache_sorted: list[tuple[int, str]] = []

        if table_load_fp != None:
            self.baseOpResultTable = {int(k):v for k,v in json.load(table_load_fp).items()}
            self._num_key_cache_sorted = sorted(self.baseOpResultTable.items(), key=lambda item: item[0])

        if auto_calc and table_load_fp == None:
            self._coverOpResultTable()
        pass

    def SaveHomoCalcTable(self, table_save_fp: TextIOWrapper):
        json.dump(self.baseOpResultTable, table_save_fp)

    def SetHomoNum(self, homo_num: str = '114514'):
        self.homoNumCursed = homo_num
        if self.auto_calc:
            self._coverOpResultTable()
    
    def UpdateHomoCalcTable(self):
        self._coverOpResultTable()

    def _coverOpResultTable(self):
        expr_table: list[str] = []
        for expr_arg in self._SplitAllSubStr(self.homoNumCursed):
            expr_table += self._AddSign(expr_arg)
        for expr_text in expr_table:
            result = self._CalcExpr(expr_text)
            if result not in self.baseOpResultTable:
                self.baseOpResultTable[result] = expr_text
            elif len(self.baseOpResultTable[result]) > len(expr_text):
                self.baseOpResultTable[result] = expr_text
            else:
                pass
        #self._NegTable()
        self._num_key_cache_sorted = sorted(self.baseOpResultTable.items(), key=lambda item: item[0])
        pass
        
    @staticmethod
    def _SplitAllSubStr(s: str):
        def backtrack(start: int, path: tuple[str, ...]):
            if start == len(s):
                result.append(path)
            else:
                for end in range(start + 1, len(s) + 1):
                    if s[start:end] != '':
                        backtrack(end, (s[start:end],) + path)

        result: list[tuple[str, ...]] = []
        backtrack(0, ())
        return [(t :=list(_), t.reverse(), t)[-1] for _ in result]
    
    @staticmethod
    def _AddSign(expr_arg: list[str]):
        def part(i: int, s: list[str]):
            if i == 0:
                result.append(''.join(s))
                result.append('-' + ''.join(s))
            else:
                _ = deepcopy(s)
                _[-i] = '+' + _[-i]
                part(i - 1, _)
                _ = deepcopy(s)
                _[-i] = '-' + _[-i]
                part(i - 1, _)
                _ = deepcopy(s)
                _[-i] = '*' + _[-i]
                part(i - 1, _)

        result: list[str] = []
        part(len(expr_arg) - 1, expr_arg)
        return result

    @staticmethod
    def _CalcExpr(expr_text: str):
        args: list[int] = [int(_) for _ in expr_text.replace('-', ' ').replace('+', ' ').replace('*', ' ').split()]
        op: list[str] = re.split(r'\d+', expr_text)
        op = [_ for _ in op if _]

        if len(op) == len(args):
            if op[0] == '+':
                val_stack: list[int] = [args[0]]
            else:
                val_stack: list[int] = [-args[0]]
            op = op[1:]
        else:
            val_stack: list[int] = [args[0]]
        op_stack: list[str] = []
        # 乘法运算
        for i in range(len(op)):
            if(op[i] == '*'):
                v = val_stack.pop()
                val_stack.append(v * args[i + 1])
            else:
                val_stack.append(args[i + 1])
                op_stack.append(op[i])
        # 加减法运算
        result = val_stack[0]
        for i in range(len(op_stack)):
            if op_stack[i] == '+':
                result += val_stack[i + 1]
            else:
                result -= val_stack[i + 1]

        return result
    
    def _NegTable(self):
        neg_table = {(-k) : '-' + ''.join([_ if _ not in ('+', '-') else ('-' if _ == '+' else '-') for _ in v]) for k, v in self.baseOpResultTable.items()}
        self.baseOpResultTable.update(neg_table)

    def Homo(self, _num: str):
        num = int(_num)

        if num in self.baseOpResultTable:
            return self.baseOpResultTable[num]
        
        result: str = ''
        while num > int(self.homoNumCursed):
            if result != '':
                result += '+'
            result += self.homoNumCursed
            num -= int(self.homoNumCursed)
        while num < -int(self.homoNumCursed):
            result += '-' + self.homoNumCursed
            num += int(self.homoNumCursed)
        while num != 0:
            c, s = self._num_key_cache_sorted[self._FindMinCost(num)]
            num -= c
            if s[0] != '-' and result != '':
                result += '+'
            result += s
        return result
        
    def _FindMinCost(self, num: int):
        # 我希望有更好的算法，可惜我是笨蛋喵
        min_cost: int = int(self.homoNumCursed)
        min_index = -1
        for i in range(len(self._num_key_cache_sorted)):
            if abs(num - self._num_key_cache_sorted[i][0]) < min_cost:
                min_cost = abs(num - self._num_key_cache_sorted[i][0])
                min_index = i
        return min_index
    
    def calcHomoNum(self):
        if len(self._num_key_cache_sorted):
            self.homoNumCursed = self._num_key_cache_sorted[-1][-1]
        return self.homoNumCursed

if __name__ == '__main__':
    Homo = HomoNumberExpr('114514')
    #with open('1919810CacheTable.json', 'w') as f:
    #    Homo.SaveHomoCalcTable(f)
    print('恶臭数字论证器')
    print('一个简易的实现喵~输入exit退出喵~')
    while True:
        i = input('Homo > ')
        if i == 'exit':
            break
        print(Homo.Homo(i))

__all__ = ['HomoNumberExpr']
