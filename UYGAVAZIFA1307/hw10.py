def lugatnikalitdanochirish(d, kalit):
    if kalit in d:
        del d[kalit]
    return d
misollugat = {'a': 1, 'b': 2, 'c': 3}
ociriladigankalit = 'b'
yangilugat = lugatnikalitdanochirish(misollugat, ociriladigankalit)
print(yangilugat)
