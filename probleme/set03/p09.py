enunt = {
    "problema" : '''Se citește numărul natural n, şi două caractere c şi d. Să se afișeze următorul pătrat,
format din n linii şi n coloane:
ccc...cc
cdd...dc
....
cdd...dc
ccc...cc''',
    "solutie" : ''' ''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
n, c, d = (5, 'c', 'd')
def readData():
    global n, c, d
    while True:
        sn = input('Enter a natural number n: ')
        try:
            n = int(sn)
            if n < 0:
                print("you should input a natural number\n")
                continue
        except:  
            print("you should input a natural number\n")
            continue
        break
    for i in range(2):
        sord = "first"
        if i == 1:
           sord = "second" 
        while True:
            sn = input(f'Enter {sord} character: ')
            if len(sn.strip()) != 1:
                    print("you should input a single character\n")
                    continue
            try:
                if i == 0:
                    c = sn.strip()
                else:
                    d = sn.strip()     
            except:  
                print("you should input a single character\n")
                continue
            break

def showSquare():
    global n, c, d
    if n == 1:print(c) 
    if n == 2:print(f"{c}{c}"); print(f"{c}{c}")
    if n >= 3:
       for i in range(n):print(c, end='')
       print()
       for i in range(1, n-1):
           for j in range(n): 
              if j == 0 or j == n-1: 
                  print(c, end='')
              else: 
                  print(d, end='') 
           print()  
    #    print()       
       for i in range(n):print(c, end='')
       print()
             

def solve():
    readData()
    showSquare()

if __name__ == "__main__":
    solve()