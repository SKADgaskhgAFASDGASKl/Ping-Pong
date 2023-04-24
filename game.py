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
ball = GameSprite('4.png',550,330,70,70,100)
font.init()
font1 = font.Font(None,70)
text1 = font1.render('Победа левого игрока!!!',True,(200,30,130))
text2 = font1.render('Победа правого игрока!!!',True,(190,210,100))
s_x = 15
s_y = 15
balls1 = 0
balls2 = 0
while game:
    clock.tick(60)
    window.blit(fon,(0,0))
    platforma1.move2()
    platforma1.reset()
    platforma2.move()
    platforma2.reset()
    if balls1 <3 and balls2 <3:
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
    if ball.rect.x <= 0:
        ball.rect.x = 500
        balls2 += 1
    if ball.rect.x >= 1200:
        ball.rect.x = 500
        balls1 += 1
    if balls1 >= 3:
        window.blit(text1,(300,365))
        #game = False
    if balls2 >= 3:
        window.blit(text2,(300,365))
        #game = False
    if balls1 <3 and balls2 <3:
        ball.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
