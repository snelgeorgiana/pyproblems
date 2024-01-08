enunt = {
    "problema" : '''Se citește un șir de caractere în care după fiecare litera este un x. Care este șirul initial?''',
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

def removeX():
    global s
    s = s.replace('x','')
    s = s.replace('X','')
    print(s)
    
def solve():
    readData()
    removeX()

if __name__ == "__main__":
    solve()