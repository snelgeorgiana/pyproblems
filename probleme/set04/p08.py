enunt = {
    "problema" : '''Scrieți un program care să poată cripta un text folosind Cifrul Atbash. Cifrul Atbash este o
formă simplă de criptare în care literele alfabetului sunt inversate. Acesta înseamnă că litera
A este înlocuită cu Z, litera B cu Y, și tot așa. Textul de criptat conţine doar litere mari.''',
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

def criptString():
    global s
    srez = ""
    for ch in s:
        srez += replaceChar(ch)
    print(srez)

def replaceChar(ch):
    return chr(155 - ord(ch))

def solve():
    readData()
    criptString()
    

if __name__ == "__main__":
    solve()