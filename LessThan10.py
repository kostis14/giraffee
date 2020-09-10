a = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
abc = []

for index in range(len(a)):
    if a[index] < 5:
        abc.append(a[index])


def numsygkrish(number):
    for index in range(len(a)):
        if a[index] < number:
            print(a[index])


number = int(input("Give me a number:"))
numsygkrish(number)
