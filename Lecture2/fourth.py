example_string = "lol kek cheburekk"

symbol_max =""
count_max = 0

for i in example_string:
    counter = 0
    for j in example_string:
        #print(i,j)
        
        if i == j:
            counter+=1
            

    if counter > count_max:
        count_max = counter
        symbol_max = i


print(example_string.count("l"))




    

