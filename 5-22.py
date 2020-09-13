n = int(input("a: "))
s = int(input("b: "))
for num in range(n, s +1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
                