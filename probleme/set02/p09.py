import math

enunt = {
    "problema" : '''Un meșter trebuie să paveze întreaga pardoseală a unei bucătării cu formă dreptunghiulară
de dimensiune L1×L2 centimetri, cu plăci de gresie pătrate, toate cu aceeași dimensiune.
Știind că meșterul nu vrea să taie nici o placă de gresie și vrea să folosească un număr
minim de plăci, să se determine dimensiunea plăcilor de gresie de care are nevoie, precum
și numărul lor. De exemplu, dacă L1=440 cm și L2=280 cm, atunci meșterul are nevoie de
77 de plăci de gresie, fiecare având latura de 40 cm.''',
    "solutie" : '''  ''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
L1, L2 = (0, 0)
def readData():
    global L1, L2
    while True:
        sn = input('Enter a natural number(>0): ')
        try:
            L1 = int(sn)
            if L1 <= 0:
                print("you should input a natural number (>0)\n")    
                continue
        except:  
            print("you should input a natural number (>0)\n")
            continue
        break
    while True:
        sn = input('Enter a natural number(>0): ')
        try:
            L2 = int(sn)
            if L2 <= 0:
                print("you should input a natural number (>0)\n")    
                continue
        except:  
            print("you should input a natural number (>0)\n")
            continue
        break

def calcRes():
    global L1, L2
    aria = L1*L2
    sqaria = int(math.sqrt(aria))
    minim = 0
    for i in range(2, sqaria):
        if int(aria/i) == aria/i and pp(int(aria/i)):
            minim = int(aria/i); break
    print(f"Se aplica {int(aria/minim)} placi de latura {int(math.sqrt(minim))}")

def pp(nr):
    return math.sqrt(nr) == int(math.sqrt(nr))

def solve():
    readData()
    calcRes()

if __name__ == "__main__":
    solve()