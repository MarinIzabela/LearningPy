row = 15

for i in range(1 , row+1):
    for j in range(i):
        print("*", end = " ")
    print()
print("\n")
for i in range(row , 0 , -2):
    for j in range(i):
        print("*", end = " ")
    print()