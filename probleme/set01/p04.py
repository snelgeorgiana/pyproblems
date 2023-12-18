import itertools

enunt = {
    "problema" : '''Să se genereze toate submulțimile mulțimii A=1,2,...,n, unde numărul natural nenul
n≤10 se citește de la tastatură (fără backtracking).''',
    "solutie" : '''Se foloseste functia combinations din modulul intertools''' 
}

def printEnunt():
    print("\nEnuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')

n = [0]; lst = []
def readData(n):
    while True:
        sn = input('Enter a number: ')
        try:
            n[0] = int(sn)
            if(n[0] < 0 or n[0] > 10):
                print("You should input a natural number <= 10\n")
                continue
        except:  
            print("You should input a natural number\n")
            continue
        break 
    
def multimeaPartilor(n, lst):
    for i in range(1, n[0]+1):
       lst.extend(itertools.combinations(range(1, n[0] + 1), i))    
    for i in lst:
        print(i)
def solve():
    readData(n)
    multimeaPartilor(n, lst)
    
if __name__ == "__main__":
    solve()