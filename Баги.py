flag = True
for i in range(10):
    n = int(input())
    if n % 2 == 0:
        flag = flag
    else:
        flag = False
if flag == True:
    print("Yes")
else:
    print("No")
