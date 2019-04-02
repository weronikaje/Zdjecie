
add_library('pdf')
def setup():
    size(400,400, PDF , "nowy_id_zdjecie.pdf")
    global id_foto
    id_foto = loadImage("zdjecie.jpg")
    print(type(id_foto))
    image(id_foto, 0,0, height,width)
    id_okulary = loadImage("okulary.png")
    print(type(id_okulary))
    image(id_okulary, 90,130,220,170)
    id_korona = loadImage("korona.png")
    print(type(id_korona))
    image(id_korona, 110,-20, 190,140)



def draw():
    rectMode(CENTER)
    fill(0)
    rect(195,280,30,10)
    
def draw():
    global img
    image(id_foto , 400,400)
    rectMode(CENTER)
    fill(0)
    rect(195,280,30,10)
    exit()    

    
