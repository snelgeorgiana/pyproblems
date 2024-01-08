enunt = {
    "problema" : '''Aceeași cerință, dar pentru cuvintele dintr-o propoziție în care cuvintele sunt despărțite între
ele prin spații. De exemplu, pentru w = "cere", p = 2 , n=4 și propoziția "Ana are mere si
pere si banane de mancare", trebuie să se afișeze următorul rezultat: 2-rimele
cuvântului 'cere' sunt: are mere pere mancare.''',
    "solutie" : '''Atentie, n este folosit ca numar maxim de cuvinte afisate.Nu se afiseaza are pt ca sunt doar 3 litere. Greseala in enunt.''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')

# se citesc datele din fisierul p09a.in

lw = [] #list of the words to be cheked from index 0
w = ""; p = 0; n = 0
def readData():
    global lw, w, p, n
    fo = open("./p09b.in","r")    
    lwp = fo.readlines()
    fo.close()
    lw1 = lwp[0].split(' ')
    w = lw1[0]; p = int(lw1[1])
    n = int(lw1[2])
    lw = lwp[1].split(' ')

def showWords():
    wrima = w[-p:]
    k = 0
    for i in range(len(lw)):
        wd = lw[i].replace('\n','')
        if (len(wd) >= p + 2) and (wd[-p:] == wrima) and k <= n:
            print(wd); k += 1

def solve():
    readData()
    showWords()

if __name__ == "__main__":
    solve()