def ikkinchi_maksimal(lst):
    birinchi_max = float('-inf')  
    ikkinchi_max = float('-inf')  
    for son in lst:
        if son > birinchi_max:
            ikkinchi_max = birinchi_max
            birinchi_max = son
        elif birinchi_max > son > ikkinchi_max:
            ikkinchi_max = son
    return ikkinchi_max
lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(ikkinchi_maksimal(lst))
