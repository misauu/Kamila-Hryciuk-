# to na prawdę ładny robaczek :)

def setup():
    size( 500, 600)
    global x
    global y
    global wayx
    global wayy
    wayy=10
    wayx=10
    x=250
    y=300
    frameRate(10)
    #global slownik
    global natezenie
    natezenie= 0 
    #slownik = {"różowy": (255,144,99), "niebieski":(108,88,214), "fioletowy":(209,137,214), "pomarańczowy":(209,137,9)}
def draw():
    global natezenie 
    global x
    global y
    global wayx 
    global wayy
    x= x+ wayx
    if x >width:
        wayx=-10
    if x<0:
        wayx=10
    y=y+ wayy
    if y>height:
        wayy=-10
    if y<0:
        wayy=10
        
#    kolory = ((255,44,99), (108,88,214),(209,137,214), (209,137,9))
    noStroke()
    fill(natezenie, random(255), random(255))
    natezenie= natezenie +1
    if(natezenie ==255):
        natezenie= 0
    circle(x, y,100)
    
    if mousePressed:
        exit()
 
# kolory de facto z randoma, nie użyłaś stworzonych tablic
# 1,5pkt
