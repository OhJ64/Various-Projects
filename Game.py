# Simple pygame program

# Import and initialize the pygame library
import pygame
import queue
que=queue.Queue();
pygame.init()

#set the name of game
pygame.display.set_caption("Game")

#set window size
win = pygame.display.set_mode((500,500))

x = 250
y = 250
width = 60
height = 60
velocity = 25

isJump = False
jumpCount = 10

run = True

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
    if control[pygame.K_RIGHT] and x < 500 - width - velocity:
        x = x + velocity

    #don't allow player to jump again if already jump
    if not(isJump):
        if control[pygame.K_UP] and y > velocity:
            y = y - velocity
        if control[pygame.K_DOWN] and y < 500 - height - velocity:
            y = y + velocity

        if control[pygame.K_SPACE]:
            isJump = True
       

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

    #sets the background so that square doesn't leave a trail
    win.fill((0,0,0))

    pygame.draw.rect(win, (0,0,255), (x,y,width,height))
    pygame.display.update()
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

#set window size
win = pygame.display.set_mode((500,500))

x = 250
y = 250
width = 60
height = 60
velocity = 25

isJump = False
jumpCount = 10

run = True

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
    if control[pygame.K_RIGHT] and x < 500 - width - velocity:
        x = x + velocity

    #don't allow player to jump again if already jump
    if not(isJump):
        if control[pygame.K_UP] and y > velocity:
            y = y - velocity
        if control[pygame.K_DOWN] and y < 500 - height - velocity:
            y = y + velocity

        if control[pygame.K_SPACE]:
            isJump = True
       

    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y = y - (jumpCount ** 2) * .5 * neg
            jumpCount = jumpCount - 1

        else:
            isJump = False
            jumpCount = 10

    #sets the background so that square doesn't leave a trail
    win.fill((0,0,0))

    pygame.draw.rect(win, (0,0,255), (x,y,width,height))
    pygame.display.update()
# Done! Time to quit.
pygame.quit()
