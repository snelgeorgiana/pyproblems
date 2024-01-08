import re

enunt = {
    "problema" : '''Sir periodic. Se citește un șir de caractere s. Să se verifice dacă există un șir t, diferit de s,
astfel încât s să se poată obține prin concatenarea de un număr arbitrar de ori (k>1) a șirului t
(adică să se verifice dacă șirul s este periodic). Dacă există mai multe astfel de șiruri t se va
determina cel mai lung. Exemplu: șirul s = abbaabbaabbaabba se obține prin concatenarea
șirului t= abbaabba de două ori.''',
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

def isPeriodic():
    global s
    t = ""; fs = ""; k = 0; ctr = 0; i = 0
    while i < len(s):
        t += s[i]
        i += 1
        kk = countSub(t, s)
        if(kk*len(t) == len(s)) and (kk > 1):
            k = kk; fs = t
    if k > 1:print(f"sirul {fs} se repeta de {k} ori")

# def countSub(subs, ss):
#     return len(re.findall(f'(?=({subs}))', ss))

def countSub(subs, ss):
    count = 0
    n = len(ss)
    m = len(subs)
    i = 0
    while  i < n-m+1:
        if ss[i:i+m] == subs:
            count += 1
            i = i+m
            continue
        i += 1   
    return count

def solve():
    readData()
    isPeriodic()
    # p = countSub("abbaabba", "abbaabbaabbaabba")
    # print(p)

if __name__ == "__main__":
    solve()