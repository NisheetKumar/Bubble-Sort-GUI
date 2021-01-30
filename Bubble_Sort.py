n_list = [1,5,7,9,4,6,2,1]


print("\nOriginal list",n_list)
for i in range(len(n_list)):
    for j in range(len(n_list)-i-1):
        if n_list[j] > n_list[j+1]:
            n_list[j],n_list[j+1] = n_list[j+1], n_list[j]

print("sort list\n",n_list)