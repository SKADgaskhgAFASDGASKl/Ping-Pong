from pygame import *
window = display.set_mode((1200,700))
display.set_caption('OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')
fon = transform.scale(image.load('1.jpg'),(1200,670))
clock = time.Clock()
game = True
class GameSprite(sprite.Sprite):
    def __init__(self,picture,x,y,w,h,speed):
        super().__init__()
        self.picture = transform.scale(image.load(picture),(w,h))
        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.picture,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 580:
            self.rect.y += self.speed
    def move2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 580:
            self.rect.y += self.speed
platforma1 = Player('3.png',20,300,50,120,10)
platforma2 = Player('3.1.png',1130,300,50,120,10 )
ball = GameSprite('2.png',550,330,70,70,5)
s_x = 5
s_y = 5
while game:
    clock.tick(60)
    window.blit(fon,(0,0))
    platforma1.move2()
    platforma1.reset()
    platforma2.move()
    platforma2.reset()
    ball.rect.x += s_x
    ball.rect.y += s_y
    if ball.rect.y >= 600:
        s_y *= -1
    if ball.rect.y <= 0:
        s_y *= -1
    if sprite.collide_rect(ball,platforma1):
        s_x *= -1
    if sprite.collide_rect(ball,platforma2):
        s_x *= -1
    ball.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
