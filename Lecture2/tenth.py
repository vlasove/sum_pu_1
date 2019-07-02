stations = {501:['Lyublino','Vikhino','Hovrino','Kotelniki','Vidnoe'], 502:['Hovrino','Maimi','Verknie Pupki','Vikhino']}

city = "Lyublino"

for k in stations.keys():
    if city in stations[k]:
        if city != stations[k][-1]:
            print(k)




