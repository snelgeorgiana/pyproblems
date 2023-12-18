import math

enunt = {
    "problema" : '''Fie x număr natural,citit. Să se verifice dacă x este:
a. pătrat perfect (fără structuri repetitive);
b. palindrom (este egal cu răsturnatul său).''',
    "solutie" : '''a. Se verifica dc sqrt(x) este nr intreg
b. se conv nrul in string, se inverseaza o copie si se compara cu originalul''' 
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

def isPerfectSquare():
    global n
    np = math.sqrt(n)
    return np.is_integer()

def isPalindrom():
    vb = True
    global n
    return str(n) == "".join(reversed(str(n)))


def solve():
    readData()
    print(f"Numarul {n} este patrat perfect") if isPerfectSquare() else print(f"Numarul {n} NU este patrat perfect")
    print(f"Numarul {n} este palindrom") if isPalindrom() else print(f"Numarul {n} NU este palindrom")

if __name__ == "__main__":
    solve()