enunt = {
    "problema" : '''Se citește de la tastatură un șir de numere reale pozitive v1,v2,..., vn (numerele sunt date
pe o linie, separate cu spațiu). Să se determine media aritmetică a numerelor din șir și să se
afișeze un mesaj de forma:
“(v1+... + vn)/n=media” unde media este media numerelor din șir afișată cu o zecimală.
De exemplu, pentru datele de intrare 40 15 1.25 1.4 se va afișa (40+15+1.25+1.4)/4=14.4''',
    "solutie" : ''' ''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
s = ""; l = []
def readData():# eneter something like "40 15 1.25 1.4"
    global s
    while True:
        sn = input('Enter a sequence of real numbers: ')
        try:
            s = sn.strip()
            if len(s) == 0 or not isValid(s):
                print(f"you should input a sequence of real numbers\n")
                continue
        except:  
            print("you should input a sequence of real numbers\n")
            continue
        break

def isValid(s):
    global l
    if len(s) == 0:
        return False
    else:
        l = s.split()
        for el in l:
            try:
                n = float(el)
            except:
                l = []
                return False  
    return True 

def calcMedia():
    global l
    suma = 0; sout = "("; k =0
    for el in l:
        suma += float(el)
        k += 1
        if k == 1: 
            sout += el
        else:
            sout += "+" + el    
    media = suma/len(l)    
    sout += f")/{len(l)} = {media: .1f}"    
    print(sout)    

def solve():
    readData()
    calcMedia()
    

if __name__ == "__main__":
    solve()