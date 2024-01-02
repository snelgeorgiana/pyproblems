enunt = {
    "problema" : '''Se citesc două numere naturale a și b cu cel mult două cifre. Să se afișeze toate numerele
naturale pozitive de cel mult două cifre care se divid cu 5 și nu se află în intervalul [a,b]
(numerele se vor afișa pe aceeași linie, ordonate crescător, apoi descrescător).''',
    "solutie" : ''' ''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
a, b = (0, 0)
def readData():
    global a, b
    while True:
        sn = input('Enter a natural number a with max 2 ciphers : ')
        try:
            a = int(sn)
            if a < 0 or not isValid(a):
                print("you should input a natural number\n")
                continue
        except:  
            print("you should input a natural number\n")
            continue
        break
    while True:
        sn = input(f'Enter a natural number b > {a} with max 2 ciphers : ')
        try:
            b = int(sn)
            if b < 0 or a >= b or not isValid(b):
                print(f"you should input a natural number b > {a}\n")
                continue
        except:  
            print(f"you should input a natural number b > {a}\n")
            continue
        break


def isValid(n):
    nr = len(str(n))
    return 1 <= nr and nr <= 2

def showNumbers():
    global a, b
    l = []
    for k in range(0, 20):
        nr = 5*k
        if nr < a or nr > b:
            l.append(nr)
    print(l)

def solve():
    readData()
    showNumbers()

if __name__ == "__main__":
    solve()