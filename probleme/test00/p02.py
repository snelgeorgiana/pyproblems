enunt = {
    "problema" : '''
a) Scrieți o funcție fără parametri care citește de la tastatură o listă de numere naturale (un
vector) cu elementele date pe o linie separate cu spații și returnează această listă. (0,5p)
b) Scrieți o funcție care primește ca parametru un număr natural n și returnează numărul de
divizori proprii ai lui n. (1p)
c) Folosind funcția de la a) să se citească o listă v de numere naturale. Apoi se citește de la
tastatură un număr natural k. Folosind funcția de la b) afișați pe ecran numerele din lista v
care au cel mult k divizori proprii, ordonate crescător, fără duplicate (un număr va fi scris o
singură dată chiar dacă apare de mai multe ori în listă). (1p)
De exemplu, la punctul c), pentru datele de intrare
9 1 9 100 101 10 7 9
2
se va afișa
1 7 9 101''',
    "solutie" : ''' a) readDataA();  b) nrDivPr(n);  c) readDataA();readDataB();selectNumbers()''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
l = []
def readDataA():
    global l
    while True:
        sn = input('Enter a list of natural numbers: ')
        try:
            if(len(sn) == 0):
               print("you should input a list of natural numbers")
               continue 
            l = sn.split()
            if not validList(l):
               print("you should input a list of natural numbertts")
               continue 
        except:  
            print("you should input a list of natural numbers\n")
            continue
        break
    print(l)

k = 0
def readDataB():
    global k
    while True:
        sn = input('Enter a natural number k = ')
        try:
            k = int(sn)
            if k < 0:
               print("you should input a natural number\n")
               continue
        except:  
            print("you should input a natural number\n")
            continue
        break

# valideaza sirul citit sa fie numere naturale 
def validList(l):
    for el in l:
        if not el.isnumeric():
           return False
    return True
    
# returneaza numarul de divizori proprii ai lui n
def nrDivPr(n):
    k = 0
    for d in range(2, n//2+1):
        if n%d != 0:
            continue
        k += 1
    return k        

# selecteaza nrele cu nrdivpr < k in lista lsel, elimina dublurile prin convertire lista in set si afiseaza set-ul
def selectNumbers():
    global l
    print(l)  
    lsel = []
    for el in l:
        iel = int(el)
        if(nrDivPr(iel)) < k: #se poate evita folosirea set-ului adaugandu-se aici: and iel not in lsel:
            lsel.append(iel)
          
    if(len(lsel)):
        ls = set(lsel)
        print(sorted(ls))

def solve():
    readDataA()
    readDataB()
    selectNumbers()

if __name__ == "__main__":
    solve()