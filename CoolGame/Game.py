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
