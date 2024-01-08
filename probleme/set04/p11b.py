enunt = {
    "problema" : '''b) Se citește un număr natural k și text criptat cu cifrul lui Cezar cu cheia k. Să se afișeze
textul decriptat.''',
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
    fo = open("./p11b.in","r")    
    lw = fo.readlines()
    fo.close()
    k = int(lw[0])
    k = k % 25 # deoarece k nu tr sa fie mai mare de 25 (nrul literelor)

def decriptText():
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
    # k = 9; k = k % 25
    pord = ord(ch) - k
    if not ((ord(ch) in range(65, 91)) or (ord(ch) in range(97, 123))):
        return ch
    elif ord(ch) in range(65, 91):
        dt = pord - 65
        if (dt < 0):
            return chr(90 + dt + 1)
        else:
            return chr(pord)    
    elif ord(ch) in range(97, 123):
        dt = pord - 97
        if (dt < 0):
            return chr(122 + dt + 1)
        else:
            return chr(pord)            

def solve():
    readData()
    decriptText()
    # ch = replaceChar("b");print(ch)

if __name__ == "__main__":
    solve()