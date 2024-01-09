enunt = {
    "problema" : '''Se citește un cuvânt. Să se șteargă din cuvânt prima literă. Se va afișa un mesaj de forma:
După ștergerea literei 'X' șirul obținut este "S" de lungime L folosind diferite tipuri de formatare.''',
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

def newString():
    global s
    t = s[1:]
    print(f"Dupa stergerea literei {s[0]} sirul obtinut este {t} de lungime {len(t)}")

def newStringp():
    global s
    t = s.replace(s[0],'',1)
    print("Dupa stergerea literei {} sirul obtinut este {} de lungime {}".format(s[0], t, len(t)))    

def solve():
    readData()
    newString()
    newStringp()

if __name__ == "__main__":
    solve()