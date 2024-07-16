def print_max_value(dictionary):
    if not dictionary:
        print("Dictionary bo'sh")
        return
    max_value = max(dictionary.values())
    print("Maksimal qiymat:", max_value)
my_dict = {'a': 10, 'b': 20, 'c': 5}
print_max_value(my_dict)
