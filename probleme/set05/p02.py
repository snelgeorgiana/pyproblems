enunt = {
    "problema" : '''Se citește un cuvânt s de cel mult 10 de caractere. Sa se afișeze pe câte o linie cuvintele
obținute succesiv din s tăind prima literă (afișate pe 10 de caractere aliniat la dreapta),
folosind diverse metode de formatare, inclusiv metoda rjust:
algoritm
 lgoritm
  goritm
   oritm
    ritm
     itm
      tm
       m''',
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
        sn = input('Enter a string (max 10 characters): ')
        try:
            s = sn.strip()
            if len(s) == 0 or len(s) > 10:
                print(f"you should input a string (max 10 characters)\n")
                continue
        except:  
            print("you should input a string (max 10 characters)\n")
            continue
        break

def showString():
    global s
    for i in range(len(s)):
        t = s[i:]
        print(t.rjust(10))

def solve():
    readData()
    showString()

if __name__ == "__main__":
    solve()