enunt = {
    "problema" : '''Se citește de la tastatură un număr natural de maxim 2 cifre. Să se afișeze pe ecran
valori astfel: dacă numărul este mai mic sau egal cu 15 se va afișa pătratul valorii
sale; dacă numărul este cuprins între 16 și 30 (inclusiv) se va afișa suma cifrelor sale;
în caz contrar se va afișa produsul cifrelor sale.''',
    "solutie" : '''Se citeste numrul de la consola, se valideaza 
si se fol max()-min()''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
n = 4

def readData():
    global n
    #read nr a
    while True:
        sn = input('Enter an integer number: ')
        try:
            n = int(sn)
            if countDigits(n) > 2:
               print("you should input an integer <= 2\n") 
               continue
        except:  
            print("you should input an integer\n")
            continue
        break

def countDigits(n):
    # return len(str(abs(n)))
    k = 0; n = abs(n)
    while n != 0:
        n //= 10
        k += 1
    return k

def evaluateNr():
    global n
    if n <= 15:
       print(f'Patratul lui {n} este {n ** 2}')
    elif 16 <= n and n <= 30:
       print(f'Suma cifrelor lui {n} este {sumaCifre(n)}')
    else:
       print(f'Produsul cifrelor lui {n} este {produsCifre(n)}') 

def sumaCifre(n):
    m = abs(n); s = 0
    while m != 0:
        s += m % 10
        m //= 10
    return s

def produsCifre(n):
    m = abs(n); p = 1
    while m != 0:
        p *= m % 10
        m //= 10
    return p

def solve():
    readData()
    evaluateNr()

if __name__ == "__main__":
    solve()