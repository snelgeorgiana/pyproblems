enunt = {
    "problema" : '''Se dau coordonatele a două puncte diferite din plan. Să se stabilească dacă dreapta
determinată de cele două puncte este orizontală, verticală sau oblică.''',
    "solutie" : '''Se evalueaza coordonatele''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    


def readData(s1 = "", s2 = ""):
    while True:
        sn = input(f'Enter {s1} number: ')
        try:
            x = float(sn)
        except:  
            print("you should input a number\n")
            continue
        break
    while True:
        sn = input(f'Enter {s2} number: ')
        try:
            y = float(sn)
        except:  
            print("you should input a number\n")
            continue
        break
    return (x, y)

def detPos():
    global p0, p1
    if(p0[0] == p1[0] and p0[1] != p1[1]):
        print("Deapta este verticala")
    elif(p0[0] != p1[0] and p0[1] == p1[1]):
        print("Deapta este orizontala")
    else:
        print("Dreapta este oblica")        

def solve():
    global p0, p1
    p0 = readData("P0.x", "P0.y")
    p1 = readData("P1.x", "P1.y")
    detPos()

if __name__ == "__main__":
    solve()
    