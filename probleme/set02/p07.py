enunt = {
    "problema" : '''Se citește un număr natural, n (n≥10), și se cere să se scrie valoarea True dacă numărul n
are toate cifrele egale, sau valoarea False în caz contrar.''',
    "solutie" : '''Se verifica cifra cu cifra''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
n = 0
def readData():
    global n
    while True:
        sn = input('Enter a natural number (>=10): ')
        try:
            n = int(sn)
            if n < 10:
               print("you should input a natural number (>=10)\n")
               continue 
        except:  
            print("you should input a natural number (>=10)\n")
            continue
        break

def isValid():
    global n
    rez = True; c = n%10; p = int(n/10)
    while p != 0:
        r = p%10
        if r != c: 
           rez = False
           break
        p = int(p/10)  

    print(rez)

def solve():
    readData()
    isValid()

if __name__ == "__main__":
    solve()