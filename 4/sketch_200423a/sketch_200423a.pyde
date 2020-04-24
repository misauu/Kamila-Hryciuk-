add_library('pdf')

def setup():
    global img
    size(350,400)
    img= loadImage("twarz.png")
    beginRecord(PDF, "outtwarz.pdf")
    

    print(type(img))
    
    
def draw():
    global img
    image(img, 0,0, height-50, width+50) #tylko w ten sposób obraz ustawiał się w pełnym ekranie
    
    
    
    s = createShape()
    s.beginShape()
    s.fill(255, 255, 0)
    s.stroke(255, 255, 0)
    s.vertex(30, height/4)
    s.vertex(280, height/4)
    s.vertex(280, height/4-100)
    s.vertex(245, height/4-50)
    s.vertex(210, height/4-100)
    s.vertex(175, height/4-50)
    s.vertex(140, height/4-100)
    s.vertex(105, height/4-50)
    s.vertex(70, height/4-100)
    s.vertex(45, height/4-50)
    s.vertex(30, height/4-100)
    s.endShape(CLOSE)
    shape(s, 25, 25)
    
    
    if keyPressed:
        if keyCode == RIGHT:
            clear()
            image(img, 0,0, height-50, width+50)
            c = createShape()
            c.beginShape()
            c.fill(0,0,0)
            c.stroke(0,0,0)
            c.vertex(40, height/3+20)
            c.vertex(260, height/3+20)
            c.vertex(260, height/3+50)
            c.vertex(200, height/3+60)
            c.vertex(180, height/3+60)
            c.vertex(160, height/3+50)
            c.vertex(160, height/3+20)
            c.vertex(140, height/3+20)
            c.vertex(140, height/3+50)
            c.vertex(120, height/3+60)
            c.vertex(100, height/3+60)
            c.vertex(40, height/3+50)
            c.vertex(40, height/3+20)
            c.endShape(CLOSE)
            shape(c, 25, 25)
    
    endRecord()
                    
   
