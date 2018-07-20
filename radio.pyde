def setup():
    size(400, 400)
    background(128, 56, 40)
    fill(181, 166, 66)
    ellipse(75, 325, 50, 50)
    triangle(75, 325, 100, 355, 110, 355)
    fill(255, 255, 255)
    rect (100, 0, 200, 50)
    rect( 100, 50, 200, 50)
    stations={"97.9":"old school hip hop",
             "v103":"hip hop",
             "102.5":"gospel",
             "kiss 104.1":"r&b",
             }
    value=0
#def draw(): 
    #print("hello")
    #fill(181, 166, 66)
   # triangle(75, 325, 100, 355, 110, 355)
    #ellipse(75, 325, 50, 50)
def mouseClicked():
    fill(0)
    if mouseX>75 and mouseY<325:
        text("97.9",100,25)
    elif mouseX<75 and mouseY<325:
        text("v103",10,30)
    
    #for Station in Stations:
       # if 
    #text(station)
    
