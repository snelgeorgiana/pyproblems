enunt = {
    "problema" : ''' Se citește numărul natural n. Să se afișeze următoarea piramidă de numere:
1
1 2
1 2 3
.......
1 2 3 ... n''',
    "solutie" : ''' ''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
n = 0
def readData():
    global n
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

def showNumbers(n):
    if n == 0: 
        return
    else: 
        showNumbers(n-1) 
        print()
    for i in range(1, n+1):
        print(i, end=' ')

def solve():
    readData()
    showNumbers(n)

if __name__ == "__main__":
    solve()