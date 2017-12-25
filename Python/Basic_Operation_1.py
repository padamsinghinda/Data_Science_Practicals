print("Numbers between 2000 and 3200 (both included) - divisible by 7 and not a multiple of 5 : \n")
for i in range(2000,3201):
    if i%7 == 0 and i%5 != 0 :
        print(i)