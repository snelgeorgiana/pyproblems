enunt = {
    "problema" : '''Se dau trei numere naturale a b x. Să se verifice 
dacă numărul x aparține intervalului [a,b].''',
    "solutie" : '''Se citesc de la consola cele 3 numere, se valideaza si se compara''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
a, b, x = (0, 0, 0)

def readData():
    global a, b, x
    #read nr a
    while True:
        sn = input('Enter number a: ')
        try:
            a = int(sn)
            if a < 0:
                print("youu should input a natural number\n")  
                continue  
        except:  
            print("you should input a naturall number\n")
            continue
        break
    #read nr b
    while True:
        sn = input('Enter number b: ')
        try:
            b = int(sn)
            if b <= a:
                print(F"you should input a natural number > {a}\n")
                continue    
        except:  
            print("you should input a natural number\n")
            continue
        break        
    #read nr x    
    while True:
        sn = input('Enter number x: ')
        try:
            x = int(sn)
            if x < 0:
                print(F"you should input a natural number\n")    
        except:  
            print("you should input a natural number\n")
            continue
        break        

def isValid():
    return bool(a <= x and x <= b)

def solve():
    readData()
    print(isValid())

if __name__ == "__main__":
    solve()