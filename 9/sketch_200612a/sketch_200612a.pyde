def setup():
    size(600, 600)
    background(180)
    global img
    img = loadImage("kotek.png")
    strokeWeight(6)
    textSize(16)
 
def draw():
    rect(width/2, height/2, 200, 200)
    try:
        stroke("#0000FF")
        image(img, width/2, height/2, 200, 200)
           
    except:
        stroke("#FF0000")
        text("tu nie ma obrazka", 25, 25)
