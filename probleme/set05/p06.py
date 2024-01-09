enunt = {
    "problema" : '''Se citesc următoarele informații despre un student (date pe o linie): numele complet și
notele obținute la cele 5 examene din sesiune. Să se afișeze media notelor studentului și
cea mai mare nota obținută sub forma:
Studentul.... are media ..... și nota maxima....
unde media se va afișa cu două zecimale.
Exemplu- pentru datele de intrare:
Ionescu Popovici Marian 7 8 9 7 6
se va afișa
Studentul Ionescu Popovici Marian are media 7.40 și nota maxima 9''',
    "solutie" : ''' ''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
s = "" 
l = [] # the list with notes
name = "" # the string with the name
def readData():# eneter something like "Ana Maria Ciobanu Valentina 7 8 9 7 6"
    global s
    while True:
        sn = input('Enter a string with 5 numbers: ')
        try:
            s = sn.strip()
            if len(s) == 0 or not isValid(s):
                print(f"you should input a string with 5 numbers\n")
                continue
        except:  
            print("you should input a string with 5 numbers\n")
            continue
        break

def isValid(s):
    global l, name
    lp = []; lpp = []; name = ""
    if len(s) == 0:
        return False
    else:
        lp = s.split()
        k = 0
        for el in lp:
            try:
                n = float(el)
                k += 1
                lpp.append(n)
            except:
                name += " " + el
                continue
        if k != 5:
           return False  
        else:
           l = [*lpp]        
    return True 

def calcMedia():
    global l, name
    suma = 0; maxn = -1
    for el in l:
        if maxn < el:
           maxn = el 
        suma += el  
    media = suma/len(l)    
    sout = f"Studentul {name} are media {media: .2f} si nota maxima {maxn}"    
    print(sout)    
    # print(l)

def solve():
    readData()
    calcMedia()

if __name__ == "__main__":
    solve()