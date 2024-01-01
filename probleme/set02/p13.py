enunt = {
    "problema" : '''Se dă n un număr natural nenul. Să se afle ultima cifră a sumei S=1^4 + 2^4 + 3^4 + ... +
n^4''',
    "solutie" : '''''' 
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

def calcSuma():
    global n
    s = 0
    for i in range(1, n+1):
        s += i ** 4
    p = s % 10    
    print(p)    

def solve():
    readData()
    calcSuma()

if __name__ == "__main__":
    solve()