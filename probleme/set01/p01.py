enunt = {
    "problema" : '''Se citește un număr întreg. Să se determine dacă acesta este par sau impar folosind
doar operatorii logici la nivel de biți.''',
    "solutie" : '''Se evalueaza ultimul bit (bit de paritate) prin opearatorul ~. 
Daca ultimul bit este 1 atunci nrul citit este impar.''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
n = [0]
def readData(n):
    while True:
        sn = input('Enter a number: ')
        try:
            n[0] = int(sn)
        except:  
            print("you should input an integer\n")
            continue
        break

def isEven(n):
    return not bool(n[0] & 1)

def solve():
    readData(n)
    print(isEven(n))

if __name__ == "__main__":
    solve()