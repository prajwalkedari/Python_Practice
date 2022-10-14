n=int(input("Enter Number: ")) #declare N= 5 / let Input = 15
for i in range(1,n+1): # let i =1,2......14,15
    if i in [1,n]:     #only for (1 & last) full 15 star
        print("* "*n)
    else:
        print("* "+ str("  "*(n-2)) + "*") #else " "(space) (n-2)=13 mean (*<----13---->*)
