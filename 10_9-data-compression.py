import zlib
s = b'witch witch has witch witches wrist watch'
print(len(s))

t = zlib.compress(s)
print(len(t))

print(zlib.decompress(t))
print(zlib.crc32(s))

