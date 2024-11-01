import pygame
import math
import random
pygame.init()

clock = pygame.time.Clock()
image = pygame.image.load("file.png")
planeImg = pygame.image.load("Plane.png")
planeImg = pygame.transform.scale(planeImg,(30,29))
screen = pygame.display.set_mode((image.get_width(),image.get_height()))

TYPES = ["Runway", "Taxiway", "Hangar"]
class Branch:
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
intersections = [Intersection(762, 72, A, C), Intersection(567, 302, D, C), Intersection(352, 555, F, C),
                 Intersection(406, 620, E, G), Intersection(470, 435, C, FBO), Intersection(735, 112, C, Hangar),
                 Intersection(305, 618, C, E), Intersection(314, 520, F, R1),
                 Intersection(562, 230, D, R1), Intersection(725, 32, A, R2), Intersection(143, 689, e1, R3),
                 Intersection(862, 689, e2, R4), Intersection(143, 620, e1, E), Intersection(862, 620, e2, E),
                 Intersection(406, 689, G, R4)]

class Plane(pygame.Rect):
    TAXI_SPEED = 2

    def __init__(self, int1, image, number):
        super().__init__(int1.x - image.get_width() / 2, int1.y - image.get_height() / 2, image.get_width(), image.get_height())
        self.base_img = image
        self.rotated_img = image
        self.fx = float(self.centerx)
        self.fy = float(self.centery)
        self.vx = 0
        self.vy = 0
        self.inter = int1
        self.pathfinding = False
        self.path_to_take = []
        self.deg_pos = 0
        self.number = number

    def set_vel(self, int2):
        dx = int2.x - self.inter.x
        dy = int2.y - self.inter.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance > 0:
            self.vx = Plane.TAXI_SPEED * (dx / distance)
            self.vy = Plane.TAXI_SPEED * (dy / distance)
            self.rotate(180 * math.atan2(-self.vy, self.vx) / math.pi)
        else:
            self.vx = 0
            self.vy = 0

    def rotate(self, degrees):
        # Rotate the image and update the angle
        self.rotated_img = pygame.transform.rotate(self.base_img, degrees)
        self.deg_pos = degrees

    def update(self):
        if self.pathfinding:
            current_index = self.path_to_take.index(self.inter)
            if self.intersects(self.path_to_take[current_index + 1]):
                self.inter = self.path_to_take[current_index + 1]
                current_index = self.path_to_take.index(self.inter)
                if current_index == len(self.path_to_take) - 1:
                    self.pathfinding = False
                    self.set_vel(self.path_to_take[current_index])
                    return
            self.set_vel(self.path_to_take[current_index + 1])

        self.fx += self.vx
        self.fy += self.vy
        self.centerx = int(self.fx)
        self.centery = int(self.fy)
        self.draw()

    def draw(self):
        # Create a rect for the rotated image
        rotated_rect = self.rotated_img.get_rect(center=(self.fx, self.fy))
        screen.blit(self.rotated_img, rotated_rect.topleft)

    def intersects(self, next_int):
        dx = next_int.x - self.centerx
        dy = next_int.y - self.centery
        dist_squared = dx ** 2 + dy ** 2
        return dist_squared <= 10
    def parse_string(self, input_string):
        branch_names = input_string.split() #The user should enter a string of taxiway and runway names separated by spaces
        print(branch_names)
        is_valid = True
        for name in branch_names:#loop through each name entered
            char_is_valid = False
            for path in branches:#check if the name entered is in the list of valid branch names
                if name == path.name:
                    char_is_valid = True
            if not char_is_valid:
                is_valid = False
        if not is_valid:
            return False  #Everything works up to here
        path_to_take = [self.inter]
        for firstInt in intersections:
            if (firstInt.branch1.name == self.inter.branch1.name and firstInt.branch2.name == branch_names[0]) or (firstInt.branch2.name == self.inter.branch1.name and firstInt.branch1.name == branch_names[0]):
                branch_names.insert(0,self.inter.branch1.name)
                print("this triggered")
            elif (firstInt.branch1.name == self.inter.branch2.name and firstInt.branch2.name == branch_names[0]) or (firstInt.branch2.name == self.inter.branch2.name and firstInt.branch1.name == branch_names[0]):
                branch_names.insert(0,self.inter.branch2.name)
                print("or this triggered")
        is_valid = True
        for b in range(0, len(branch_names)-1):
            if branch_names[b] == "E" and branch_names[b+1] == "R3" or branch_names[b] == "R3" and branch_names[b+1] == "E":
                branch_names.insert(b+1, e1.name)
            if branch_names[b] == "E" and branch_names[b+1] == "R4" or branch_names[b] == "R4" and branch_names[b + 1] == "E":
                branch_names.insert(b+1, e2.name)
        is_valid = True
        for x in range(0, len(branch_names) - 1):
            inter_is_valid = False
            for inter in intersections:
                if ((inter.branch1.name == branch_names[x] and inter.branch2.name == branch_names[x + 1]) or (
                        inter.branch2.name == branch_names[x] and inter.branch1.name == branch_names[x + 1])):
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
        if not self.path_to_take:
            print("invalid string")
            return False
        self.pathfinding = True
        return True
    def get_number(self):
        return self.number
temp = Plane(Intersection(735, 112,C,Hangar), planeImg, 12345)


class Main:
    def __init__(self):
        self.text_bar_words = ""
        self.it_pathfinds = ""
        self.it_readsback = ""
        self.screen = pygame.display.set_mode((1200, 767))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)  # Use None for the default font
        self.image = pygame.image.load('airport v1.2.png')
        self.button_one = pygame.Rect(983, 460+64*0+20, 197, 50)
        self.button_two = pygame.Rect(983, 460+64*1+20, 197, 50)
        self.button_three = pygame.Rect(983, 460+64*2+20, 197, 50)
        self.button_four = pygame.Rect(983, 460+64*3+20, 197, 50)
        self.last_input_len = 0
        self.hanger_button = pygame.Rect(880, 350, 175, 50)
        self.fbo_button = pygame.Rect(560, 495, 75, 50)
        self.rnwy09_button = pygame.Rect(100, 650, 100, 50)
        self.rnwy27_button = pygame.Rect(825, 650, 100, 50)
        self.rnwy04_button = pygame.Rect(255, 510, 50, 50)
        self.rnwy22_button = pygame.Rect(715, 0, 50, 30)
        self.twaya_button = pygame.Rect(710, 28, 50, 50)
        self.twayc_button = pygame.Rect(580, 235, 50, 50)
        self.twayd_button = pygame.Rect(530, 240, 50, 50)
        self.twaye_button = pygame.Rect(470, 590, 50, 50)
        self.twayf_button = pygame.Rect(310, 510, 40, 40)
        self.twayg_button = pygame.Rect(375, 620, 50, 50)
        self.dest = ""
        self.show_notif = False
        self.notif_starting_time = None
        self.first_plane = True
        self.plane_list = [Plane(Intersection(470, 435, C, FBO), "N2159H")]
        self.plane_selected = self.plane_list[0]
        self.make_timing_random = int(random.random()*3000)
        self.constant_minimum_timing = 3000
        self.plane_timer = 0
        self.last_plane_generated = 0

    def get_the_text_bar(self, text):
        self.text_bar_words += text
    def make_it_read_back(self, text):
        self.it_readsback += text
    def removes_some_of_readback(self):
        self.it_readsback = self.it_readsback[:len(self.it_readsback)-self.last_input_len]
        print(self.it_readsback)
    def generate_aircraft_ids(self):
        type_of_reg = int(random.random() * 10)
        if type_of_reg == 0:
            number_of_nums = int(random.random() * 3) + 3
            if number_of_nums == 3:
                string = "N" + str((int(random.random() * 7)) + 3) + str((int(random.random() * 10))) + str((int(random.random() * 10)))
                print(string)
                return string
            elif number_of_nums == 4:
                string = "N" + str((int(random.random() * 7)) + 3) + str((int(random.random() * 10))) + str((int(random.random() * 10))) + str((int(random.random() * 10)))
                print(string)
                return string
            else:
                string = "N" + str((int(random.random() * 7)) + 3) + str((int(random.random() * 10))) + str((int(random.random() * 10))) + str((int(random.random() *10))) + str((int(random.random() *10)))
                print(string)
                return string
        elif type_of_reg == 1:
            number_of_nums = int(random.random()*4)+1
            if number_of_nums == 1:
                string = "N" + str(int(random.random() * 9)+1) + self.generate_random_letter()
                print(string)
                return string
            elif number_of_nums == 2:
                string = "N" + str(int(random.random() * 9)+1) +str((int(random.random() * 10))) + self.generate_random_letter()
                print(string)
                return string
            elif number_of_nums == 3:
                string = "N" + str(int(random.random() * 9)+1) +str((int(random.random() * 10)))+str((int(random.random() * 10))) + self.generate_random_letter()
                print(string)
                return string
            else:
                string = "N" + str(int(random.random() * 9)+1)+str((int(random.random() * 10)))+str((int(random.random() * 10)))+str((int(random.random() * 10))) +self.generate_random_letter()
                print(string)
                return string
        else:
            number_of_nums = int(random.random()*5)+1
            if number_of_nums == 1:
                string = "N"+ str(int(random.random() * 9)+1) + self.generate_random_letter() + self.generate_random_letter()
                print(string)
                return string
            elif number_of_nums == 2:
                string = "N"+ str(int(random.random() * 9)+1) + str((int(random.random() * 10))) + self.generate_random_letter() + self.generate_random_letter()
                print(string)
                return string
            else:
                string = "N"+ str(int(random.random() * 9)+1) + str((int(random.random() * 10))) + str((int(random.random() * 10))) +  self.generate_random_letter() + self.generate_random_letter()
                print(string)
                return string
    @staticmethod
    def generate_random_letter():
        letter = int((random.random() * 26) + 1)
        if letter == 1:
            return "A"
        elif letter == 2:
            return "B"
        elif letter == 3:
            return "C"
        elif letter == 4:
            return "D"
        elif letter == 5:
            return "E"
        elif letter == 6:
            return "F"
        elif letter == 7:
            return "G"
        elif letter == 8:
            return "H"
        elif letter == 9:
            return ""
        elif letter == 10:
            return "J"
        elif letter == 11:
            return "K"
        elif letter == 12:
            return "L"
        elif letter == 13:
            return "M"
        elif letter == 14:
            return "N"
        elif letter == 15:
            return ""
        elif letter == 16:
            return "P"
        elif letter == 17:
            return "Q"
        elif letter == 18:
            return "R"
        elif letter == 19:
            return "S"
        elif letter == 20:
            return "T"
        elif letter == 21:
            return "U"
        elif letter == 22:
            return "V"
        elif letter == 23:
            return "W"
        elif letter == 24:
            return "X"
        elif letter == 25:
            return "Y"
        elif letter == 26:
            return "Z"
    def get_the_pathfinding_str(self, text):
         self.it_pathfinds += text
    def delete_a_word(self):
        self.text_bar_words = self.text_bar_words[:len(self.text_bar_words)-self.last_input_len]
    def delete_a_pathfinding_str(self):
        self.it_pathfinds = self.it_pathfinds[:len(self.it_pathfinds)-2]
    def fixes_the_pathfinding_string(self):
        self.it_pathfinds += self.dest
    def execute(self):
        self.plane_selected.pathfind(self.it_pathfinds)
        if self.plane_selected.parse_string(self.it_pathfinds):
            print(self.it_readsback + self.plane_selected.get_number())
            return True
        else:
            print("Unable")
            return False

    def run(self):
        running = True
        while running:
            #Process player inputs:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if self.button_one.collidepoint(mouse_pos):
                        print("taxi ")
                        self.get_the_text_bar("taxi to ")
                        self.make_it_read_back("taxi to ")
                        self.last_input_len = 8
                    elif self.button_two.collidepoint(mouse_pos):
                        print("hold short of")
                        self.get_the_text_bar("hold short of ")
                        self.make_it_read_back("hold short of ")
                        self.last_input_len = 14
                    elif self.button_three.collidepoint(mouse_pos):
                        print("give way to")
                        self.get_the_text_bar("give way to ")
                        self.make_it_read_back("give way to ")
                        self.last_input_len = 12
                    elif self.button_four.collidepoint(mouse_pos):
                        print("stop")
                        self.get_the_text_bar("stop ")
                        self.make_it_read_back("stop ")
                        self.last_input_len = 5
                    elif self.hanger_button.collidepoint(mouse_pos):
                        print('hangar via')
                        self.get_the_text_bar("hangars via ")
                        self.make_it_read_back("hangars via ")
                        self.dest = "Hangar"
                        self.last_input_len = 12
                    elif self.fbo_button.collidepoint(mouse_pos):
                        print('FBO via ')
                        self.get_the_text_bar('FBO via ')
                        self.make_it_read_back("FBO via ")
                        self.dest = "FBO"
                        self.last_input_len = 8
                    elif self.rnwy04_button.collidepoint(mouse_pos):
                        print('to runway 04 via ')
                        self.get_the_text_bar('runway 04 via ')
                        self.make_it_read_back("runway 04 via ")
                        self.dest = "R1"
                        self.last_input_len = 14
                    elif self.rnwy09_button.collidepoint(mouse_pos):
                        print('to runway 09 via ')
                        self.get_the_text_bar('runway 09 via ')
                        self.make_it_read_back('runway 09 via ')
                        self.dest="R3"
                        self.last_input_len = 14
                    elif self.rnwy22_button.collidepoint(mouse_pos):
                        print('to runway 22 via ')
                        self.get_the_text_bar('runway 22 via ')
                        self.make_it_read_back('runway 22 via ')
                        self.dest="R2"
                        self.last_input_len = 14
                    elif self.rnwy27_button.collidepoint(mouse_pos):
                        print('to runway 27 via ')
                        self.get_the_text_bar('runway 27 via ')
                        self.make_it_read_back('runway 27 via ')
                        self.dest = "R4"
                        self.last_input_len = 14
                    elif self.twaya_button.collidepoint(mouse_pos):
                        print("a")
                        self.get_the_text_bar("alpha ")
                        self.make_it_read_back('alpha ')
                        self.get_the_pathfinding_str("A ")
                        self.last_input_len = 6
                    elif self.twayc_button.collidepoint(mouse_pos):
                        print("c")
                        self.get_the_text_bar("charlie ")
                        self.make_it_read_back('charlie ')
                        self.get_the_pathfinding_str("C ")
                        self.last_input_len = 8
                        print(str)
                    elif self.twayd_button.collidepoint(mouse_pos):
                        print("d")
                        self.get_the_text_bar("delta ")
                        self.make_it_read_back('delta ')
                        self.get_the_pathfinding_str("D ")
                        self.last_input_len = 6
                    elif self.twaye_button.collidepoint(mouse_pos):
                        print("e")
                        self.get_the_text_bar("echo ")
                        self.make_it_read_back('echo ')
                        self.get_the_pathfinding_str("E ")
                        self.last_input_len = 5
                    elif self.twayf_button.collidepoint(mouse_pos):
                        print("f")
                        self.get_the_text_bar("foxtrot ")
                        self.make_it_read_back('foxtrot ')
                        self.get_the_pathfinding_str("F ")
                        self.last_input_len = 8
                    elif self.twayg_button.collidepoint(mouse_pos):
                        print("g")
                        self.get_the_text_bar("golf ")
                        self.make_it_read_back('golf ')
                        self.get_the_pathfinding_str("G ")
                        self.last_input_len = 5
                    for a in self.plane_list:
                        if a.collidepoint(mouse_pos):
                            self.get_the_text_bar(a.get_number() + " ")
                            self.plane_selected = a
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        print("a")
                        self.get_the_text_bar("alpha ")
                        self.make_it_read_back('alpha ')
                        self.get_the_pathfinding_str("A ")
                        self.last_input_len = 6
                    elif event.key == pygame.K_c:
                        print("c")
                        self.get_the_text_bar("charlie ")
                        self.make_it_read_back('charlie ')
                        self.get_the_pathfinding_str("C ")
                        self.last_input_len = 8
                        print(str)
                    elif event.key == pygame.K_d:
                        print("d")
                        self.get_the_text_bar("delta ")
                        self.make_it_read_back('delta ')
                        self.get_the_pathfinding_str("D ")
                        self.last_input_len = 6
                    elif event.key == pygame.K_e:
                        print("e")
                        self.get_the_text_bar("echo ")
                        self.make_it_read_back('echo ')
                        self.get_the_pathfinding_str("E ")
                        self.last_input_len = 5
                    elif event.key == pygame.K_f:
                        print("f")
                        self.get_the_text_bar("foxtrot ")
                        self.make_it_read_back('foxtrot ')
                        self.get_the_pathfinding_str("F ")
                        self.last_input_len = 8
                    elif event.key == pygame.K_g:
                        print("g")
                        self.get_the_text_bar("golf ")
                        self.make_it_read_back('golf ')
                        self.get_the_pathfinding_str("G ")
                        self.last_input_len = 5
                    elif event.key==pygame.K_BACKSPACE:
                        print("delete")
                        self.removes_some_of_readback()
                        self.delete_a_word()
                        self.delete_a_pathfinding_str()
                    elif event.key==pygame.K_ESCAPE:
                        running = False
                        print(self.it_pathfinds)
                    elif event.key==pygame.K_t:
                        print("to")
                        self.get_the_text_bar("to ")
                    elif event.key==pygame.K_UP:
                        if self.text_bar_words:
                            print("execute")
                            self.fixes_the_pathfinding_string()
                            print(self.it_pathfinds)
                            self.execute()
                            self.it_pathfinds = ""
                            self.show_notif = True
                            self.notif_starting_time = pygame.time.get_ticks()
                            self.make_it_read_back(self.plane_list[0].get_number() + " ")
                        self.text_bar_words = ""
                    elif event.key==pygame.K_DOWN:
                        print("clear")
                        self.text_bar_words = ""
                        self.it_readsback = ""
                        self.it_pathfinds = ""
            #Do logical updates here:
            self.plane_timer = pygame.time.get_ticks()
            if self.plane_timer == (self.constant_minimum_timing + self.make_timing_random):
                location_picker = int(random.random()*10)
                if location_picker == 0:
                    self.plane_list.append(Plane(Intersection(470, 435, C, FBO), self.generate_aircraft_ids()))
                elif location_picker == 1:
                    self.plane_list.append(Plane(Intersection(744, 114, C, Hangar), self.generate_aircraft_ids()))
                elif location_picker == 2:
                    self.plane_list.append(Plane(Intersection(314, 520, F, R1), self.generate_aircraft_ids()))
                elif location_picker == 3:
                    self.plane_list.append(Plane(Intersection(562, 230, D, R1), self.generate_aircraft_ids()))
                elif location_picker == 4:
                    self.plane_list.append(Plane(Intersection(725, 32, A, R2), self.generate_aircraft_ids()))
                elif location_picker == 5:
                    self.plane_list.append(Plane(Intersection(143, 689, e1, R3), self.generate_aircraft_ids()))
                elif location_picker == 6:
                    self.plane_list.append(Plane(Intersection(562, 230, D, R1), self.generate_aircraft_ids()))
                elif location_picker == 7:
                    self.plane_list.append(Plane(Intersection(143, 689, e1, R3), self.generate_aircraft_ids()))
                elif location_picker == 8:
                    self.plane_list.append(Plane(Intersection(862, 689, e2, R4), self.generate_aircraft_ids()))
                else:
                    self.plane_list.append(Plane(Intersection(406, 689, G, R4), self.generate_aircraft_ids()))
            #Update graphics here:
            self.screen.fill('white') # Inspiration for UI https://www.google.com/url?sa=i&url=https%3A%2F%2Fflighttrainingcentral.com%2F2017%2F04%2Fatc-controller-sees-tech-tower%2F&psig=AOvVaw03ilNX_wzU7_oEnfBFeLcc&ust=1727441791395000&source=images&cd=vfe&opi=89978449&ved=0CBcQjhxqFwoTCNCdz6TU4IgDFQAAAAAdAAAAABAx
            self.screen.blit(self.image, (0, 0))
            text_surface = self.font.render(self.text_bar_words, True, 'black')  # True for antialiasing
            text_rect = text_surface.get_rect(topleft=(80-40, 715))
            self.screen.blit(text_surface, text_rect)
            pygame.draw.rect(self.screen, 'black', (75-40, 705, 900+40, 40), 2)
            pygame.draw.rect(self.screen, 'black', (973, 300+150, (1200-983), 245+50), 2)
            if self.show_notif:
                current_time = pygame.time.get_ticks()
                if current_time < self.notif_starting_time +3000 and self.show_notif:
                    text_surface_two = self.font.render(self.it_readsback, True, 'black')
                    text_rect_two = text_surface.get_rect(topleft=(20,20))
                    self.screen.blit(text_surface_two,text_rect_two)
                else:
                    self.it_readsback = ""
                    self.show_notif = False
            i=0
            while i < 4:
                temp_rect = (983, 460+64*i+20, 197, 50)
                pygame.draw.rect(self.screen, 'black', temp_rect, 2)
                if i ==0:
                    text_surface = self.font.render('...taxi to...', True, 'black')  # True for antialiasing
                    text_rect = text_surface.get_rect(topleft=(983+30+10, 544-64+15))
                    self.screen.blit(text_surface, text_rect)
                elif i==1:
                    text_surface = self.font.render('...hold short of...', True, 'black')  # True for antialiasing
                    text_rect = text_surface.get_rect(topleft=(983+3, 608 -64+15))
                    self.screen.blit(text_surface, text_rect)
                elif i==2:
                    text_surface = self.font.render('...give way to...', True, 'black')  # True for antialiasing
                    text_rect = text_surface.get_rect(topleft=(983+10, 672 -64+15))
                    self.screen.blit(text_surface, text_rect)
                else:
                    text_surface = self.font.render('...stop...', True, 'black')  # True for antialiasing
                    text_rect = text_surface.get_rect(topleft=(983+55, 736 -64+15))
                    self.screen.blit(text_surface, text_rect)
                i += 1
            for t in self.plane_list:
                t.update()
            pygame.display.flip()  # Refresh on-screen display
            self.clock.tick(60)  # wait until next frame (at 60 FPS)
main = Main()
main.run()
