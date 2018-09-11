a. Para qué se utiliza el módulo struct en Python
	Como se esta trabajando con datos empaquetados con descripciones compactas, se usa para realizar las conversiones.

b. Qué hacen los scripts bmp.py, decode.py, encode.py. Para esto, explique cada función implementada
	
	el inicio en 'encode(m)' se realiza el complemento a dos, primer paso que se realiza con el bloque de 8x8
	en la compresion JPEG. Despues se aplica DCT que convierte los datos intensidad y con esto se puede mirar
	que tan rapido vairan las intensidades en el bloque. despues de esto se realiza.

https://asecuritysite.com/comms/dct2


	def encode(m):
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
