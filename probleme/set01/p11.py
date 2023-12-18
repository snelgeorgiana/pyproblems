enunt = {
    "problema" : '''Se citește un șir de valori întregi până la întâlnirea lui 0. Să se afișeze:
a. valoarea maximă din șir;
b. media aritmetică a valorilor pozitive.''',
    "solutie" : '''a. se salveaza nrele intr-un set si se aplica max()
b. se parcurge setul si se calc ma''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
m = set()
def readData():
    x = 0
    while True:
        sn = input('Enter an integer: ')
        try:
            x = int(sn)
            if x == 0:
               break 
            else:
               m.add(x)
               continue
        except:  
            print("you should input an integer\n")
            continue
        break

def printMax():
    global m
    print(f"Maximul este {max(m)}")

def printMA(): 
    s = 0
    for el in m:
        s += el
    print(f"nrl = {s / len(m)}")

def solve():
    readData()
    printMax()
    printMA()

if __name__ == "__main__":
    solve()