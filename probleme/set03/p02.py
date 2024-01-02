enunt = {
    "problema" : '''Ce afișează următoarele secvențe?''',
    "solutie" : ''' ''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    

def showFirst():
    for i in range(10):
        print(i, end=" ")
    print(i)  

def showSecond():
    for i in range(10):
        print(i, end=" ")
        i="ab"
        print(i, end=" ")
    print()

def showThird():
    for i in range(10):
        print(i, end=" ")
        i+=2
        print(i)
    print(i)

def solve():
    # showFirst()
    # showSecond()  
    showThird()

if __name__ == "__main__":
    solve()