from pygame import *
window = display.set_mode((1200,700))
display.set_caption('OHHHHHHHHH')
fon = transform.scale(image.load('1.jpg'),(1200,700))
clock = time.Clock()
game = True
while game:
    clock.tick(60)
    window.blit(fon,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
