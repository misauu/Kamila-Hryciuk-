def setup():
    size(400,400)
    textSize(70)
    background(0,0,0)
    global zaznaczenie # tak będzie czytelniej :)
    zaznaczenie = (204,0,102)
    
def draw():
    clear()
    fill(255) # biel wygląda tak samo w przestrzeni szarości jak w przestrzeni rgb
    text("K", width/2-50, height/2)
    if mouseX >= width/2-50 and mouseX<= width/2-50 +60 and mouseY >= height/2-50 and mouseY<= height/2 +20 :
        fill(*zaznaczenie)
        text("K", width/2-50, height/2)
        fill(255)
        text("H",width/2-10, height/2)
    else:
        fill(255)
        text("K", width/2-50, height/2)    
        
    print(keyPressed)
    text("H",width/2-10, height/2)
    if keyPressed:
        text("H", width/2-10, height/2)
        if key== 'H' or key=='h':
            fill(*zaznaczenie)
            text("H", width/2-10, height/2)
    else:
        fill(255)
        
    if keyPressed:
        if keyCode == LEFT:
            fill(*zaznaczenie)
            text("K", width/2-50, height/2)
            fill(255)
            text("H", width/2-10, height/2)
        if keyCode == RIGHT:
            fill(*zaznaczenie)
            text("H", width/2-10, height/2)
            fill(255)
            text("K", width/2-50, height/2)

    s= createShape()
    s.beginShape()
    s.fill(0,0,255,255)
    s.stroke(0,0,255,255)
    s.vertex(95, height/3*2)
    s.vertex(120, height/3*2-20)
    s.vertex(130, height/3*2)
    s.vertex(140, height/3*2+20)
    s.vertex(150, height/3*2+40)
    s.vertex(160, height/3*2+45)
    s.vertex(170, height/3*2-40)
    s.vertex(200, height/3*2-40)
    s.vertex(210, height/3*2+45)
    s.vertex(220, height/3*2+40)
    s.vertex(230, height/3*2+20)
    s.vertex(240, height/3*2)
    s.vertex(250, height/3*2-20)
    s.vertex(275, height/3*2)
    s.endShape(CLOSE)
    shape(s,25,25)
    
# jeszcze taki mankament, że wciśnięcie samych strzałek, bez zaznaczonej litery też działa, a nie powinno
# 1,75p
