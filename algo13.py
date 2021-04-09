ROMAN_NUM = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)


class Solution:
    def romanToInt(self, s: str) -> int:
        out_value = 0
        for symbol, n in ROMAN_NUM.items():
            out_value += s.count(symbol) * n
        if 'IV' in s:
            out_value -= 2
        if 'IX' in s:
            out_value -= 2
        if 'XL' in s:
            out_value -= 20
        if 'XC' in s:
            out_value -= 20
        if 'CD' in s:
            out_value -= 200
        if 'CM' in s:
            out_value -= 200
        return out_value