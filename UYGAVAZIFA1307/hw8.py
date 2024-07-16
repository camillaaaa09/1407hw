def dictionary_to_set(d):
    result_set = set()
    for key, value in d.items():
        result_set.add(key)
        result_set.add(value)
    return result_set
my_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}
result = dictionary_to_set(my_dict)
print(result)
