enunt = {
    "problema" : '''Să se scrie un program care determină minimul a trei numere întregi.''',
    "solutie" : '''Se citesc de la consola cele 3 numere, se valideaza si se fol ftia min()''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
a, b, c = (0, 0, 0)

def readData():
    global a, b, c
    #read nr a
    while True:
        sn = input('Enter number a: ')
        try:
            a = int(sn)
        except:  
            print("you should input an integer\n")
            continue
        break
    #read nr b
    while True:
        sn = input('Enter number b: ')
        try:
            b = int(sn)  
        except:  
            print("you should input an integer\n")
            continue
        break        
    #read nr c    
    while True:
        sn = input('Enter number c: ')
        try:
            c = int(sn)
        except:  
            print("you should input an integer\n")
            continue
        break        

def calcMin():
    return min(a, b, c)

def solve():
    readData()
    print(calcMin())

if __name__ == "__main__":
    solve()