from collections import Counter

def eng_kop_takrorlangan_qiymat(royxat):
    sanash = Counter(royxat)
    eng_kop_qiymat, takrorlanish_soni = sanash.most_common(1)[0]
    return (eng_kop_qiymat, takrorlanish_soni)
royxat = [1, 3, 2, 1, 4, 1, 3, 2, 1, 3, 3]
natija = eng_kop_takrorlangan_qiymat(royxat)
print(natija) 