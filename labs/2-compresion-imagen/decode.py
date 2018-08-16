import struct
from collections import OrderedDict
import bmp
import dct

IMG_SIZE   = 512
BLOCK_SIZE = 8

#litle-endian
U_SIZE_1 = '<b'
SIZE_1   = '<B'
SIZE_2   = '<H'
SIZE_4   = '<L'

def unpack_code(filename):
    def unpack(size, data, offset):
        return struct.unpack_from(size, data, offset)[0]

    codes = []
    dec_bmp = OrderedDict()
    with open(filename, 'rb') as f:
        data = bytearray(f.read())

        dec_bmp['signature']         = unpack(SIZE_2, data, 0)
        dec_bmp['bmp_file_size']     = unpack(SIZE_4, data, 2)
        dec_bmp['reserved_0']        = unpack(SIZE_2, data, 6)
        dec_bmp['reserved_1']        = unpack(SIZE_2, data, 8)
        dec_bmp['offset']            = unpack(SIZE_4, data, 10)
        dec_bmp['info_size']         = unpack(SIZE_4, data, 14)
        dec_bmp['img_width']         = unpack(SIZE_4, data, 18)
        dec_bmp['img_height']        = unpack(SIZE_4, data, 22)
        dec_bmp['num_planes']        = unpack(SIZE_2, data, 26)
        dec_bmp['bpp']               = unpack(SIZE_2, data, 28)
        dec_bmp['compression']       = unpack(SIZE_4, data, 30)
        dec_bmp['bmp_raw_file_size'] = unpack(SIZE_4, data, 34)
        dec_bmp['h_res']             = unpack(SIZE_4, data, 38)
        dec_bmp['v_res']             = unpack(SIZE_4, data, 42)
        dec_bmp['max_colors']        = unpack(SIZE_4, data, 46)
        dec_bmp['important_colors']  = unpack(SIZE_4, data, 50)
        dec_bmp['palette'] = []

        offset = dec_bmp['offset']
        code_size = unpack(SIZE_2, data, offset)

        tmp_code = list()
        for i in range(offset+2, offset+2+code_size):
            byte = unpack(U_SIZE_1, data, i)
            if byte == -128:
                codes.append(tmp_code)
                tmp_code = list()
            else:
                tmp_code.append(byte)
    return codes, dec_bmp


def decode(codes):
    tmp = []
    img_data = [[0]*IMG_SIZE for i in range(IMG_SIZE)]
    block_i = 0
    block_j = 0
    for c in codes:
        decoded_block = dct.decode(c)
        for i in range(BLOCK_SIZE):
            for j in range(BLOCK_SIZE):
                img_data[i+block_i][j+block_j] = decoded_block[i][j]
        block_j += BLOCK_SIZE
        if block_j >= IMG_SIZE:
            block_j = 0
            block_i += BLOCK_SIZE
    img_data_list = []
    for i in range(IMG_SIZE):
        for j in range(IMG_SIZE):
            img_data_list.append(img_data[i][j])
    return img_data_list


if __name__ == "__main__":
    codes, dec_bmp = unpack_code('lena.cbmp')
    data = decode(codes)
    bmp.save_bmp(dec_bmp, 'lena_dec.bmp', bmp_data = data)
