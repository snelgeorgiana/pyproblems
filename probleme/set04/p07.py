enunt = {
    "problema" : '''Se citește un cuvânt s. Să se determine cel mai mare prefix al acestuia care este palindrom.''',
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

def testPalindrom(s):
    return s[::-1] == s

def findPrefix():
    global s
    sp = ""; srez = ""
    for ch in s:
        sp += ch
        if testPalindrom(sp):
           srez = sp         
    print(srez)    

def solve():
    readData()
    findPrefix()

if __name__ == "__main__":
    solve()