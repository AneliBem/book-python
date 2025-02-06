import struct
from dataclasses import field
from fileinput import filename
from zipfile import crc32

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):
    start += 14
    filename = struct.unpack('<IIIHH', data[start:start + 16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = filename

    start += 16
    filename = data[start:start + filenamesize]
    start += filenamesize
    extra = data[start:start + extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size