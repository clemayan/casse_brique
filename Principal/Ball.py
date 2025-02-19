#coding=utf-8

class Ball():

    def __init__(self):# le constructeur
        self.r = 10 #attribut rayon
        self.vel = PVector(1, 1)*4 # attribut vitesse
        self.dir = PVector(1, 1) # attribut direction
        self.pos = PVector(width/2, height/2) # attribut position

    # méthode pour l'actualisation de la position
    def update(self):
        self.pos.x += self.vel.x*self.dir.x
        self.pos.y += self.vel.y*self.dir.y

    # méthode pour afficher la balle ellipse(x,y,diamètre horizontal, diamètre vertical)
    def display(self):
        #fill("#ffff64")
        fill("#ffe37e")
        
        noStroke()
        ellipse(self.pos.x, self.pos.y, self.r*2, self.r*2)

    #méthode pour les collision avec les bords
    def checkEdges(self):
        # bord droit
        if (self.pos.x > width - self.r and self.dir.x > 0):
            self.dir.x *= -1 # on change le signe de la direction
        # bord gauche
        if (self.pos.x < self.r and self.dir.x < 0):
            self.dir.x *= -1
        # bord haut
        if (self.pos.y < self.r and self.dir.y < 0):
            self.dir.y *= -1
        # bord bas
        #if (self.pos.y > height - self.r and self.dir.y > 0):
        #    self.dir.y *= -1

    # méthode pour détecter la collision avec le paddle
    # def meets(self, paddle):
    #     if (self.pos.y < paddle.pos.y and
    #         self.pos.y > paddle.pos.y - self.r and
    #         self.pos.x > paddle.pos.x - self.r and
    #         self.pos.x < paddle.pos.x + paddle.w + self.r):
    #         return True
    #     else:
    #         return False
    
    # méthode pour détecter la collision avec le paddle
    def meets(self, paddle):
        if (self.pos.y < paddle.pos.y and
            self.pos.y > paddle.pos.y - self.r and
            self.pos.x > paddle.pos.x - self.r and
            self.pos.x < paddle.pos.x + paddle.w ):
            return True
        elif self.pos.y - self.r > 300 :
            println("jgg")
        else:
            return False


    # # méthode pour que la balle casse les briques
    # def meets(self, brick):
    #     if (self.pos.y < brick.pos.y + brick.h and
    #         self.pos.y > brick.pos.y - self.r and
    #         self.pos.x > brick.pos.x - self.r and
    #         self.pos.x < brick.pos.x + brick.w + self.r):
    #         return True
    #     else:
    #         return False
        
    # méthode pour que la balle casse les briques
    
    def meets(self, brick):
        if (self.pos.y < brick.pos.y + self.r + brick.h and #changement pour que la balle ne rentre pas à l'intérieur d'une brique
            self.pos.y > brick.pos.y - self.r and
            self.pos.x > brick.pos.x - self.r and
            self.pos.x < brick.pos.x + brick.w + self.r):
            return True
        else:
            return False
