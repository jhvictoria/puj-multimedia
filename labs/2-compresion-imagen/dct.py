# -*- coding: cp1252 -*-
import math
import sys
import decimal
from decimal import Decimal

#Block size
N = 8
M = 8

#Q-Matrix
Q = [[16,11,10,16,24, 40, 51, 61],
     [12,12,14,19,26, 58, 60, 55],
     [14,13,16,24,40, 57, 69, 56],
     [14,17,22,29,51, 87, 80, 62],
     [18,22,37,56,68, 109,103,77],
     [24,35,55,64,81, 104,113,92],
     [49,64,78,87,103,121,120,101],
     [72,92,95,98,112,100,103,99]]


def do_print(msg, e, s_type='M'):
    print(msg)
    if not e:
        pass
    elif s_type in ['E','L']:
        print(e)
    elif s_type == 'M':
        for i in e:
            print(i)
    print()


def int_round(n):
    return int(Decimal(n).quantize(Decimal('1'), rounding=decimal.ROUND_HALF_UP))


def encode(m):
    Shift_Fxy = shift(m)
    Tuv = dct_encode(Shift_Fxy)
    Quv = quantize(Tuv,Q)
    ZZ_uv = zig_zag(Quv)
    NZ_uv = no_zeros(ZZ_uv)
    return NZ_uv


def decode(l):
    ZZ_uv = add_zeros(l)
    Quv = zig_zag_inv(ZZ_uv)
    Tuv = dequantize(Quv,Q)
    Shift_Fxy = dct_decode(Tuv)
    Fxy = shift_inv(Shift_Fxy)
    return Fxy


def shift(F):
    pass


def shift_inv(F):
    pass


def dct_encode(Fxy):
    pass


def dct_decode(Tuv):
    pass


def quantize(T, Q):
    pass


def dequantize(T, Q):
    pass


def zig_zag(m):
    pass


def zig_zag_inv(l):
    pass


def no_zeros(l):
    pass


def add_zeros(l):
    pass

  

def main():
    #Bloque original
    Fxy = \
    [
        [52,55,61,66, 70, 61, 64,73],
        [63,59,55,90, 109,85, 69,72],
        [62,59,68,113,144,104,66,73],
        [63,58,71,122,154,106,70,69],
        [67,61,68,104,126,88, 68,70],
        [79,65,60,70, 77, 68, 58,75],
        [85,71,64,59, 55, 61, 65,83],
        [87,79,69,68, 65, 76, 78,94]
    ]

    print("Code\n")

    do_print("image:", Fxy)

    Shift_Fxy = shift(Fxy)
    do_print("shift:", Shift_Fxy)

    Tuv = dct_encode(Shift_Fxy)
    do_print("dct:\n", Tuv)

    Quv = quantize(Tuv,Q)
    do_print("quantize:\n", Tuv)

    ZZ_uv = zig_zag(Quv)
    do_print("zig-zag scan:\n", ZZ_uv, s_type='L')

    NZ_uv = no_zeros(ZZ_uv)
    do_print("remove zeros:\n", NZ_uv, s_type='L')

    #inverse process
    print("\n\nDecode\n")

    ZZ_uv = add_zeros(NZ_uv)
    do_print("add zeros:\n", ZZ_uv, s_type='L')

    Quv = zig_zag_inv(ZZ_uv)
    do_print("Quantized:\n", Quv)

    Tuv = dequantize(Quv,Q)
    do_print("Dequantized:\n", Tuv)

    Shift_Fxy = dct_decode(Tuv)
    do_print("idct:\n", Shift_Fxy)

    Fxy_decoded = shift_inv(Shift_Fxy)
    do_print("Shift inv - image:\n", Fxy_decoded)

    expected_decoded = \
        [
            [60, 63, 55, 58, 70, 61, 58, 80],
            [58, 56, 56, 83, 108, 88, 63, 71],
            [60, 52, 62, 113, 150, 116, 70, 67],
            [66, 56, 68, 122, 156, 116, 69, 72],
            [69, 62, 65, 100, 120, 86, 59, 76],
            [68, 68, 61, 68, 78, 60, 53, 78],
            [74, 82, 67, 54, 63, 64, 65, 83],
            [83, 96, 77, 56, 70, 83, 83, 89]
        ]
    print("\nis decode ok?:", Fxy_decoded == expected_decoded)


if __name__ == "__main__":
    main()
