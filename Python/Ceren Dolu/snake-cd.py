import pygame
import sys
import random

class Snake():
    def __init__(self):
        self.length = 1
        self.position= [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.color = (245,245,245)
        self.score = 0
        
    def draw(self, surface):
        for p in self.position:
            rect = pygame.Rect((p[0],p[1]), (gridsize, gridsize))
            pygame.draw.rect(surface, self.color, rect)
            pygame.draw.rect(surface, (35, 61, 64), rect, 1)

    def getheadposition(self):
        return self.position[0]

    def move(self):
        currentpos= self.getheadposition()
        x,y = self.direction
        new =(((currentpos[0]+ (x*gridsize))% screen_width), (currentpos[1]+(y*gridsize))% screen_height)
        if len(self.position) > 2 and new in self.position[2:]:
            return
        else:
            self.position.insert(0,new)
            if len(self.position) > self.length:
                self.position.pop()

    def handlekeys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)


    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point
            


    def reset(self):
        self.length = 1
        self.position=([screen_width/2], [screen_height/2])
        self.direction =random.choice([up, down, left, right])
        self.score = 0


class Food():
    def __init__(self):
        self.position = (0,0)
        self.color = (249, 217, 255)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, grid_width-1)*gridsize, random.randint(0, grid_height-1)*gridsize)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (31, 54, 56), r, 1)


        
def drawGrid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x+y)%2 == 0:
                r = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface,(31, 54, 56), r)
            else:
                rr = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface, (35, 61, 64), rr)




screen_width=480
screen_height=480

gridsize=20
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize

up=(0,-1)
down= (0,1)
right=(1,0)
left=(-1,0)


def main():
    pygame.init()

    clock= pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = Snake()
    food = Food()
    myfont= pygame.font.SysFont("lato", 20)

    while True:
        clock.tick(10)
        snake.handlekeys()
        drawGrid(surface)
        snake.move()
        if snake.getheadposition() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0,0))
        text = myfont.render("Score {0}".format(snake.score), 1, (245,245,245))
        screen.blit(text, (5,10))
        pygame.display.update()
 
main()
    
