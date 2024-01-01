enunt = {
    "problema" : '''Se citește un număr natural, n, și se cere să se scrie valoarea True dacă toate cifrele lui n
sunt din mulțimea {2,3} sau valoarea False în caz contrar.''',
    "solutie" : '''Se evalueaza nrul cifra cu cifra.''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
n = 0
def readData():
    global n
    while True:
        sn = input('Enter a natural number: ')
        try:
            n = int(sn)
            if n < 0:
               print("you should input a natural number\n") 
               continue
        except:  
            print("you should input a natural number\n")
            continue
        break

def isValid():
    global n
    sn = "nu"; vb = True
    s = {2, 3}; m = n
    while m != 0:
        p = m % 10
        vb = p in s
        if not vb:
           break
        m = int(m/10) 
    if not vb:
        sn = ""
    print(f"Nrul {n} {sn} are cifre care nu sunt in {2, 3}")   
    return vb 

def solve():
    readData()
    print(isValid())

if __name__ == "__main__":
    solve()