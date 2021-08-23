# 1. Strings
#   what is the value of the variable u in the code below ?
once = "umbr"
repeat = "ella"
u = once + (repeat +" ")*4

# 2. Comparisions
#   what does the code below print?
pset_time = 15
sleep_time = 8
print(sleep_time > pset_time)
derive = True
drink = False
both = drink and derive
print(both)

# 3. branching
#   what's printed when x = 0 and y = 5
x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
if x == y:
    if y != 0:
        print("x / y is", x/y)
elif x < y:
    print("x is smaller")
else:
    print("y is smaller")

# 4. while loops
#   in the code below from Lecture 2, what is printed when you type "Right"?
n = input("You're in the Lost Forest. Go left or right? ")
while n == "right":
    n = input("You're in the Lost Forest. Go left or right? ")
print("You got out of the Lost Forest!")

# 5. For loops
#   What is printed when the code below is run?
mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
        break
        mysum += 1
print(mysum)