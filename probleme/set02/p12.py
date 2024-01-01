enunt = {
    "problema" : '''Să se scrie un program care citește numărul natural n și determină suma S=1*n+2*(n-
1)+3*(n-2)+...+n*1.''',
    "solutie" : '''''' 
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

def calcSuma():
    l = [*range(1,n+1)]
    s = 0
    for i in range(n):
        # print(l[i],l[len(l)-i-1])
        s += l[i]*l[len(l)-i-1]
    print(s)

def solve():
    readData()
    calcSuma()

if __name__ == "__main__":
    solve()