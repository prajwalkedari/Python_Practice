n = int(input("Enter Number: "))
sum=0
for i in  range(n+1):
    sum+=i

sum1 = 0
i=0
while i<=n:
    sum1+=i
    i+=1
print(f"Sum of {n} is {sum} (with For Loop)")
print(f"Sum of {n} is {sum1} (with while Loop)")

