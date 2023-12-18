enunt = {
    "problema" : '''Să se scrie un program care citeşte de la tastatură 
trei numere naturale și determină diferenţa dintre cel mai mare şi cel mai mic.''',
    "solutie" : '''Se citesc de la consola cele 3 numere, se valideaza 
si se fol max()-min()''' 
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

def calcDiff():
    return max(a, b, c)-min(a, b, c)

def solve():
    readData()
    print(calcDiff())

if __name__ == "__main__":
    solve()