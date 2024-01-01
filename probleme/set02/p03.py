enunt = {
    "problema" : '''Dându-se o ecuaţie de gradul 1, să se scrie un program care determină soluţiile acestei
ecuaţii.''',
    "solutie" : '''Se rez ec.''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
a , b = (0.0, 0.0) # ax +b = 0
def readData():
    global a , b
    print("You need to input a , b of ecuation ax + b = 0:")
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

def findSolution():
    print(f"Solution of equation {a}x {sSign(b)} {abs(b)} = 0 is x = {-b/a}")

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