import  array

LOW_LIMIT =60
HIGHT_LIMIT = 100

n= int(input("Enter the number of heart rate readings: "))
heart_rates = array.array('i',[])

for i in range(n):
    rate = int(input(f"Enter heart rate reading{i+1}: "))
    heart_rates.append(rate)
print("\nHeart rate analysis:")
print("Reading no.| Heart Rate | Status")
print("-"*30)

low_count = 0
normal_count = 0
hight_count = 0

for i in range(n):
    rate = heart_rates[i]

    if rate<LOW_LIMIT:
        status = "Low"
        low_count+=1
    elif rate>HIGHT_LIMIT:
        status = "Hight"
        hight_count+=1
    else:
        status = "Normal"
        normal_count+=1

    print(f"{i+1} | {rate} | {status}")

print("\nSummary:")
print(f"Total Readings: {n}" )
print(f"Low heart Rate Count: {low_count}")
print(f"Normal heart Rate Count: {normal_count}")
print(f"Hight heart Rate Count: {hight_count}")