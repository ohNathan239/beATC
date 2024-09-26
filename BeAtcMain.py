import pygame

screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

class Plane(pygame.Rect):
    def __init__(self, x, y, vx, vy):
        super().__init__(x,y,50,50)
        self.vx = vx
        self.vy = vy
    def update(self):
        self.x+=self.vx
        self.y += self.vy
        self.draw()

    def draw(self):
        pygame.draw.rect(screen, 'white', self)#TODO: draw a sprite

class RoadWay():
    def __init__(self, startX, startY, endX, endY):
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY
    def draw(self):
            pygame.draw.rect(screen,'grey', self, 0)

class TaxiWay(RoadWay):
    def __init__(self, startX, startY, endX, endY):
        super().__init__(startX, startY, endX, endY)
class RunWay(RoadWay):
    def __init__(self, startX, startY, endX, endY):
        super().__init__(startX, startY, endX, endY)

while True:
    #Process player inputs:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    #Do logical updates here:

    #Update graphics here:
    screen.fill("white")

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)