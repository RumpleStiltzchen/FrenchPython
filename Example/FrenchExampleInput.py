
de math importe dist
importe pygame
importe sys
importe random


width = 1280
height = 720
#set title of window to "Solo Pong: You're alone"
pygame.display.set_caption("Solo Pong: You're alone")

#load et set window icon
icon = pygame.image.load('Icon.png')
pygame.display.set_icon(icon)

score = 0

classe Main:
    def __init__(self):
        self.score = 0
    def drawScore(self):
        #cast score int to string
        score_text = str(self.score) 
        #create surface pour the scores shadow et set its position
        Shadow_surface = game_font.render(score_text,Vrai, (51, 51, 51))
        Shadx = int(65)
        Shady = int(45)
        #create a rectangle pour the shadow to sit inside of, et paste it on the screen avec screen.blit
        Shadow_rect = Shadow_surface.get_rect(center = (Shadx, Shady))
        
        screen.blit(Shadow_surface, Shadow_rect)
        #do the exact same steps but offset by -5px to create a dropshadow 
        score_text = str(self.score) 
        score_surface = game_font.render(score_text,Vrai, (255, 255, 255))
        scorex = int(60)
        scorey = int(40)
        score_rect = score_surface.get_rect(center = (scorex, scorey))
        screen.blit(score_surface, score_rect)



    def update(self):
        # si score est even, set window title to ping. Else set to Pong
        si self.score == 0:
            passeeee
        sinon:
            si self.score % 2 == 0:
                pygame.display.set_caption('ping')
                
                
            sinon:
                pygame.display.set_caption('pong')

classe Paddle:
    
    def __init__(self):
        self.left = Faux
        self.right = Faux
        self.w = 200
        self.h = 40
        self.x = width / 2 - self.w / 2
        self.y = height / 5 * 4
        
        self.speed = 5
        
    def update(self):


        si self.left:
            self.x -= self.speed
        si self.right:
            self.x += self.speed

        si self.x > 1080:
            self.x = 1080
            self.right = Faux
        si self.x < 0:
            self.x = 0
            self.left = Faux
        

    def draw(self):
        ShadowRect = pygame.Rect(self.x + 5, self.y + 5, self.w, self.h)
        pygame.draw.rect(screen, (51, 51, 51), ShadowRect, 5)
        PaddleRect = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(screen, (255, 255, 255), PaddleRect, 5)
        
        
classe Ball:
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
        
        

        si self.x > pad.x et self.x < pad.x + pad.w:
            si self.y + self.R > pad.y et self.y < pad.y + pad.h:
                si self.y + self.R < pad.y et self.y > pad.y + pad.h:
                    self.y = pad.y
                    
                sinon:
                    self.vy *= -1 
                    main.score += 1
                    self.RandPhysics(pad)
                    self.vx *= dist((self.x, self.y), (pad.x + pad.w / 2, pad.y)) / 40
                    si self.vx < 0 et self.x > pad.x + 2 * (pad.w / 3):
                        self.vx *= -1
                    si self.vx > 0 et self.x < pad.x + pad.w / 3:
                        self.vx *= -1
                     
        si self.y > height - self.R:
            self.y = height - self.R


        self.ay += self.G

        self.vx += self.ax
        self.x += self.vx  
        self.vy += self.ay
        self.y += self.vy   
        
        si self.vy > 4:
            self.vy = 4
        si self.vx > 5:
            self.vx = 5

        si self.x < 0:
            self.x = 0
            self.vx *= -1
            self.RandPhysics(pad)
        si self.x > width - self.R:
            self.x = width - self.R
            self.vx *= -1
            self.RandPhysics(pad)
        si self.y < 0:
            self.RandPhysics(pad)
            self.y = 0
            self.vy *= -1

        self.ax = 0
        self.ay = 0

        si self.y > pad.y + pad.h * 3:
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
        si rand == 1:
            self.G = 0.03
        sinon:
            self.G = 0
        self.PlayRandSound()
    def PlayRandSound(self):
        rand = random.randrange(0, 3)
        si rand == 0:
            self.LoB.play()
        si rand == 1:
            self.MiB.play()
        si rand == 2:
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
pendant Vrai:
    screen.fill(BGcolor)    
    pour event dans pygame.event.get():
        si event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
        si event.type == pygame.KEYDOWN:
            si event.key == pygame.K_LEFT:
                paddle.left = Vrai
            si event.key == pygame.K_RIGHT:
                paddle.right = Vrai

        si event.type == pygame.KEYUP:
            si event.key == pygame.K_LEFT:
                paddle.left = Faux
            si event.key == pygame.K_RIGHT:
                paddle.right = Faux

    
    ball.update(paddle, main)
    ball.draw()
    
    paddle.update()
    paddle.draw()
    
    main.update()
    main.drawScore()
    
    pygame.display.update()
    clock.tick(framerate)

