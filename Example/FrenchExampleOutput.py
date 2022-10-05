from math import dist
import pygame
import sys
import random


width = 1280
height = 720
#set title of window to "Solo Pong: You're alone"
pygame.display.set_caption("Solo Pong: You're alone")

#load and set window icon
icon = pygame.image.load('Icon.png')
pygame.display.set_icon(icon)

score = 0

class Main:
    def __init__(self):
        self.score = 0
    def drawScore(self):
        #cast score int to string
        score_text = str(self.score) 
        #create surface for the scores shadow and set its position
        Shadow_surface = game_font.render(score_text,True, (51, 51, 51))
        Shadx = int(65)
        Shady = int(45)
        #create a rectangle for the shadow to sit inside of, and paste it on the screen with screen.blit
        Shadow_rect = Shadow_surface.get_rect(center = (Shadx, Shady))
        
        screen.blit(Shadow_surface, Shadow_rect)
        #do the exact same steps but offset by -5px to create a dropshadow 
        score_text = str(self.score) 
        score_surface = game_font.render(score_text,True, (255, 255, 255))
        scorex = int(60)
        scorey = int(40)
        score_rect = score_surface.get_rect(center = (scorex, scorey))
        screen.blit(score_surface, score_rect)



    def update(self):
        # if score is even, set window title to ping. Else set to Pong
        if self.score == 0:
            pass
        else:
            if self.score % 2 == 0:
                pygame.display.set_caption('ping')
                
                
            else:
                pygame.display.set_caption('pong')

class Paddle:
    
    def __init__(self):
        self.left = False
        self.right = False
        self.w = 200
        self.h = 40
        self.x = width / 2 - self.w / 2
        self.y = height / 5 * 4
        
        self.speed = 5
        
    def update(self):


        if self.left:
            self.x -= self.speed
        if self.right:
            self.x += self.speed

        if self.x > 1080:
            self.x = 1080
            self.right = False
        if self.x < 0:
            self.x = 0
            self.left = False
        

    def draw(self):
        ShadowRect = pygame.Rect(self.x + 5, self.y + 5, self.w, self.h)
        pygame.draw.rect(screen, (51, 51, 51), ShadowRect, 5)
        PaddleRect = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(screen, (255, 255, 255), PaddleRect, 5)
        
        
class Ball:
    def __init__(self, x, y, ax, ay,r):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.ax = ax
        self.ay = ay
        self.G = 0.03
        self.R = r

        self.HiB = pygame.mixer.Sound('bounceHigh.wav')
        self.MiB = pygame.mixer.Sound('BounceMid.wav')
        self.LoB = pygame.mixer.Sound('BounceLow.wav')
        self.Lose = pygame.mixer.Sound('Lose.wav')
    def update(self, pad, main):
        
        

        if self.x > pad.x and self.x < pad.x + pad.w:
            if self.y + self.R > pad.y and self.y < pad.y + pad.h:
                if self.y + self.R < pad.y and self.y > pad.y + pad.h:
                    self.y = pad.y
                    
                else:
                    self.vy *= -1 
                    main.score += 1
                    self.RandPhysics(pad)
                    self.vx *= dist((self.x, self.y), (pad.x + pad.w / 2, pad.y)) / 40
                    if self.vx < 0 and self.x > pad.x + 2 * (pad.w / 3):
                        self.vx *= -1
                    if self.vx > 0 and self.x < pad.x + pad.w / 3:
                        self.vx *= -1
                     
        if self.y > height - self.R:
            self.y = height - self.R


        self.ay += self.G

        self.vx += self.ax
        self.x += self.vx  
        self.vy += self.ay
        self.y += self.vy   
        
        if self.vy > 4:
            self.vy = 4
        if self.vx > 5:
            self.vx = 5

        if self.x < 0:
            self.x = 0
            self.vx *= -1
            self.RandPhysics(pad)
        if self.x > width - self.R:
            self.x = width - self.R
            self.vx *= -1
            self.RandPhysics(pad)
        if self.y < 0:
            self.RandPhysics(pad)
            self.y = 0
            self.vy *= -1

        self.ax = 0
        self.ay = 0

        if self.y > pad.y + pad.h * 3:
            self.x = 640
            self.y = 360
            self.vx = 2
            self.vy = 0
            self.R = 20
            self.G = 0.03
            main.score = 0
            pygame.display.set_caption("You're bad")
            self.Lose.play()

    def RandPhysics(self, pad):
        rand = random.randrange(0, 2)
        if rand == 1:
            self.G = 0.03
        else:
            self.G = 0
        self.PlayRandSound()
    def PlayRandSound(self):
        rand = random.randrange(0, 3)
        if rand == 0:
            self.LoB.play()
        if rand == 1:
            self.MiB.play()
        if rand == 2:
            self.HiB.play()
        
        


    def draw(self):
        ShadowRect = pygame.Rect(self.x + 5, self.y + 5, self.R, self.R)
        pygame.draw.ellipse(screen, (51, 51, 51), ShadowRect, 5)
        BallRect = pygame.Rect(self.x, self.y, self.R, self.R)
        pygame.draw.ellipse(screen, (255, 255, 255), BallRect, 5)
        
    



framerate = 144
BGcolor = (150,150,150)

pygame.init()

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


game_font = pygame.font.Font(None, 80)

main = Main()

paddle = Paddle() 

ball = Ball(640, 360, random.randrange(-4, 4), -5, 20)
while True:
    screen.fill(BGcolor)    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle.left = True
            if event.key == pygame.K_RIGHT:
                paddle.right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                paddle.left = False
            if event.key == pygame.K_RIGHT:
                paddle.right = False

    
    ball.update(paddle, main)
    ball.draw()
    
    paddle.update()
    paddle.draw()
    
    main.update()
    main.drawScore()
    
    pygame.display.update()
    clock.tick(framerate)

