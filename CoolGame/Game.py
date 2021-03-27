# Import and initialize the pygame library
import pygame
import queue
que=queue.Queue();
pygame.init()

#set the name of game
pygame.display.set_caption("Game")


#load in character animation sprites and background from local file
#9 frames for walking right, 9 frames for walking left
#load in background picture, load in standing still animation 
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), \
             pygame.image.load('R3.png'), \
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), \
             pygame.image.load('R6.png'), pygame.image.load('R7.png'), \
             pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'),\
            pygame.image.load('L3.png'), pygame.image.load('L4.png'),\
            pygame.image.load('L5.png'), pygame.image.load('L6.png'), \
            pygame.image.load('L7.png'),\
            pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bak.png')
char = pygame.image.load('standing.png')

#change fps of game
clock = pygame.time.Clock()

#music sound track
music = pygame.mixer.music.load('creep.mp3')
pygame.mixer.music.play(-1)

#bullet sound effect and hit sound effect
bulletSound = pygame.mixer.Sound('bullet.wav')
hitSound = pygame.mixer.Sound('oof.wav')

score = 0
#create a class for player object
class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 10
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29,52)

    #method for making man walk under class player
    def draw(self,win):
        #run out of index errors, 9 sprites, 3 frame for each sprite = 27 total
        if self.walkCount + 1 >=27:
            self.walkCount = 0
        #if not standing execute frames that walk in either pointed direction 
        if not (self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount = self.walkCount + 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))

        #if character is standing to the right or left, look in the direction
        #everytime we draw the character, we move the hitbox with it
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 20, self.y, 28,60)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    #subtract from score
    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 60
        self.y = 390
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255,0,0))
        win.blit(text, (250 - (text.get_width()/2),200))
        pygame.display.update()
        i = 0
        #delaying while loop by 10 seconds
        #for loop lets us exit out of the game
        while i < 300:
            pygame.time.delay(7)
            i+=1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        i = 301
                        pygame.quit()
            
        
#create a class for bullet projectile
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = 10 * facing

    #method under projectile class that draws the actual bullet
    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

#create a class for goblin object
class enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'),\
                 pygame.image.load('R3E.png'), pygame.image.load('R4E.png'),\
                 pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),\
                 pygame.image.load('R7E.png'), pygame.image.load('R8E.png'),\
                 pygame.image.load('R9E.png'), pygame.image.load('R10E.png'),\
                 pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'),\
                pygame.image.load('L3E.png'), pygame.image.load('L4E.png'),\
                pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),\
                pygame.image.load('L7E.png'), pygame.image.load('L8E.png'),\
                pygame.image.load('L9E.png'), pygame.image.load('L10E.png'),\
                pygame.image.load('L11E.png')]
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 5
        self.hitbox = (self.x + 17, self.y+2, 31,57)
        self.health = 10
        self.visible = True

    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount +1 <= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            #draw a health bar
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,255,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - ((50/10) * (10-self.health)), 10))
            self.hitbox = (self.x + 20, self.y, 28,60)
            #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
            
            

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel*-1
                self.x += self.vel
                self.walkCount = 0

        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
                
    def hit(self):
        if self.health > 0:
            self.health -=1
        else:
            self.visible = False
        print("fugg")
        
#draw background function
def redrawGameWindow():
    win.blit(bg, (0,0))
    text = font.render('Score: ' + str(score), 1, (255,255,255))
    win.blit(text, (390,10))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()



#set window size
win = pygame.display.set_mode((500,460))


#main program

font = pygame.font.SysFont('comicsans', 30, True, True)
man = player(300,350,64,64)
bullets = []
goblin = enemy(100,395,64,64,300)
shootLoop = 0
run = True
while run:
    clock.tick(27)

    if goblin.visible == True:
    #colision between goblin and man 
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                man.hit()
                score-=5
        
    #only fire up to 3 bullets 1 at a time
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    #get a list of all the events tgat happen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    for bullet in bullets:
        #up to [3] checks to see if we are above bottom of rectangle of goblin,
        #and and after checks if we are above the top of the rectangle of the goblin.
        #bullets will only hit the goblin if the goblin is visible on the screen
        if goblin.visible:
            if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
                if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                    hitSound.play()
                    goblin.hit()
                    score+=1
                    bullets.pop(bullets.index(bullet))

        #shows the bullet going to the right and left when shot       
        if bullet.x < 500 and bullet.x > 0:
            bullet.x = bullet.x + bullet.velocity

        else:
            bullets.pop(bullets.index(bullet))
        
    #keeps track of all keys moving input
    control = pygame.key.get_pressed()

    #can only shoot after 3 are shot
    if control[pygame.K_SPACE] and shootLoop == 0:
        bulletSound.play()
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
             bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (255,160,0), facing))

        shootLoop = 1

    #change velocity so you change one variable instead of 4
    #dont want left and up, to go past velocity, right and down shouldn't go past left/down edge of rect
    if control[pygame.K_LEFT] and man.x > man.velocity:
        man.x = man.x - man.velocity
        man.left = True
        man.right = False
        man.standing = False

    elif control[pygame.K_RIGHT] and man.x < 500 - man.width - man.velocity:
        man.x = man.x + man.velocity
        man.right = True
        man.left = False
        man.standing = False

    else:
        man.standing = True
        man.walkCount = 0

    #don't allow player to jump again if already jump
    if not(man.isJump):

        if control[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False

    else:
        #this causes the object to start going up.
        if man.jumpCount >= -10:
            neg = 1
            
            #this will cause object to start falling down after you reach maxinmum/apex
            if man.jumpCount < 0:
                neg = -1
            #parabola jump - neg will cause object to fall after jumpdown reaches 0 and goes down to - 10.
            man.y = man.y - (man.jumpCount ** 2) * .5 * neg
            man.jumpCount = man.jumpCount - 1

        #makes it so no longer jumping and can go left and right again
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()
# Done! Time to quit.
pygame.quit()
