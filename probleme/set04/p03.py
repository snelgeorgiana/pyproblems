enunt = {
    "problema" : '''Se citește un șir de caractere și un număr natural k. Să se șteargă din s caracterul de pe poziția
k (pozițiile numerotate de la 0) și să se afișeze șirul nou obținut.''',
    "solutie" : ''' ''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
n = ["", 0]
def readData():
    sn = input(f'Enter a string: ')
    while True:
        try:
            n[0] = sn.strip()
            if len(n[0]) == 0:
                print("you should input a string\n")
                continue
        except:
            print("you should input a string\n")
            continue
        break    
    while True and len(n[0])>0:
        sn = input(f'Enter a natural number (<{len(n[0])}): ')
        try:
            n[1] = int(sn)
            if n[1]<0 or n[1] >= len(n[0]):
                print(f"you should input a natural number (<{len(n[0])})")
                continue
        except:  
            print("you should input an integer\n")
            continue
        break

def makeString():
    s = n[0]; k = n[1]; 
    s = s.replace(s[k],'')
    print(s)
def makeStringp():
    n[0] = n[0].replace(n[0][n[1]],'')
    print(n[0])

def solve():
    readData()
    makeString()
    # makeStringp()

if __name__ == "__main__":
    solve()