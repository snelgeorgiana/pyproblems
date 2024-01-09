enunt = {
    "problema" : '''Se citesc un cuvânt s, un cuvânt t și un număr k (date fiecare pe o linie). Să se verifice dacă
t apare ca subșir într-un șir s de cel puțin k ori (se numără aparițiile care nu se suprapun).
În caz afirmativ să se afișeze k poziții la care începe t în s, altfel să se afișeze un mesaj
corespunzător.''',
    "solutie" : ''' ''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
# s = "abbaabbaabbaabba"; t = "abbaabba"; k=0
s=""; t=""; k = 0    
def readData():
    global s, t, k
    while True:
        sn = input('Enter a string s: ')
        try:
            s = sn.strip()
            if len(s) == 0:
                print(f"you should input a string\n")
                continue
        except:  
            print("you should input a string\n")
            continue
        break
    while True:
        sn = input('Enter a string t:')
        try:
            t = sn.strip()
            if len(t) == 0:
                print(f"you should input a string\n")
                continue
        except:  
            print("you should input a string\n")
            continue
        break
    while True:
        sn = input('Enter a natural number k: ')
        try:
            k = int(sn)
            if k < 0:
                print(f"you should input a natural number\n")
                continue
        except:  
            print("you should input a natural number\n")
            continue
        break

def showResult():
    global s, t, k
    k1 = countSubs()
    print(f"Subsirul {t} se regaseste in sirul {s} de {k1} ori.")
    print(f"Deci {k1} >= {k} este {k1 >= k}")

def countSubs():
    global s, t
    return s.count(t)

def solve():
    readData()
    showResult()

if __name__ == "__main__":
    solve()