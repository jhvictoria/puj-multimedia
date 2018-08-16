import struct
import bmp
import dct

IMG_SIZE   = 512
BLOCK_SIZE = 8

#litle-endian
U_SIZE_1 = '<b'
SIZE_1   = '<B'
SIZE_2   = '<H'
SIZE_4   = '<L'

def get_block(start_x, start_y, data):
    block = [[0]*BLOCK_SIZE for i in range(BLOCK_SIZE)]
    pos = (start_x*IMG_SIZE) + start_y
    for i in range(BLOCK_SIZE):
        n_pos = pos
        for j in range(BLOCK_SIZE):
            block[i][j] = data[n_pos]
            n_pos += 1
        pos += IMG_SIZE
    return block


def pack_code(filename, bmp_data, codes):
    def pack(size, data, offset, value):
        struct.pack_into(size, data, offset, value)

    #headers + palette + total_coding + data              
    encoding_byte_length = 54 + 4*256 + 2 + len(codes)

    with open(filename, 'wb') as f:
        data = bytearray(encoding_byte_length)
        pack(SIZE_2, data, 0, dec_bmp['signature'])
        pack(SIZE_4, data, 2, dec_bmp['bmp_file_size'])
        pack(SIZE_2, data, 6, dec_bmp['reserved_0'])
        pack(SIZE_2, data, 8, dec_bmp['reserved_1'])
        pack(SIZE_4, data, 10, dec_bmp['offset'])
        pack(SIZE_4, data, 14, dec_bmp['info_size'])
        pack(SIZE_4, data, 18, dec_bmp['img_width'])
        pack(SIZE_4, data, 22, dec_bmp['img_height'])
        pack(SIZE_2, data, 26, dec_bmp['num_planes'])
        pack(SIZE_2, data, 28, dec_bmp['bpp'])
        pack(SIZE_4, data, 30, dec_bmp['compression'])
        pack(SIZE_4, data, 34, dec_bmp['bmp_raw_file_size'])
        pack(SIZE_4, data, 38, dec_bmp['h_res'])
        pack(SIZE_4, data, 42, dec_bmp['v_res'])
        pack(SIZE_4, data, 46, dec_bmp['max_colors'])
        pack(SIZE_4, data, 50, dec_bmp['important_colors'])

        bmp_palette = bmp.get_palette()
        for i in range(len(bmp_palette)):
            pack(SIZE_1, data, 54+i, bmp_palette[i])

        offset = dec_bmp['offset']
        pack(SIZE_2, data, offset, len(codes))

        for i in range(len(codes)):
            tmp_offset = offset + 2 + i
            pack(U_SIZE_1, data, tmp_offset, codes[i])
        f.write(data)


def encode(bmp_data):
    codes = []
    for i in range(0, IMG_SIZE, BLOCK_SIZE):
        for j in range(0, IMG_SIZE, BLOCK_SIZE):
            block_tmp = get_block(i, j, bmp_data)
            block_encoded = dct.encode(block_tmp) + [-128]
            codes += block_encoded
    return codes


if __name__ == "__main__":
    dec_bmp = bmp.read_bmp('lena.bmp')
    bmp_data = dec_bmp['bmp_data']
    codes = encode(bmp_data)
    pack_code('lena.cbmp', bmp_data, codes)
