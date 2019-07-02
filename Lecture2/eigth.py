ex_dict = {"one":1, "two":2, "five": 10, "three":3,"four":4}


keys_list = []
for k in ex_dict.keys():
    keys_list.append(k)
keys_list.sort()


for new_k in keys_list:
    print(new_k,ex_dict[new_k])