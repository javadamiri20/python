num_list = [2,2314,23,24,32,1234,45,5463,634,63,25,56,65,5775,9,3]
num_list2 = []
num = 0

for i in range(len(num_list)):
    if num_list[i] % 2 == 0:
        num_list2.append(num_list[i])
    else:
        num += num_list[i]

print(num_list2)
print(num)



