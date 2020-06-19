def setup():
    size(600, 600)
    background(180)
    global img
    img = loadImage("kotek.png")
    strokeWeight(6)
    textSize(16)
    noFill()
 
def draw():
    try:
        image(img, width/2, height/2, 200, 200)
    except:
        stroke("#FF0000")
        text("tu nie ma obrazka", 25, 25)
    else:
        stroke("#0000FF")
    finally:
        rect(width/2, height/2, 200, 200)
        
# 1,5pkt
