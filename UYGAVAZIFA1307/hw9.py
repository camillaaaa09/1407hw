def invert_dict(d):
    inverted_dict = {}
    for key, value in d.items():
        inverted_dict[value] = key
    return inverted_dict
sample_dict = {'a': 1, 'b': 2, 'c': 3}
inverted_sample = invert_dict(sample_dict)
print(inverted_sample)
