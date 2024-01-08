enunt = {
    "problema" : '''Se citește un șir de caractere reprezentând o propoziție în care cuvintele sunt despărțite între
ele prin spații. Să se numere câte cuvinte din propoziție se termină cu o vocală şi au minim 3 litere.''',
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

def countWords():
    global s, sv
    cw = 0; i = 0
    for ch in s:
        if ch == ' ' and s[i-1] in sv:
           cw += 1 
        i += 1
    # dc am un singur cuvant:    
    if cw == 0 and s[len(s)-1] in sv:
        cw = 1    
    print(cw)    

def solve():
    readData()
    countWords()

if __name__ == "__main__":
    solve()