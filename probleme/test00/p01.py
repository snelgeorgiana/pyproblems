enunt = {
    "problema" : '''Se citește de la tastatură o propoziție în care cuvintele sunt separate prin câte un spațiu.
a) Să se afișeze care este lungimea maximă a unui cuvânt din propoziție (0,75p)
b) Să se afișeze cuvintele de lungime maximă din propoziție pe o linie, separate cu spațiu (0,75p)
De exemplu, pentru propoziția "pentru acest exemplu avem lungime maxima 7" se va afișa 
7 
exemplu lungime''',
    "solutie" : ''' ''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
s = ""
def readData():
    global s
    while True:
        sn = input('Enter a string: ')
        try:
            s = sn.strip()
            if len(s) == 0:
                print(f"you should input a string\n")
                continue
        except:  
            print("you should input a string\n")
            continue
        break

def showResult():
    global s
    ls = s.split()
    wmax = -1
    for el in ls:
        if len(el) > wmax:
            wmax = len(el)
    print(wmax)
    for el in ls:
        if len(el) == wmax:        
           print(el, end=" ") 
    print()
    
def solve():
    readData()
    showResult()

if __name__ == "__main__":
    solve()