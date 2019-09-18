def seperator(list):
    odd = []
    even = []
    for i in range(len(list)):
        if list[i] % 2 == 0:
            even.append(list[i])
        else:
            odd.append(list[i])
    return odd, even


li = [1, 123, 2, 3, 4, 5, 6, 4, 2, 231, 223, 121]
odd, even = seperator(li)
print(odd)
print(even)
