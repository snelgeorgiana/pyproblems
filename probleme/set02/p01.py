from datetime import datetime

enunt = {
    "problema" : '''Se dă un număr natural n cu exact 13 cifre reprezentând un cod numeric personal. Să se
afișeze anul, luna și ziua nașterii deținătorului.''',
    "solutie" : '''Numarul se converteste in lista si apoi se afiseaza grupurile de cifre cerute.''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
n = 1_000_000_000_000
def readData():
    global n
    n = 1_900815_000_000
    # global n
    # while True:
    #     sn = input('Enter a natural 13 ciphers number(CID): ')
    #     try:
    #         n = int(sn)
    #         if len(str(n)) == 13 or n == 0:
    #            break 
    #         else:
    #            print("Wrong! You should input a natural 13 ciphers number(CID)!\n")
    #            continue
    #     except:  
    #         print("you should input an integer\n")
    #         continue
    #     break

def printData():
    print(f"Data nasterii: {bDay()} {bMonth()} {bYear()}")

def bYear():
    global n
    dtnow = datetime.now()
    sy = str(dtnow.year)[2:4]
    ny_now = int(sy)
    s =  str(n)
    ny_read = int(s[1:3])
    sadd = "20"
    if ny_read > ny_now:
        sadd = "19"
    sny = sadd + s[1:3]   
    return sny 
    
def bMonth():
    global n
    months = ["Ianuarie", "Februarie", "Martie", "Aprilie", "Mai",
              "Iunie", "Iulie", "August", "Septembrie", "Octombrie",
              "Noiembrie", "Decembrie"]
    s =  str(n)
    snm = months[int(s[3:5])]    
    return snm

def bDay():
    global n
    s =  str(n)
    snd = s[5:7]   
    return snd

def solve():
    readData()
    printData()

if __name__ == "__main__":
    solve()