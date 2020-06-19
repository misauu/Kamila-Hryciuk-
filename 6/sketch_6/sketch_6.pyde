class Kwadrat():
    def __init__(self, bok): 
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
        
class PasiastyKwadrat(Kwadrat): 
    def sketchPasiasty(self, x, y, paski):
        Kwadrat.sketch(self, x, y) 
        space = self.bok/paski 
        _xLinii_ = 0 
        for pasek in range(0, paski):
            line(x+_xLinii_, y, x+_xLinii_, y+self.bok)
            _xLinii_ +=space
            
class PuszystyKwadrat(Kwadrat):
    def sketchPuszysty(self,x,y,kratka):
        Kwadrat.sketch(self, x, y)
        space = self.bok/kratka
        _xLinii_ = 0
        for linie in range(0,kratka):
            line(x+_xLinii_, y+_xLinii_, x+_xLinii_, y+self.bok)
            line(x+_xLinii_, y+_xLinii_, x+self.bok, y+_xLinii_)
            _xLinii_ +=space
        
class KociKwadrat(Kwadrat): #  :)
    def sketchKoci(self,x,y, kot):
        Kwadrat.sketch(self,x,y)
        _xLinii_ = 0
        img = loadImage( 'kot.png')
        for obrazek in range(0, kot):
            image(img, x+_xLinii_, y+_xLinii_, self.bok, self.bok)  
       
        
def setup():
    size(500, 500)
    malyKwadrat = Kwadrat(50.0) 
    malyKwadrat.sketch(200, 300)
    duzyKwadrat = Kwadrat(200.0)
    duzyKwadrat.sketch(50, 75)
    malyKwadrat.sketch(100, 200) 
    malyPasiastyKwadrat = PasiastyKwadrat(30.0) 
    malyPasiastyKwadrat.sketchPasiasty(300, 300, 5)
    malyPasiastyKwadrat.sketchPasiasty(100,300, 8) 
    duzyPasiastyKwadrat  = PasiastyKwadrat(120.0)
    duzyPasiastyKwadrat.sketchPasiasty(300, 50, 12)
    duzyPasiastyKwadrat.sketch(350, 300) 
    malyPuszystyKwadrat = PuszystyKwadrat(80.0)
    malyPuszystyKwadrat.sketchPuszysty(400,120, 20)
    duzyPuszystyKwadrat =PuszystyKwadrat(200.0)
    duzyPuszystyKwadrat.sketchPuszysty(100,270, 20)
    malyKociKwadrat = KociKwadrat(80.0)
    malyKociKwadrat.sketchKoci(220,120, 30)
    duzyKociKwadrat =KociKwadrat(150.0)
    duzyKociKwadrat.sketchKoci(100,170, 30)
    
# 2pkt
