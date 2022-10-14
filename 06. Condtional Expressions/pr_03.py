mail = " Hey User, We Have Best Offer You  .Buy now our Python Couser click me to  proccesd"
SpamContain = ["buy now","make a lot of money","click me", "subscribe  this"]
if  "Buy now" in mail  :
    print("This Spam")

# Other way (Not Begginer)(only For Loop)

print("\n\nanother Way with For Loop \n")
spam = False
for i in SpamContain:
    if i in mail:
        spam = True
else: 
    spam = False

if spam:
    print("This spam")
else:
    print("This not spam")

num = int(input("Enter the number"))
def table(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")

table(num)
