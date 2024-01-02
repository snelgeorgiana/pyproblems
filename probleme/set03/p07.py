enunt = {
    "problema" : '''Se dau două numere naturale nenule n și p. Afișați în ordine crescătoare puterile lui n mai
mici sau egale cu p.''',
    "solutie" : ''' ''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
n, p = (0, 0)
def readData():
    global n, p
    while True:
        sn = input('Enter a natural number n: ')
        try:
            n = int(sn)
            if n < 0:
                print("you should input a natural number\n")
                continue
        except:  
            print("you should input a natural number\n")
            continue
        break
    while True:
        sn = input(f'Enter a natural number p > {n}: ')
        try:
            p = int(sn)
            if p < 0 or n > p:
                print(f"you should input a natural number p > {n}\n")
                continue
        except:  
            print(f"you should input a natural number p > {n}\n")
            continue
        break


def showNumbers():
    global n, p
    l = [(n, 0)]
    print(1, end=' ')
    exponent = 1
    pp = n ** exponent
    while pp < p:
        print(pp, end=' ')
        l.append((n, exponent))
        exponent += 1
        pp = n ** exponent
    print()    
    print(l)



def solve():
    readData()
    showNumbers()

if __name__ == "__main__":
    solve()