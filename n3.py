j = [12,3,4,5,6]
for i in j:
    if i > 3:
        j.remove(i)
        print(j)
        continue
    if i < 2:
        j.append(i)
        print(j)
