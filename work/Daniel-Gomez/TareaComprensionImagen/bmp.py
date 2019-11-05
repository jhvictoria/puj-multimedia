import struct
from collections import OrderedDict

#litle-endian
SIZE_1 = '<B'
SIZE_2 = '<H'
SIZE_4 = '<L'

def read_bmp(filename):
    def unpack(size, data, offset):
        try:
            return struct.unpack_from(size, data, offset)[0]
        except:
            print(size, offset)
            raise

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
        for i in range(54, dec_bmp['offset']):
            dec_bmp['palette'].append(unpack(SIZE_1, data, i))
        
        offset   = dec_bmp['offset']
        width    = dec_bmp['img_width']
        height   = dec_bmp['img_height']

        dec_bmp['bmp_data'] = []
        for i in range(offset, offset+(width*height)):
            dec_bmp['bmp_data'].append(unpack(SIZE_1, data, i))
    return dec_bmp


def get_palette():
    palette = []
    for i in range(256):
        palette += [i,i,i,0]
    return palette


def save_bmp(dec_bmp, filename, bmp_data=None):
    def clamp(minimum, x, maximum):
        return max(minimum, min(x, maximum))

    def pack(size, data, offset, value):
            try:
                struct.pack_into(size, data, offset, value)
            except:
                print(size, offset, value)
                raise

    with open(filename, 'wb') as f:
        data = bytearray(dec_bmp['bmp_file_size'])
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

        bmp_palette = get_palette() if dec_bmp['palette'] == [] else dec_bmp['palette']
        for i in range(len(bmp_palette)):
            pack(SIZE_1, data, 54+i, bmp_palette[i])

        offset   = dec_bmp['offset']
        bmp_data = dec_bmp['bmp_data'] if bmp_data == None else bmp_data
        for i in range(len(bmp_data)):
            tmp_offset = offset + i
            value = clamp(0, bmp_data[i], 255)
            pack(SIZE_1, data, tmp_offset, value)
        f.write(data)

def print_decoded_bpm(dec_bmp):
    lenght = dec_bmp['img_width'] * dec_bmp['img_height']
    for k,v in dec_bmp.items():
        if k in ['bmp_data','palette']:
            if lenght > 5:
                print("%s:"%k, v[0:5] + ['...'])
                continue
        print("%s:"%k, v)

if __name__ == "__main__":
    import random
    bmp_data = []
    for i in range(512*512):
        bmp_data.append(random.randint(0,255)) 

    dec_bmp_1 = read_bmp('lena.bmp')
    print_decoded_bpm(dec_bmp_1)
    save_bmp(dec_bmp_1, 'lena2.bmp')

    dec_bmp_2 = read_bmp('lena2.bmp')
    #print_decoded_bpm(dec_bmp_2)

    print(dec_bmp_1 == dec_bmp_2)
