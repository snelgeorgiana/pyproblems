enunt = {
    "problema" : '''Se dau n numere naturale. Determinaţi primul număr par dintre cele n numere. Dacă nu
au fost citite numere pare, se va afişa doar mesajul IMPOSIBIL.''',
    "solutie" : ''' ''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
l = []
def readData(l):
    while True:
        sn = input('Enter a natural number: ')
        try:
            m = int(sn)
            if m <= 0:
                break 
            else:
                l.append(m)
        except:  
            print("you should input a natural number\n")
            continue
    print(l)    

# l = [3, 33, 12, 5, 6, 8]

def detectNumbers(l):
    vb = False
    for el in l:
        if el%2 == 0:
           vb = True
           print(el)
           break
    if not vb:
        print("Imposibil")       

def detectNumbersR(l):
    np = -1
    def detectNumbersRec(l, n):
        nonlocal np
        if l[n]%2 == 0:
            np = l[n]
        if n == 0: 
            return 1
        else: 
            detectNumbersRec(l, n-1)
    detectNumbersRec(l, len(l)-1)
    if np > 0:
        print(np)
    else:
        print("Imposibil")    

def solve():
    global np
    readData(l)
    # detectNumbers(l)
    detectNumbersR(l)

if __name__ == "__main__":
    solve()