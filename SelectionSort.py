num = [5, 3, 8, 6, 7, 2]

def sort(num):
    for i in range(5):
        min = i
        for j in range(i, 6):
            if num[j] < num[min]:
                min = j

        num[i], num[min] = num[min], num[i]
        print(num)
print(num)

sort(num)

print(num)
