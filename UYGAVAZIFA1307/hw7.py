def find_max_key(d):
    max_key = max(d, key=d.get)
    print(f"Maksimal qiymatga ega bo'lgan kalit: {max_key}")
    return max_key
sample_dict = {
    'a': 10,
    'b': 20,
    'c': 15
}
find_max_key(sample_dict)
