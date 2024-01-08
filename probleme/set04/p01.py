enunt = {
    "problema" : '''Ce valoare au pentru șirul s= "acest exemplu" felierile: s[0:4], s[0:4:2], s[0:4:-2], s[0::2],
s[::100], s[::-100], s[-3:-1], s[-1:4], s[-12:4], s[len(s):]? Cum se poate accesa prin feliere
subsecvența “exe” folosind indici pozitivi? Dar folosind indici negativi?''',
    "solutie" : '''s[6:9] ; s[-8:-4]''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
s=""
def readData():
    global s
    s="acest exemplu"

def testString(s):
    print(f"s = {s}")
    print(f"len(s) = {len(s)}")
    print(f"s[0:4] = {s[0:4]}")
    print(f"s[0:4:2] = {s[0:4:2]}")
    print(f"s[0:4:-2] = {s[0:4:-2]}")
    print(f"s[4:0:-2] = {s[4:0:-2]}")
    print(f"s[4:0] = {s[4:0]}")
    print(f"s[4:0:-1] = {s[4:0:-1]}")
    print(f"s[0::2] = {s[0::2]}")
    print(f"s[::-1] = {s[::-1]}")
    print(f"s[::-2] = {s[::-2]}")
    print(f"s[::-3] = {s[::-3]}")
    print(f"s[::-12] = {s[::-12]}")
    print(f"s[::-13] = {s[::-13]}")
    print(f"s[::-14] = {s[::-14]}")
    print(f"s[::-100] = {s[::-100]}")
    print(f"s[-1::] = {s[-1::]}")
    print(f"s[-3:-1] = {s[-3:-1]}")
    print(f"s[-3:0] = {s[-3:0]}")
    print(f"s[-1:4] = {s[-1:4]}")
    print(f"s[-12:4] = {s[-12:4]}")
    print(f"s[len(s):] = {s[len(s):]}")
    print(f"s[-len(s):] = {s[-len(s):]}")
    print(f"s[len(s)::-1] = {s[len(s)::-1]}")
    print(f"s[6:9] = {s[6:9]}")
    print(f"s[-8:-4] = {s[-8:-4]}")

def solve():
    readData()
    testString(s)

if __name__ == "__main__":
    solve()