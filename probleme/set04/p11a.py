enunt = {
    "problema" : '''Cifrul lui Cezar
a) Se citește un text și un număr natural k. Să se afișeze textul cifrat cu cifrul lui Cezar, prin
care fiecare literă (!doar literele) este înlocuită cu litera aflată peste k poziții la dreapta în
alfabet în mod circular (valoarea k reprezintă cheia secretă comună pe care trebuie să o
cunoască atât expeditorul, cât și destinatarul mesajului criptat). De exemplu, pentru textul "O
zi frumoasa!" și k=9 se va afișa “X ir oadvxjbj! " ''',
    "solutie" : ''' ''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
lw = [] #lines with text to be cripted
k = 0
def readData():
    global lw, k
    fo = open("./p11a.in","r")    
    lw = fo.readlines()
    fo.close()
    k = int(lw[0])
    k = k % 25 # deoarece k nu tr sa fie mai mare de 25 (nrul literelor)

def criptText():
    global k
    i = 1; srez = ""
    while i < len(lw):
        s = lw[i]
        for ch in s:
            srez += replaceChar(ch)
        i += 1    
    print(srez)

def replaceChar(ch):
    global k
    pord = ord(ch) + k
    if not ((ord(ch) in range(65, 91)) or (ord(ch) in range(97, 123))):
        return ch
    elif ord(ch) in range(65, 91):
        dt = pord - 90
        if (dt > 0):
            return chr(65 + dt - 1)
        else:
            return chr(pord)    
    elif ord(ch) in range(97, 123):
        dt = pord - 122
        if (dt > 0):
            return chr(97 + dt - 1)
        else:
            return chr(pord)            

def solve():
    readData()
    criptText()
    # ch = replaceChar("i");print(ch)

if __name__ == "__main__":
    solve()