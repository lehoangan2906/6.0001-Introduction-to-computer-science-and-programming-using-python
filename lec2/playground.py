n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
count = 1
while n == "right" or n == "Right":
    if count >= 2:
        n = input("You are in the Lost Forest\n****************\n******       ***\n  ( ˘︹˘ )\n****************\n****************\nGo left or right? ")
    else:
        n = input("You are in the Lost Forest\n****************\n******       ***\n  (╯°□°）╯︵ ┻━┻\n****************\n****************\nGo left or right? ")
    count += 1
print("\nYou got out of the Lost Forest!\n\o/")