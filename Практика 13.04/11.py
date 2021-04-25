def fn():
    dictionary = {29:"двадцать девять", 3:"три", 7:"семь", 1:"один"}
    list_keys = list(dictionary.keys())
    list_keys.sort()
    for i in list_keys:
        print(i, ':', dictionary[i])
fn()