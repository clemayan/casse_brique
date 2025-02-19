from __future__ import unicode_literals  #pour utiliser unicode et donc les accents et caracteres speciaux 
from Paddle import Paddle #import de la classe Paddle
from Ball import Ball #import de la classe Ball
from Brick import Brick #import de la classe Brick

playingGame = False
bricks = []  #création de la lste
score = 0 #initialisation du score à 0
vies = 3 #initialisation à 3 vies
niv = 1 #on initialise le niveau à 1
triche = False

#bouton start
overBox = False
xOffset = 0.0
yOffset = 0.0

def setup():
    global paddle, ball, police, bx, by # on déclare les variables comme globales
    size(605,400)
    police = createFont("SynchroLET",64) #changement de la police
    #println(PFont.list())
    paddle = Paddle() # on crée l'objet paddle
    ball = Ball()# on crée l'objet ball
    
    #position du bouton
    bx = 260
    by = 250

    # appel de la fonction addBrick pour ajouter la première ligne de briques et enlever les anciennes
    for x in range (len(bricks)-1,-1,-1):  #parcourt liste des briques à l'envers
        bricks.pop(x)
    for x in range (5, width - 80, 75):
        addBrick(x + 37.5, 90, 1) 
    #ball.vel *= 1.2 

def draw():
    background(0,0,0)
    global score, vies, playingGame, niv, triche, overBox
    
    #souris sur le bouton start
    if bx - 80 < mouseX < bx + 80 and \
       by - 80< mouseY < by + 80:
        overBox = True
    else:
        stroke(153)
        fill(153)
        overBox = False
        
    #création du bouton start    
    rect(bx,by,80,80)
    fill (255,255,255)
    stroke(255)
    triangle(280,270,320,290,280,310)

    if playingGame :
        background(0) #cache le bouton start
    
    #affichage des informations lors de la partie
    textFont(police)
    textSize(20)
    fill(250)
    textAlign(LEFT)
    #if score < 0: #le score ne peut pas être négatif
    #    score = 0
    text("Score : "+str(score),12,30) #affichage du score du joueur

    textAlign(RIGHT)
    text("Vies : "+str(vies),597,30) #affichage des vies restantes

    textAlign(CENTER)
    text("Niveau "+str(niv),302.5,30) #affichage du niveau actuel
    
    
    #appel des méthodes pour le paddle
    paddle.display()
    if playingGame:
        paddle.checkEdges()
        paddle.update()
        
    #appel des méthodes pour la balle
    ball.display()
    if playingGame:
        ball.checkEdges()
        ball.update()
    if (ball.meets(paddle)): #contact entre la balle et le socle
        if (ball.dir.y > 0):
            ball.dir.y *= -1

    for i in range (len(bricks)):
        bricks[i].display()
    for i in range (len(bricks)-1,-1,-1):  #parcourt liste des briques à l'envers
        if (ball.meets(bricks[i])):  #si collision détectée
        
            if bricks[i].hits == 3:  #la brique touchée est violette donc il faut 3 coups pour la détruire
                bricks[i].col = Brick.COLORS[2] # la couleur change pour rose
                bricks[i].hits = 2
                #score = score + 5
                ball.dir.y*=-1
                
            elif bricks[i].hits == 2:  #la brique touchée est rose donc il faut 2 coups pour la détruire
                bricks[i].col = Brick.COLORS[1] # la couleur change pour vert
                bricks[i].hits = 1
                #score = score + 5
                ball.dir.y*=-1

            else:  #la brique touchée est vert donc il faut 1 coup pour la détruire
                score = score + 10
                bricks.pop(i)  #sup brique touchée
                #del bricks[i]
                ball.dir.y*=-1
            
   
    if ball.pos.y > 400 and len(bricks) != 0: #si la balle ne se trouve plus dans la fenetre, le joueur perd une vie
        vies = vies - 1
        #score = score - 20
        textSize(20)
        fill(250)
        textAlign(RIGHT)
        text(str(vies),600,30) #affiche le nombre de vie restante
        
        paddle.pos = PVector(width/2 - paddle.w/2, height - 40)#retour du paddle au centre de l'écran
        ball.pos = PVector(width/2, height/2) #retour de la balle au centre de l'écran
        playingGame = False
        
    
    if vies <= 0: #le joueur n'a plus de vie
        background(255,100,80) #changement de couleur du fond
        textSize(76)
        fill(250)
        textAlign(CENTER)
        text("Perdu !",302.5,170)
        textSize(20)
        if score == 0:
            text("Vous avez perdu au niveau "+str(niv)+" avec "+str(score)+" point",300,220) #affichage du score et du niveau à la fin de la partie avec aucun point
        else:
            text("Vous avez perdu au niveau "+str(niv)+" avec "+str(score)+" points",300,220) #affichage du score et du niveau à la fin de la partie
        
        if triche == True:
            textSize(18)
            text("en trichant :)",500,250) #affichage disant que la personne a triché en utilisé les fleches pour augmenter de niveaux
        
        #affiche le bouton restart
        fill(0,0,0,125)
        rect(260,270,80,80)
        fill (255,255,255)
        noStroke()
        triangle(280,290,320,310,280,330)
        
        #retour au menu pour jouer lorsque le joueur clique sur le bouton
        if playingGame:
            vies = 3
            niv = 1
            score = 0
            setup()
            playingGame = False


    
    if len(bricks) == 0: #le joueur a détruit toutes les briques du niveau
        background(152,190,100) #changement de couleur du fond
        textSize(76)
        fill(250)
        textAlign(CENTER)
        text("Gagné !",302.5,180)
        #text(u"Gagné !",302.5,180)  # autre syntaxe si  la premiere ligne n'est pas ajoutee 
        textSize(46)
        text("Niveau superieur !",302.5,230)
        textSize(20)
        text("Cliquer sur la touche 'ENTER' pour afficher le niveau",302.5,280) #permet de changer de fond

    #chag avec touche entrer
        if key == ENTER  : #la touche ENTER permet d'afficher le nouveau niveau
            playingGame = False
            paddle.pos = PVector(width/2 - paddle.w/2, height - 40)#retour du paddle au centre de l'écran
            ball.pos = PVector(width/2, height/2) #retour de la balle au centre de l'écran
            niv = niv + 1 #augmentation du niveau
            ball.vel *= 1.01**niv #la vitesse de la balle dépend du niveau atteind
            #println(ball.vel)
            niveau()


#augmenter manuellement les niveaux : bug parfois sur le contact entre la balle et les briques
    if keyCode==UP: #la fleche du haut permet de changer de niveau manuellement
        niv = niv + 1 #augmentation du niveau
        triche = True
        playingGame = False
        niveau()
        ball.vel *= 1.01**niv #la vitesse de la balle dépend du niveau atteind
        #println(ball.vel)
        delay(900)
        
    # elif keyCode==DOWN: #la fleche du bas permet de changer de niveau manuellement
    #     playingGame = False
    #     niv = niv - 1 #diminuation du niveau
    #     triche = True
    #     niveau()   
    #     delay(900)
        

def niveau():
    println("niveau")
    println(niv)
    if niv == 2:
        for x in range (5, width - 80, 75):  #affichage de 2 lignes de briques
            addBrick(x + 37.5, 90, 1)
            addBrick(x + 37.5, 70, 2)
        ball2 = Ball()
    
    if niv == 3:
        for x in range (5, width - 80, 75): #affichage de 3 lignes de briques
            addBrick(x + 37.5, 90, 1)
            addBrick(x + 37.5, 70, 2)
            addBrick(x + 37.5, 50, 3)
        
    if niv >= 4 : # à partir du niveau 4 seule la vitesse change
        for x in range (5, width - 80, 75):
            addBrick(x + 37.5, 90, 1)
            addBrick(x + 37.5, 70, 2)
            addBrick(x + 37.5, 50, 3)
        paddle.w = 80 #la taille de la raquette diminue
              
# fonction créant et stockant les briques dans la liste
def addBrick(x, y, hits): #hits permet de definir la couleur de la brique
    brick = Brick(x, y, hits)
    bricks.append(brick)
    #println(bricks)

# détection des mouvements touches <- et ->
def keyPressed():
    if keyCode==LEFT:
        paddle.isMovingLeft = True #la touche fleche gauche du clavier fait bouger le socle à gauche
    elif keyCode==RIGHT: 
        paddle.isMovingRight = True #la touche fleche droite du clavier fait bouger le socle à droite


#annulation des mouvements quand on relâche la touche
def keyReleased(): #tant qu'on maintient enfoncé la touche, le socle continu d'avancer
    paddle.isMovingRight = False
    paddle.isMovingLeft = False

#clic bouton start
def mousePressed():
    global xOffset, yOffset,playingGame
    if overBox: #la souris est sur le bouton
        playingGame = True
        println(playingGame)

    xOffset = mouseX - bx
    yOffset = mouseY - by
    
    delay(500) #temps de flottement avanat le début du jeu
