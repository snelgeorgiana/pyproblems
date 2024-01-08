enunt = {
    "problema" : '''Fie şirul s="petrecere". Scrieţi felieri astfel încât să obţineţi valorile: "cere", "eee", "rece".''',
    "solutie" : ''' ''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
s = ""
def readData():
    global s
    s = "petrecere"

def testString(s):
    print(f"s = {s}")
    # cere
    print(f"\ns[5:] = {s[5:]}")
    print(f"s[5:9] = {s[5:9]}")
    print(f"s[5:len(s)] = {s[5:len(s)]}")
    print(f"s[-4:] = {s[-4:]}")
    print(f"s[len(s)-4:len(s)] = {s[len(s)-4:len(s)]}")
    print(f"s[s[-4:0:-1].replace('t','')] = {s[-4:0:-1].replace('t','')}")
    print()
    # eee
    print(f"s[4::2] = {s[4::2]}")
    print(f"s[-1:-6:-2] = {s[-1:-6:-2]}")
    print()
    #rece
    print(f"s[3:7] = {s[3:7]}")
    print(f"s[-6:-2] = {s[-6:-2]}")
    print(f"s[::-1] = {s[-2:-6:-1]}")
    print()

def solve():
    readData()
    testString(s)

if __name__ == "__main__":
    solve()