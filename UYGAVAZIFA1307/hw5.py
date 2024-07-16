from collections import Counter
def eng_kam_takrorlangan_qiymat(royxat):
    sanash = Counter(royxat)
    
    eng_kam_son = min(sanash.values())
    
    eng_kam_takrorlangan_qiymatlar = [key for key, value in sanash.items() if value == eng_kam_son]
    return (eng_kam_takrorlangan_qiymatlar[0], eng_kam_son)
royxat = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
natija = eng_kam_takrorlangan_qiymat(royxat)
print(f"Eng kam takrorlangan qiymat: {natija[0]}, Takrorlanish soni: {natija[1]}")
