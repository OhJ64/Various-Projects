
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
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')


#create a class for player object
class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 15
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True

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
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))

#create a class for bullet projectile
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = 12 * facing

    #method under projectile class that draws the actual bullet
    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

        
#change fps of game
clock = pygame.time.Clock()

#set window size
win = pygame.display.set_mode((500,469))


#draw background function
def redrawGameWindow():
    #put in the background
    win.blit(bg, (0,0))
    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


#main program
man = player(300,400,64,64)
bullets = []
run = True
while run:
    clock.tick(27)

    #get a list of all the events tgat happen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x = bullet.x + bullet.velocity

        else:
            bullets.pop(bullets.index(bullet))
        
    #keeps track of all keys moving input
    control = pygame.key.get_pressed()

    if control[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
             bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))

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
