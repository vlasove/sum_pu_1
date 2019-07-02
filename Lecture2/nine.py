new_dict = {}

with open("kek.txt","r") as f:
    for line in f:
        new_str = line.lower()
        new_list = new_str.split()

        for name in new_list:
            if name in new_dict.keys():
                new_dict[name] +=1
            else:
                new_dict[name] = 1

print(new_dict)


    