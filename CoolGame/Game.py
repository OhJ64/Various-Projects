# Import and initialize the pygame library
import pygame
import queue
que=queue.Queue();
pygame.init()

#set the name of game
pygame.display.set_caption("Game")


#load in character animation sprites and background from local file
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), \
             pygame.image.load('R3.png'), \
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), \
             pygame.image.load('R6.png'), pygame.image.load('R7.png'), \
             pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'),\
            pygame.image.load('L3.png'), pygame.image.load('L4.png'),\
            pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'),\
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

    #method for making man walk
    def draw(self,win):
        #run out of index errors, 9 sprites, 3 frame for each sprite = 27 total
        if self.walkCount + 1 >=27:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount = self.walkCount + 1

        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))

        else:
            win.blit(char, (self.x,self.y))
        
#change fps of game
clock = pygame.time.Clock()

#set window size
win = pygame.display.set_mode((500,469))




#draw background function
def redrawGameWindow():
    #put in the background
    win.blit(bg, (0,0))
    man.draw(win)
    pygame.display.update()


#main program
man = player(300,400,64,64)
run = True
while run:
    clock.tick(27)

    #get a list of all the events tgat happen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    control = pygame.key.get_pressed()

    #change velocity so you change one variable instead of 4
    #dont want left and up, to go past velocity, right and down shouldn't go past left/down edge of rect
    if control[pygame.K_LEFT] and man.x > man.velocity:
        man.x = man.x - man.velocity
        man.left = True
        man.right = False

    elif control[pygame.K_RIGHT] and man.x < 500 - man.width - man.velocity:
        man.x = man.x + man.velocity
        man.right = True
        man.left = False

    else:
        man.right = False
        man.left = False
        man.walkCount = 0

    #don't allow player to jump again if already jump
    if not(man.isJump):

        if control[pygame.K_SPACE]:
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
# Import and initialize the pygame library
import pygame
import queue
que=queue.Queue();
pygame.init()

#set the name of game
pygame.display.set_caption("Game")


#character animation sprites and background
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), \
             pygame.image.load('R3.png'), \
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), \
             pygame.image.load('R6.png'), pygame.image.load('R7.png'), \
             pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'),\
            pygame.image.load('L3.png'), pygame.image.load('L4.png'),\
            pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'),\
            pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

#change fps of game
clock = pygame.time.Clock()

#set window size
win = pygame.display.set_mode((500,469))

x = 69
y = 369
width = 60
height = 60
velocity = 25

isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0
run = True


#draw background function
def redrawGameWindow():
    #will be changing the variable
    global walkCount
    #put in the background
    win.blit(bg, (0,0))

    #run out of index errors, 9 sprites, 3 frame for each sprite = 27 total
    if walkCount + 1 >=27:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount = walkCount + 1

    elif right:
        win.blit(walkRight[walkCount//3], (x,y))

    else:
        win.blit(char, (x,y))

    pygame.display.update()

#main program
while run:
    clock.tick(27)

    #get a list of all the events tgat happen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    control = pygame.key.get_pressed()

    #change velocity so you change one variable instead of 4
    #dont want left and up, to go past velocity, right and down shouldn't go past left/down edge of rect
    if control[pygame.K_LEFT] and x > velocity:
        x = x - velocity
        left = True
        right = False

    elif control[pygame.K_RIGHT] and x < 500 - width - velocity:
        x = x + velocity
        right = True
        left = False

    else:
        right = False
        left = False
        walkCount = 0

    #don't allow player to jump again if already jump
    if not(isJump):

        if control[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False

    else:
        #this causes the object to start going up.
        if jumpCount >= -10:
            neg = 1
            
            #this will cause object to start falling down after you reach maxinmum/apex
            if jumpCount < 0:
                neg = -1
            #parabola jump - neg will cause object to fall after jumpdown reaches 0 and goes down to - 10.
            y = y - (jumpCount ** 2) * .5 * neg
            jumpCount = jumpCount - 1

        #makes it so no longer jumping and can go left and right again
        else:
            isJump = False
            jumpCount = 10

    redrawGameWindow()
# Done! Time to quit.
pygame.quit()
# Simple pygame program

# Import and initialize the pygame library
import pygame
import queue
que=queue.Queue();
pygame.init()

#set the name of game
pygame.display.set_caption("Game")


#character animation sprites 
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

#set window size
win = pygame.display.set_mode((500,500))

x = 69
y = 369
width = 60
height = 60
velocity = 25

isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0
run = True


#draw background function
def redrawGameWindow():
    #will be changing the variable
    global walkCount
    #put in the background
    win.blit(bg, (0,0))

    #run out of index errors, 9 sprites, 3 frame for each sprite = 27 total
    if walkCount + 1 >=27:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount = walkCount + 1

    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
   

    else:
        win.blit(char, (x,y))

    pygame.display.update()

#main program
while run:
    pygame.time.delay(50)

    #get a list of all the events tgat happen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    control = pygame.key.get_pressed()

    #change velocity so you change one variable instead of 4
    #dont want left and up, to go past velocity, right and down shouldn't go past left/down edge of rect
    if control[pygame.K_LEFT] and x > velocity:
        x = x - velocity
        left = True
        right = False

    elif control[pygame.K_RIGHT] and x < 500 - width - velocity:
        x = x + velocity
        right = True
        left = False

    else:
        right = False
        left = False
        walkCount = 0

    #don't allow player to jump again if already jump
    if not(isJump):

        if control[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False

       

    else:
        #this causes the object to start going up.
        if jumpCount >= -10:
            neg = 1
            
            #this will cause object to start falling down after you reach maxinmum/apex
            if jumpCount < 0:
                neg = -1
            #parabola jump - neg will cause object to fall after jumpdown reaches 0 and goes down to - 10.
            y = y - (jumpCount ** 2) * .5 * neg
            jumpCount = jumpCount - 1

        #makes it so no longer jumping and can go left and right again
        else:
            isJump = False
            jumpCount = 10

    redrawGameWindow()
# Done! Time to quit.
pygame.quit()
