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
    for x in range(len(F)):
        for y in range(len(F[x])):
            F[x][y] = (F[x][y]*(127+128))/255-128
    return F


def shift_inv(F):
    for x in range(len(F)):
        for y in range(len(F[x])):
            F[x][y] = (F[x][y]+128)*(255)/(127+128)
    return F

########################################################################
def alfa(x):
    if(x == 0):
        return (1/float(8))**0.5;
    else:
        return (2/float(8))**0.5;

def sumatoryDct(N,M,u,v,F):
    sum = 0
    for x in range(N):
        for y in range(M):
            sum = sum +((alfa(u))*(alfa(v)*F[x][y] *(math.cos(((x+.5)*u*math.pi)/float(N))*math.cos(((y+.5)*v*math.pi)/float(M)))))
    return (sum)

def dct_encode(Fxy):
    matrizDCT = []
    for u in range(8):
        matrizDCT.append([])
        for v in range(8):
            matrizDCT[u].append(int_round(sumatoryDct(8,8,u,v,Fxy)))
    return matrizDCT

########################################################################

def constant(m):
    if(m!=0):
        return 1
    else:
        return (1/math.sqrt(2))

def sumatoryIdct(N,M,x,y,T):
    sum = 0
    for u in range(N):
        for v in range(M):
            sum = sum+(T[u][v] * (alfa(u)*alfa(v)* (math.cos(((x+.5)*u*math.pi)/float(N))* math.cos(((y+.5)*v*math.pi)/float(M)))))
    return sum

def dct_decode(Tuv):
    matriz_idct = [[]for o in range(8)]
    for x in range(8):
        for y in range(8):
            matriz_idct[x].append(int_round(sumatoryIdct(8,8,x,y,Tuv)))
    return matriz_idct

########################################################################
def quantize(T, Q):
    matrixQuantize = []
    for x in range(8):
        matrixQuantize.append([])
        for y in range(8):
            matrixQuantize[x].append(int_round(float(T[x][y])/float(Q[x][y])))
    return matrixQuantize

def dequantize(T, Q):
    for i in range(len(T)):
        for j in range(len(T)):
            T[i][j] = T[i][j]*Q[i][j]
    return T


########################################################################
def zig_zag(m):
    zigzag = []
    zigzag.append(m[0][0])
    for i in range(1,8):
        for g in range(i+1):
            if(i%2 == 1):
                zigzag.append(m[g][i-g])
            else:
                zigzag.append(m[i-g][g])
    cont = 0
    for i in reversed(range(1,8)):
        cont+=1
        contIv = 7
        for g in range(cont,8):
            if(i%2==1):
                zigzag.append(m[contIv][g])
            else:
                zigzag.append(m[g][contIv])
            contIv-=1
    return zigzag


def zig_zag_inv(l):
    zigzag = [[0 for x in range(int(math.sqrt(len(l))))]for i in range(int(math.sqrt(len(l))))]
    zigzag[0][0] = l[0]
    conr = 1
    for i in range(1,8):
        for g in range(i+1):
            if(i%2 == 1):
                zigzag[g][i-g] = l[conr]
            else:
                zigzag[i-g][g] = l[conr]
            conr+=1
    cont = 0
    for i in reversed(range(1,8)):
        cont+=1
        contIv = 7
        for g in range(cont,8):
            if(i%2==1):
                zigzag[contIv][g] = l[conr]
            else:
                zigzag[g][contIv] = l[conr]
            contIv-=1
            conr+=1
    return zigzag

########################################################################
def no_zeros(l):
    guard = '0'
    cont = 0
    while cont< len(l):
        if(l[cont] == 0 and guard == '0'):
            guard = cont
        elif(l[cont]== 0 and guard != '0' ):
            pass
        elif(l[cont]!=0 and guard != '0'):
            guard = '0'
        elif(l[cont]!= 0 and guard == '0'):
            pass
        cont+=1
    l = l[:guard]
    return l

def add_zeros(l):
    lista = [0 for i in range(64-len(l))]
    l = l+lista
    return l
  
########################################################################
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
