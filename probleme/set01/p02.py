enunt = {
    "problema" : '''Dacă un număr natural n este de forma 2
k să se afișeze puterea k.''',
    "solutie" : '''Se imparte nrul succesiv la 2, se contorizeaza 
impartirile si se afiseaza contorul / nrul de iteratii. Folosesc ciclu repetitiv cu test final''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"])

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"])

n = [0,0]
def readData(n):
    while True:
        sn = input('Enter a number: ')
        try:
            n[0] = int(sn)
        except:  
            print("you should input an integer")
            continue
        break

def isValid(n):
    a = n[0]; k = n[1]; r = 0
    while True:
        r = a
        a /= 2; k += 1
        if a <= 1:
            r %= 2
            break
    if r == 0:    
       n[1] = k
       return True    
        
def solve():
    readData(n)
    vb = isValid(n)
    print(f'Numarul {n[0]} este de forma 2 la puterea {n[1]}') if vb else print(f'Numarul {n[0]} nu este putere a lui 2')

if __name__ == "__main__":
    solve()