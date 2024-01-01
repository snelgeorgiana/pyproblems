enunt = {
    "problema" : '''Se dă un număr natural n. Să se afişeze în ordine crescătoare, primii n termeni ai şirului lui
Fibonacci''',
    "solutie" : '''S''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
n = 0
def readData():
    global n
    while True:
        sn = input('Enter a natural number (>=3): ')
        try:
            n = int(sn)
            if n < 3:
                print("you should input a natural number (>=3)\n")
                continue
        except:  
            print("you should input a natural number (>=3)\n")
            continue
        break

def calcSirFib():
    global n
    l = [1, 1]
    while len(l) < n:
        el = l[len(l)-2] + l[len(l)-1]
        l.append(el)
    print(l)

def solve():
    readData()
    calcSirFib()

if __name__ == "__main__":
    solve()