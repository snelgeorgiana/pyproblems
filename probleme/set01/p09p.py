enunt = {
    "problema" : '''Se dau coordonatele a două puncte diferite din plan. Să se stabilească dacă dreapta
determinată de cele două puncte este orizontală, verticală sau oblică.''',
    "solutie" : '''Se evalueaza coordonatele''' 
}

def printEnunt():
    print("Enuntul Problemei:\n" + enunt["problema"]+'\n')

def printSolutia():    
    print("Enuntul Solutiei:\n" + enunt["solutie"]+'\n')
    
class CPoint:

    def __init__(self, x = 0, y = 0, name=""):
        self.x = x; self.y = y; self.name=name

    def readPointFromConsole(self):
        while True:
            sn = input(f'Enter {self.name}(x) number: ')
            try:
                self.x = float(sn)
            except:  
                print("you should input a number\n")
                continue
            break
        while True:
            sn = input(f'Enter {self.name}(y) number: ')
            try:
                self.y = float(sn)
            except:  
                print("you should input a number\n")
                continue
            break    

class CDreapta:
    
    def __init__(self, p0 = CPoint(0,0,""), p1 = CPoint(0,0,"")):
        self.p0 = p0; self.p1 = p1

    def panta(self):
        if(self.p0.x == self.p1.x and self.p0.y != self.p1.y):
            print("Deapta este verticala")
        elif(self.p0.x != self.p1.x and self.p0.y == self.p1.y):
            print("Deapta este orizontala")
        else:
            print("Dreapta este oblica")      


def solve():
    pa = CPoint(name="A"); pa.readPointFromConsole()
    pb = CPoint(name="B"); pb.readPointFromConsole()
    d = CDreapta(pa, pb)
    d.panta()

if __name__ == "__main__":
    solve()
    