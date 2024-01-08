enunt = {
    "problema" : '''a) Se citește un cuvânt w, un număr natural nenul p, un număr natural n și un șir format din n
cuvinte, date fiecare pe o linie. Să se afișeze toate cuvintele care sunt p-rime cu w (adică
ultimele p caractere din cuvânt coincid cu ultimele p caractere ale lui w) și au lungime cel
puțin p+2. De exemplu, pentru w = "mere", p = 2 , n=4 și cuvintele "pere", "teste", “are” și
"programare", trebuie să fie afișate cuvintele "pere" și "programare" (“are” rimează cu “mere”,
dar are lungime mai mică decât p+2.''',
    "solutie" : ''' ''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')

# se citesc datele din fisierul p09a.in

lw = [] #list of the words to be cheked from index 1
w = ""; p = 0; n = 0
def readData():
    global lw, w, p, n
    fo = open("./p09a.in","r")    
    lw = fo.readlines()
    fo.close()
    lw1 = lw[0].split(' ')
    w = lw1[0]; p = int(lw1[1])
    n = int(lw1[2])

def showWords():
    wrima = w[-p:]
    for i in range(len(lw)):
        if i == 0:
           continue
        wd = lw[i].replace('\n','')
        if (len(wd) >= p + 2) and (wd[-p:] == wrima):
            print(wd)

def solve():
    readData()
    showWords()

if __name__ == "__main__":
    solve()