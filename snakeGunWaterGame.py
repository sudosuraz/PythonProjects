import random

print("this is snake gun water game")
cTurn = random.randint(1, 3)
if cTurn == 1:
    c = 's'
elif cTurn == 2:
    c = 'w'
elif cTurn == 3:
    c = 'g'
else:
    print("computer error!")

p = input("enter the the number for your choice:\nSnake(s) Water(w) Gun(g): ")

def gameResult(c, p):
    if c == p:
        return None
    elif c == 'w':
        if p == 'g':
            return False
        elif p == 's':
            return True
    elif c == 'g':
        if p == 's':
            return False
        elif p == 'w':
            return True
    elif c == 's':
        if p == 'w':
            return False
        elif p == 'g':
            return True

a = gameResult(c, p)

print(f"you choose : {p}")

print(f"computer choose : {c}")

if a == None:
    print("the game is a tie!")
elif a:
    print("you win")
else:
    print("computer win")


print(f"you choose : {p}")

print(f"computer choose : {c}")
