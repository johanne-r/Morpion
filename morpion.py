class Case:
    def __init__(self):
        self.occupe = " "

    def jouer1(self):
        if (self.occupe == " "):
            self.occupe = "X"
    
    def jouer2(self):
        if (self.occupe == " "):
            self.occupe = "O"
    
class Terrain:
    def __init__(self):
        self.grille = [Case() for i in range(9)]
        self.tour = 1

    def __str__(self):
        print(self.grille[0].occupe," | ", self.grille[1].occupe," | " ,self.grille[2].occupe,"\n")
        print(self.grille[3].occupe," | ", self.grille[4].occupe," | ",self.grille[5].occupe,"\n")
        print(self.grille[6].occupe," | ",self.grille[7].occupe," | ", self.grille[8].occupe,"\n")
        
    def jouer(self, i):
        if (self.grille[i].occupe == " "):
            if self.tour == 1:
                self.grille[i].jouer1()
                self.tour = 2
            else:
                self.grille[i].jouer2()
                self.tour = 1

partie = Terrain()
partie.jouer(3)
partie.jouer(2)
partie.jouer(4)
partie.jouer(6)
partie.jouer(5)
partie.__str__()