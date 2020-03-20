def setup():
    size(900, 900)
def draw():
     point(50,50)
     rectMode(CORNERS)

     if mousePressed:
        circle(30, 30, 30)
        #poniższy prostokąt był rysowany zawsze, tylko w przypadku kliknięcia myszą był czyszczony.. to może lepiej rysować go tylko gdy nie klikamy myszą? Obecnie na to samo wyjdzie a mniej roboty dla programu
        rect(mouseX, mouseY, width/3*2, height/3*2)
     else:
          circle(50,60,200)
#def mouseClicked(): 
    #clear()
    #triangle(100, 300, 400, 50, 70, 100)

#generalanie ok: 1.75pkt
