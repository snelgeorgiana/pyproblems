enunt = {
    "problema" : '''Se dau n numere naturale nenule. Calculaţi suma celor n numere date.''',
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

def calcSuma(l):
    sum = 0
    for el in l:
        sum += el
    print(sum)

def calcSumaRecLista(l, n):
    if n == 0:
       return l[0]
    else:
       return l[n] + calcSumaRecLista(l, n-1) 


# suma primelor n + 1 numere naturale 0 + 1 + 2 +... + n
# calculata recursiv    
def calcSumaRec(n):
    if n == 0: 
        return 0
    else:
        return n + calcSumaRec(n-1)  

def solve():
    readData(l)
    # p = calcSumaRec(3);print(p)
    p = calcSumaRecLista(l, len(l) - 1); print(p)

if __name__ == "__main__":
    solve()