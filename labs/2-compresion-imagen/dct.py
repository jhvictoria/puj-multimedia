#Juan Fernando Escobar

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
    tmp=F[:]
    for e in range(N):
        for ee in range(M):
            F[e][ee]-=128
    return tmp


def shift_inv(F):
    tmp=F[:]
    for e in range(N):
        for ee in range(M):
            F[e][ee]+=128
    return tmp

def alpha(x):
    if x==0:
        return math.sqrt(1/8)
    else:
        return math.sqrt(2/8)


def dct_encode(Fxy):
    salida= [ [ 0 for e in range(M) ] for ee in range(N) ]
    for u in range(N):
        for v in range(M):
            for x in range(N):
                for y in range(M):
                    salida[u][v]+=Fxy[x][y]*alpha(u)*alpha(v)*math.cos(((2*x+1)*u*math.pi)/(2*N))*math.cos(((2*y+1)*v*math.pi)/(2*M))
            salida[u][v]=int_round(salida[u][v])
    return salida


def dct_decode(Tuv):
    salida= [ [ 0 for e in range(M) ] for ee in range(N) ]
    for x in range(N):
        for y in range(M):
            for u in range(N):
                for v in range(M):
                    salida[x][y]+=Tuv[u][v]*alpha(u)*alpha(v)*math.cos(((2*x+1)*u*math.pi)/(2*N))*math.cos(((2*y+1)*v*math.pi)/(2*M))
            salida[x][y]=int_round(salida[x][y])
    return salida


def quantize(T, Q):
    for u in range(N):
        for v in range(M):
            T[u][v]=int_round(T[u][v]/Q[u][v])
    return T


def dequantize(T, Q):
    for u in range(N):
        for v in range(M):
            T[u][v]=T[u][v]*Q[u][v]
    return T


def zig_zag(m):
    sube=True
    half=True
    i=0
    salida=[ None for e in range(M*N) ]
    x=0
    y=0
    while x!=N-1 or y!=M-1:
        salida[i]=m[x][y]
        i+=1
        if half:
            if x==0 and sube:
                y+=1
                sube=False
            elif y==0 and not(sube):
                x+=1
                sube=True
            elif sube==True:
                x-=1
                y+=1
            else:
                x+=1
                y-=1
            if x==7:
                salida[i]=m[x][y]
                sube=True
                i+=1
                half=False
                x=N-1
                y=1
        else:
            if x==N-1 and not(sube):
                y+=1
                sube=True
            elif y==M-1 and sube:
                x+=1
                sube=False
            elif sube==True:
                x-=1
                y+=1
            else:
                x+=1
                y-=1
    salida[i]=m[x][y]
    return salida


def zig_zag_inv(l):
    sube=True
    half=True
    i=0
    salida=[ [ None for e in range(M) ] for ee in range(N) ]
    x=0
    y=0
    while x!=N-1 or y!=M-1:
        salida[x][y]=l[i]
        i+=1
        if half:
            if x==0 and sube:
                y+=1
                sube=False
            elif y==0 and not(sube):
                x+=1
                sube=True
            elif sube==True:
                x-=1
                y+=1
            else:
                x+=1
                y-=1
            if x==7:
                salida[x][y]=l[i]
                sube=True
                i+=1
                half=False
                x=N-1
                y=1
        else:
            if x==N-1 and not(sube):
                y+=1
                sube=True
            elif y==M-1 and sube:
                x+=1
                sube=False
            elif sube==True:
                x-=1
                y+=1
            else:
                x+=1
                y-=1
    salida[x][y]=l[i]
    return salida

def no_zeros(l):
    lenght=len(l)-1
    flag=False
    while(lenght>=0 and not(flag)):
        if l[lenght]==0:
            lenght-=1
        else:
            flag=True
    l=l[:lenght+1]
    return l


def add_zeros(l):
    length=len(l)
    while length<M*N:
        l.append(0)
        length+=1
    return l

  

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
    do_print("quantize:\n", Quv)

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
