#coding=utf-8

class Brick():
    #attribut de classe un dictionnaire de couleurs
    #COLORS = {1: "#64ff96", 2: "#ff6496", 3: "#9664ff"}
    COLORS = {1: "#85d9a8", 2: "#f56991", 3: "#7c9ed9"} #nouvelles couleurs
    

    def __init__(self, x, y, hits):# le constructeur
        self.w = 75 # attribut longueur
        self.h = 20 # attribut largeur
        self.pos = PVector(x, y) # attribut position
        self.hits = hits #attribut clé pour la couleur
        self.col = Brick.COLORS[hits] # la couleur

    # méthode pour afficher la brique
    def display(self):
        fill(self.col)
        stroke("#ffffff") # couleur du bord
        strokeWeight(2)# épaisseur des bords
        rect(self.pos.x, self.pos.y, self.w, self.h)
