enunt = {
    "problema" : '''Se citește n, natural. Afișați cea mai mare putere a lui 2 care îl divide pe n.''',
    "solutie" : '''Cat timp restul imp la 2 a nrului citit este 0 
se imparte succesiv la 2 si se retine nrul iteratiilor.''' 
}

def printEnunt():
    print("\nEnuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')

n = [0]
def readData(n):
    while True:
        sn = input('Enter a number: ')
        try:
            n[0] = int(sn)
            if(n[0] < 0):
                print("You should input a natural number\n")
                continue
        except:  
            print("You should input a natural number\n")
            continue
        break

def ordinulLuiDoi(n):
    a = n[0]; k = 0
    while not a % 2:
        a /= 2
        k += 1            
    return k

def solve():
    readData(n)
    print(f'Ordinul lui 2 in descompunerea lui {n[0]} este {ordinulLuiDoi(n)}')

if __name__ == "__main__":
    solve()