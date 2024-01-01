enunt = {
    "problema" : '''Se citesc două numere naturale a și b. Să se afișeze cel mai mic număr Fibonacci din
intervalul [a,b].''',
    "solutie" : '''  ''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
a, b = (0, 0)
def readData():
    global a, b
    while True:
        sn = input('Enter a natural number a: ')
        try:
            a = int(sn)
            if a < 0:
                print("you should input a natural number(>0)\n")
                continue
        except:  
            print("you should input a natural number(>0)\n")
            continue
        break
    while True:
        sn = input(f'Enter a natural number b > {a}: ')
        try:
            b = int(sn)
            if a < 0 or b <= a:
               print(f"you should input a natural number(>{a})\n")
               continue
        except:  
            print(f"you should input a natural number(>{a})\n")
            continue
        break

def calcSirFib():
    global a, b
    l = [1, 1, 2]
    n = 0
    while n <= a:
        n = l[len(l)-2] + l[len(l)-1]
        l.append(n)
    print(l)
    if a <= l[len(l)-1] and l[len(l)-1] <= b:
        print(l[len(l)-1])
    else:
        print("No number")    

def solve():
    readData()
    calcSirFib()

if __name__ == "__main__":
    solve()