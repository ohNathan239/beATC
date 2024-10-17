import pygame
import math

clock = pygame.time.Clock()
image = pygame.image.load("file.png")
screen = pygame.display.set_mode((image.get_width(),image.get_height()))

TYPES = ["Runway", "Taxiway", "Hangar"]
class Branch():
    def __init__(self, type, name):
        self.type = type
        self.name = name
branches = []
A = Branch(TYPES[2],'A')
branches.append(A)
C = Branch(TYPES[2],'C')
branches.append(C)
D = Branch(TYPES[2],'D')
branches.append(D)
E = Branch(TYPES[2],'E')
branches.append(E)
F = Branch(TYPES[2],'F')
branches.append(F)
G = Branch(TYPES[2],'G')
branches.append(G)
FBO = Branch(TYPES[1],"FBO")
branches.append(FBO)
Hangar = Branch(TYPES[1],"Hangar")
branches.append(Hangar)
R1 = Branch(TYPES[0],"R1")
branches.append(R1)
R2 = Branch(TYPES[0],"R2")
branches.append(R2)
R3 = Branch(TYPES[0],"R3")
branches.append(R3)
R4 = Branch(TYPES[0],"R4")
branches.append(R4)
e1 = Branch(TYPES[2], "e1")
e2 = Branch(TYPES[2], "e2")


class Intersection:
    def __init__(self, x, y, branch1, branch2):
        self.x = x
        self.y = y
        self.branch1 = branch1
        self.branch2 = branch2
    def __str__(self):
        return "b1: " + self.branch1.name + "   b2:" + self.branch2.name
intersections = []
intersections.append(Intersection(766,72,A,C))
intersections.append(Intersection(572,307,D,C))
intersections.append(Intersection(360,560,F,C))
intersections.append(Intersection(406,627,E,G))
intersections.append(Intersection(470,435,C,FBO))
intersections.append(Intersection(744,114,C,Hangar))
intersections.append(Intersection(312,620,C,E))
intersections.append(Intersection(314,520,F,R1))
intersections.append(Intersection(314,520,F,R1))
intersections.append(Intersection(562,230,D,R1))
intersections.append(Intersection(725,32,A,R2))
intersections.append(Intersection(143,689,e1, R3))
intersections.append(Intersection(862,689,e2,R4))
intersections.append(Intersection(143,624,e1,E))
intersections.append(Intersection(862,624,e2,E))
intersections.append(Intersection(406,689,G,R4))

class Plane(pygame.Rect):
    TAXI_SPEED = 2
    def __init__(self, int1):
        super().__init__(int1.x,int1.y,50,50)
        self.x = int1.x
        self.y = int1.y
        self.fx = float(self.x)
        self.fy = float(self.y)
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
            if self.intersects(self.path_to_take[current_index+1]):
                self.inter = self.path_to_take[current_index+1]
                current_index = self.path_to_take.index(self.inter)
                if current_index == len(self.path_to_take)-1:
                    self.pathfinding = False
                    self.set_vel(self.path_to_take[current_index])
                    return
            self.set_vel(self.path_to_take[current_index+1])
        self.fx +=self.vx
        self.fy += self.vy
        self.x = int(self.fx)
        self.y = int(self.fy)
        self.draw()
    def draw(self):
        my_rect = pygame.Rect(self.x-25,self.y-25,50,50)
        pygame.draw.rect(screen, 'blue', my_rect)#TODO: draw a sprite
    def intersects(self, nextInt):
        dx = nextInt.x - self.x
        dy = nextInt.y - self.y
        distSquared = dx**2 + dy**2
        if distSquared <= 10:
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
            elif (firstInt.branch1.name == self.inter.branch2.name and firstInt.branch2.name == branchNames[0]) or (firstInt.branch2.name == self.inter.branch2.name and firstInt.branch1.name == branchNames[0]):
                branchNames.insert(0,self.inter.branch2.name)
        is_valid = True
        for b in range(0, len(branchNames)-1):
            if branchNames[b] == "E" and branchNames[b+1] == "R3" or branchNames[b] == "R3" and branchNames[b+1] == "E":
                branchNames.insert(b+1, e1.name)
            if branchNames[b] == "E" and branchNames[b+1] == "R4" or branchNames[b] == "R4" and branchNames[b + 1] == "E":
                branchNames.insert(b+1, e2.name)
        is_valid = True
        for x in range(0, len(branchNames) - 1):
            inter_is_valid = False
            for inter in intersections:
                if ((inter.branch1.name == branchNames[x] and inter.branch2.name == branchNames[x + 1]) or (
                        inter.branch2.name == branchNames[x] and inter.branch1.name == branchNames[x + 1])):
                    path_to_take.append(Intersection(inter.x, inter.y, inter.branch1, inter.branch2))
                    inter_is_valid = True
            if not inter_is_valid:
                is_valid = False
        if is_valid:
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
test = Plane(Intersection(744,114,C,Hangar))
test.pathfind("E R4 G E C A R2")
while True:
    #Process player inputs:
    #path_string = input("")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    #Do logical updates here:

    #Update graphics here:
    screen.blit(image, (0, 0))
    test.update()

  # Refresh on-screen display
    pygame.display.flip()
    clock.tick(60)         # wait until next frame (at 60 FPS)
