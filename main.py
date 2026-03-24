print("hello world")
print("hey")

for i in range(1,501):
    count = 0
    q = i
    rem = 0
    mul = 0
    result = 0

    while q != 0:
        q = q // 10
        count +=1

    q = i

    while q!=0:
        rem = q % 10
        mul = rem ** count
        result = result + mul
        q = q // 10

    if result == i:
        print(f"{i} Is Armstrong")
    else:
        print(f"{i} is Not Armstrong")