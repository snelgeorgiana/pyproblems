import math

enunt = {
    "problema" : '''Se citește un număr natural, n (n≥2), și se cere să se scrie numărul prim care apare la puterea
cea mai mică în descompunerea în factori primi a lui n. Dacă sunt mai multe astfel de
numere, se scrie cel mai mic dintre acestea. Exemplu: dacă n=880, se scrie numărul 5''',
    "solutie" : ''' ''' 
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

def minimNr(l):
    m1 = 1000; m2 = 1000; ic = 0
    for i in range(len(l)):
        if l[i][1] <= m1:
            m1 =  l[i][1] 
    for i in range(len(l)):
        if (l[i][1] == m1) and (l[i][0] < m2):
            m2 =  l[i][0]        
    print(m2)
    
def solve():
    readData()
    primeDivs(l)
    minimNr(l)

if __name__ == "__main__":
    solve()