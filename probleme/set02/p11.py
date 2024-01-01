enunt = {
    "problema" : '''Se dă un număr natural n. Afișați în ordine descrescătoare primele n numere naturale
impare.''',
    "solutie" : '''  ''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
n = 0
def readData():
    global n
    while True:
        sn = input('Enter a natural number: ')
        try:
            n = int(sn)
            if n < 0:
                print("you should input a natural number\n")
                continue
        except:  
            print("you should input a natural number\n")
            continue
        break

def showNumbers():
    global n
    l = []; k = 0
    while k < n:
        l.append(2*k + 1)
        k += 1
    print(l)    
    

def solve():
    readData()
    showNumbers()

if __name__ == "__main__":
    solve()