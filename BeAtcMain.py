import pygame
import math

screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

TYPES = ["Runway", "Taxiway", "Hangar"]
class Branch():
    def __init__(self, type, name):
        self.type = type
        self.name = name
branches = []

class Intersection:
    def __init__(self, x, y, branch1, branch2):
        self.x = x
        self.y = y
        self.branch1 = branch1
        self.branch2 = branch2
    def __str__(self):
        return "b1: " + self.branch1 + "   b2: " + self.branch2
intersections = []

class Plane(pygame.Rect):
    TAXI_SPEED = 6
    def __init__(self, int1):
        super().__init__(int1.x,int1.y,50,50)
        self.x = int1.x
        self.y = int1.y
        self.vx = 0
        self.vy = 0
        self.inter = int1
        self.pathfinding = False
        self.path_to_take = []
    def set_vel(self, int2):
        dx = int2.x - self.inter.x
        dy = int2.y - self.inter.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance > 0:
            self.vx = Plane.TAXI_SPEED * (dx / distance)
            self.vy = Plane.TAXI_SPEED * (dy / distance)
        else:
            self.vx = 0
            self.vy = 0
    def update(self):
        if self.pathfinding:
            current_index = self.path_to_take.index(self.inter)
            if(self.intersects(self.path_to_take[current_index+1])):
                self.inter = self.path_to_take[current_index+1]
                current_index = self.path_to_take.index(self.inter)
                if current_index == len(self.path_to_take)-1:
                    self.pathfinding = False
                    self.set_vel(self.path_to_take[current_index])
                    print("stopped!")
                    return
            self.set_vel(self.path_to_take[current_index+1])
            #print("this triggered")
        self.x+=self.vx
        self.y += self.vy
        self.draw()
    def draw(self):
        my_rect = pygame.Rect(self.x-25,self.y-25,50,50)
        pygame.draw.rect(screen, 'grey', my_rect)#TODO: draw a sprite
    def intersects(self, nextInt):
        dx = nextInt.x - self.x
        dy = nextInt.y - self.y
        distSquared = dx**2 + dy**2
        if(distSquared <= 10):
            return True
        return False
    def parse_string(self, input_string):
        branchNames = input_string.split() #The user should enter a string of taxiway and runway names separated by spaces
        print(branchNames)
        is_valid = True
        for name in branchNames:#loop through each name entered
            char_is_valid = False
            for path in branches:#check if the name entered is in the list of valid branch names
                if name == path.name:
                    char_is_valid = True
            if not char_is_valid:
                is_valid = False
        if not is_valid:
            return False  #Everything works up to here
        path_to_take = []
        path_to_take.append(self.inter)
        for firstInt in intersections:
            if (firstInt.branch1.name == self.inter.branch1.name and firstInt.branch2.name == branchNames[0]) or (firstInt.branch2.name == self.inter.branch1.name and firstInt.branch1.name == branchNames[0]):
                branchNames.insert(0,self.inter.branch1.name)
            else:
                branchNames.insert(0,self.inter.branch2.name)
        is_valid = False
        for x in range(0, len(branchNames)-1):
            for inter in intersections:
                if ((inter.branch1.name == branchNames[x] and inter.branch2.name == branchNames[x+1]) or (inter.branch2.name == branchNames[x] and inter.branch1.name == branchNames[x+1])):
                    print("how many times did this trigger?")
                    is_valid = True
                    path_to_take.append(Intersection(inter.x, inter.y, inter.branch1, inter.branch2))
        if is_valid:
            print("works")
            return path_to_take
        return False
    def pathfind(self, input_string):
        self.path_to_take = self.parse_string(input_string)
        print(self.path_to_take)
        if self.path_to_take == False:
            print("invalid string")
            return
        self.pathfinding = True
        return

while True:
    #Process player inputs:
    #path_string = input("")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    #Do logical updates here:

    #Update graphics here:
    screen.fill("white")
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)