enunt = {
    "problema" : '''Se citește un cuvânt s. Să se afișeze șirul obținut prin ștergerea primei vocale.''',
    "solutie" : ''' ''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')

sv = {'a', 'e', 'i', 'o', 'u'}    
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

def removeVowel():
    global s 
    srez = ""; i = -1; vb = True
    for ch in s:
        i += 1
        if (ch in sv) and vb:
           vb = False
           continue
        srez += s[i]
    s = srez
    print(s)     

def solve():
    readData()
    removeVowel()

if __name__ == "__main__":
    solve()