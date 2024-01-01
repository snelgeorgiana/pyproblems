import math

enunt = {
    "problema" : '''Se citește un număr natural, n (n≥2) și se cere să se scrie cel mai mic număr natural care
are aceiași divizori primi ca n. Exemplu: dacă n=75, se scrie numărul 15, iar dacă n=7, se
scrie numărul 7.''',
    "solutie" : '''  ''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
n = 0; l = []
def readData():
    global n
    while True:
        sn = input('Enter a natural number (>=2): ')
        try:
            n = int(sn)
            if n < 2:
               print("you should input a natural number (>=2)\n")
               continue 
        except:  
            print("you should input a natural number (>=2)\n")
            continue
        break

def primeDivs(l):
    global n
    p = n
    radn = int(math.sqrt(n))+1
    # radn = int(n/2)
    # print(f"{n} => {int(math.sqrt(n))}")
    for i in range(2, radn):
        k=0
        while p%i == 0:
            k += 1
            p = p/i
        if k != 0:
           l.append((i, k)) 
    p = int(p)
    if p > 1:
       l.append((p,1))        
    print(l)

def calcRes(l):
    res = 1
    for i in range(len(l)):
        res *= l[i][0]
    print(res)

def solve():
    readData()
    primeDivs(l)
    calcRes(l)

if __name__ == "__main__":
    solve()