enunt = {
    "problema" : '''
a) [2,5p.] Să se citească și să se memoreze datele din fișierul cinema.in într-un dicționar în
care cheile sunt nume de cinematografe astfel încât să se răspundă cât mai eficient la
cerințele de la punctele următoare.
''',
    "solutie" : '''
    a) readData();  
    b) readDataA(); readDataB() 
    c) readDataA(); readDataC()''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
lw = {}
def readDataA():
    global lw
    fo = open("./cinema.in","r")    
    lt = fo.readlines()
    fo.close()
    if len(lt):
       for el in lt:
           ltt = el.split('%',1) 
           s1 = ltt[0].strip(); s2 = ltt[1].strip()
           if len(ltt) == 2:
                if not lw.get(s1):
                   lw[s1] = [s2]
                else:
                   lw.get(s1).append(s2)    
    print("Dictionar initial:")            
    print(lw)

cinema = ""; film = ""
def readDataB():
    global cinema, film, lw
    while True:
        sn = input('Enter a cinema: ')
        try:
            cinema = sn.strip()
            if len(cinema) == 0:
                print(f"you should input a string\n")
                continue
        except:  
            print("you should input a string\n")
            continue
        break
    while True:
        sn = input('Enter a film: ')
        try:
            film = sn.strip()
            if len(film) == 0:
                print(f"you should input a string\n")
                continue
        except:  
            print("you should input a string\n")
            continue
        break
    sterge_film(lw, cinema, film)
    print("Dictionar dupa stergere:")
    print(lw)

def sterge_film(lw, cinema, film):
    sp = lw.get(cinema)
    if sp:
       for i in range(len(sp)):
          if sp[i].find(film) >= 0:
            del sp[i]
               

# daca filmul ar apare de doua ori in lista - imposbil dar tratez ca exemplu
# def sterge_film(lw, cinema, film):
#     sp = lw.get(cinema)
#     if sp:
#         vbg = True
#         while vbg:
#           vbg = False
#           for i in range(len(sp)):
#             if sp[i].find(film) >= 0:
#                del sp[i]
#                vbg = True
#                break

# pt punctul c)
            
def readDataC():
    global lw
    lcinema = []
    for i in range(2):
        while True:
            sn = input('Enter a cinema: ')
            try:
                cinema = sn.strip()
                if len(cinema) == 0:
                    print(f"you should input a string\n")
                    continue
                else:
                    lcinema.append(cinema)
            except:  
                print("you should input a string\n")
                continue
            break
    cinema_film(lw, lcinema)        

# returneaza [(nume_film, nume_cinema, numar_ore)]
def cinema_film(lw, lcinema):
    lrez = []
    for el in lcinema:
        sp = lw.get(el)
        if sp:
            for elp in sp:
                ncinema = el
                sf = elp.split('%', 1)
                nfilm = sf[0].strip()
                nrore = len(sf[1].strip().split())
                lrez.append((nfilm, ncinema, nrore))
    lrez.sort(key = lambda x : (x[0], -x[2]))            
    if len(lrez):
      for el in lrez:
          print(f"Filmul '{el[0]}' ruleaza la '{el[1]}' de {el[2]} ori")


def solve():
    readDataA()
    # readDataB()
    readDataC()
    # cinema_film(lw, ["Cinema 1", "Cinema 2"])

if __name__ == "__main__":
    solve()