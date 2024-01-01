enunt = {
    "problema" : '''Dându-se trei numere, R, G și B, verificați dacă acestea pot reprezenta o culoare sau o
nuanță de gri. O culoare se consideră nuanță de gri dacă și numai dacă diferența dintre
oricare două coduri ce reprezintă culorile primare nu depășește 10.''',
    "solutie" : '''Se evalueaza cele 3 numere si se valideaza: [0, 255].''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
n = [0, 0, 0]
def readData(n):
    k = 0; s="RGB"
    while k < 3:
        while True:
            sn = input(f"{s[k]}: ")
            try:
                n[k] = int(sn)
                if not testValid(n[k]):
                   print(f"The number {n[k]} is not a color\n")
                   continue 
            except:  
                print("you should input a natural number between 0 and 255\n")
                continue
            break
        k += 1

def testValid(nr):
    return 0 <= nr <= 255

def testGri(n):
    vrez = False
    if(abs(n[0] - n[1]) <= 10) and (abs(n[0] - n[2]) <= 10) and (abs(n[1] - n[2]) <= 10):
        vrez = True
    print(f"Numarul este nuanta de gri\n") if vrez else print(f"Numarul NU este nuanta de gri\n")

def solve():
    readData(n)
    testGri(n)

if __name__ == "__main__":
    solve()