
enunt = {
    "problema" : '''Se dau n numere naturale. Calculați media lor geometrică.''',
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
            n = int(sn)
            if n <= 0:
                break 
            else:
                l.append(n)
        except:  
            print("you should input a natural number\n")
            continue
        # break

def mg(l):
    p = 1; rez = 0
    for el in l:
        p *= el
    rez = p ** (1/len(l))
    print(f"mg = {rez:.3f}")

def solve():
    readData(l)
    mg(l)

if __name__ == "__main__":
    solve()