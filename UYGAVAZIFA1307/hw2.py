def ikkinchi_minimal(lst):
    birinchi_min = float('inf')
    ikkinchi_min = float('inf')
    for son in lst:
        if son < birinchi_min:
            ikkinchi_min = birinchi_min
            birinchi_min = son
        elif birinchi_min < son < ikkinchi_min:
            ikkinchi_min = son
    return ikkinchi_min

lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(ikkinchi_minimal(lst))
