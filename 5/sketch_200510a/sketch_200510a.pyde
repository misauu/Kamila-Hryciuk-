class Pilka() :
    odbicia_pilki = 0
    def __init__(self, arg_x, arg_y, arg_r):
        self.obrot =0
        self.pressed = False
        self.x = arg_x
        self.y = arg_y
        self.r = arg_r
    def rysuj(self):
        arc(self.x, self.y, self.r+100, self.r+100, 0+radians(self.obrot+90), HALF_PI+ radians(self.obrot+90), PIE)
        arc(self.x, self.y, self.r+100, self.r+100, 0+radians(self.obrot), HALF_PI+ radians(self.obrot), PIE)
        arc(self.x, self.y, self.r+100, self.r+100, 0+radians(self.obrot+180), HALF_PI+ radians(self.obrot+180), PIE)
        arc(self.x, self.y, self.r+100, self.r+100, 0+radians(self.obrot+270), HALF_PI+ radians(self.obrot+270), PIE)
        circle(self.x, self.y, self.r/2)
    def obroc(self, obrocik):
        self.obrot += obrocik
    def press(self):
        Pilka.odbicia_pilki += 1
        self.pressed = not self.pressed
        if self.pressed:
            fill(255,255, 0)
        else:
            fill(255,50,50)
            
            
def setup():
    size(400,400)
    global pilki
    p1= Pilka(width/2, height/2, 50)
    p2 = Pilka(width/4, height/4, 20) # obiekty miały być dwa
    pilki = (p1, p2) # warto je spiąć w kolekcję by późnieij nie powtarzać na każdym obiekcie wszystkich wywołań

def mouseClicked():
    pilki[0].press()
    
def mouseWheel(event):
    for pilka in pilki:
        pilka.obroc(15)
    
def draw():
    background(0,0,62)
    for pilka in pilki:
        pilka.rysuj()
    print('Odbicia pilki:',Pilka.odbicia_pilki)
    
# zmieniona została głównie graficzna reprezentacja, natomiast atrybuty i metody są kalką z mojego programu, a o kreatywność głównie na tym polu mi chodziło
# 1,25pkt
