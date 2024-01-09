enunt = {
    "problema" : '''Se citește o propoziție în care cuvintele sunt separate prin spațiu. Să se creeze o nouă
propoziție în care fiecare cuvânt din propoziția inițială este înlocuit de cuvântul obținut
prin ordonarea literelor sale și să se afișeze noua propoziție. De exemplu, pentru propoziția:
un doi trei
se va afișa
nu dio eirt''',
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
    l = s.split()
    i = 0
    for w in l:
        l[i] = newWord(w)
        i += 1
    s = ' '.join(l)     
    print(s)    
    
def newWord(w):
    l = [*w]
    l.sort() 
    w = "".join(l)
    # print(w)
    return w

def solve():
    readData()
    showResult()

if __name__ == "__main__":
    solve()