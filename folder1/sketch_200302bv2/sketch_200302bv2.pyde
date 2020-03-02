def setup():
    size(900, 900)
def draw():
     point(50,50)
     rectMode(CORNERS)
     rect(mouseX, mouseY, width/3*2, height/3*2)
     if mousePressed:
         circle(30, 30, 30)
     else:
          clear()
          circle(50,60,200)
#def mouseClicked(): 
    #clear()
    #triangle(100, 300, 400, 50, 70, 100)
    
