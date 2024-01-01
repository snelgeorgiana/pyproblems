import math

enunt = {
    "problema" : '''Dându-se o ecuaţie de gradul 2, să se scrie un program care determină soluţiile acestei
ecuaţii.''',
    "solutie" : '''Se rez ec.''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
a, b, c = (0.0, 0.0, 0.0) # ax^2 + bx + c = 0
def readData():
    global a , b, c
    print("You need to input a, b, c of ecuation ax^2 + bx + c = 0:")
    while True:
        sn = input('Enter number a: ')
        try:
            a = float(sn)
        except:  
            print("you should input a number\n")
            continue
        break
    while True:
        sn = input('Enter number b: ')
        try:
            b = float(sn)
        except:  
            print("you should input a number\n")
            continue
        break
    while True:
        sn = input('Enter number c: ')
        try:
            c = float(sn)
        except:  
            print("you should input a number\n")
            continue
        break

def findSolution():
    global a, b, c
    ssol = "No solution"
    delta = b**2 - 4*a*c
    if delta == 0:
        ssol = f"x1 = x2 = {-b/(2*a):.2f}"
    elif delta < 0:
        sqdelta = math.sqrt(-delta)
        ssol = f"x1 = {-b/2:.2f} + {sqdelta/2:.2f}i; x2 = {-b/2:.2f} - {sqdelta/2:.2f}i"
    elif delta > 0:
        ssol = "delta pozitiv"        
    print(f"Solution of equation {a}x^2 {sSign(b)} {abs(b)}x {sSign(c)} c = 0 is {ssol}")

def sSign(nr):
    rez = "-"
    if nr >= 0:
        rez = "+"
    return rez    

def solve():
    readData()
    findSolution()

if __name__ == "__main__":
    solve()