from lib2to3.fixes.fix_dict import iter_exempt

import pygame
import random
pygame.init()

class Plane(pygame.Rect):
    def __init__(self, x, y, vx, vy):
        super().__init__(x,y,50,50)
        self.vx = vx
        self.vy = vy
        self.screen = pygame.display.set_mode((1200, 767))
    def update(self):
        self.x+=self.vx
        self.y += self.vy
        self.draw()

    def draw(self):
        pygame.draw.rect(self.screen, 'white', self)

class RoadWay():
    def __init__(self, startX, startY, endX, endY):
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY
        self.screen = pygame.display.set_mode((1200, 767))
    def draw(self):
            pygame.draw.rect(self.screen,'grey', self, 0)

class Main():
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

    def get_the_text_bar(self, text):
        self.text_bar_words += text

    def make_it_read_back(self, text):
        self.it_readsback += text

    def removes_some_of_readback(self):
        self.it_readsback = self.it_readsback[:len(self.it_readsback)-self.last_input_len]
        print(self.it_readsback)

    def generate_aircraft(self):
        type = (int)(random.random()*7)
        if type == 0:
            number_of_nums = (int)(random.random()*3)+3
            if number_of_nums == 3:
                string = "N" + str(((int)(random.random()*7))+3) + str(((int)(random.random()*10))) + str(((int)(random.random()*10)))
                print(string)
            elif number_of_nums == 4:
                string = "N" + str(((int)(random.random() * 7)) + 3) + str(((int)(random.random() * 10))) + str(((int)(random.random() * 10))) + str(((int)(random.random() * 10)))
                print(string)
            else:
                string = "N" + str(((int)(random.random() * 7)) + 3) + str(((int)(random.random() * 10))) + str(((int)(random.random() * 10))) + str(((int)(random.random() *10))) + str(((int)(random.random() *10)))
                print(string)
        elif type == 1:
            number_of_nums = (int)(random.random()*4)+1
            if number_of_nums == 1:
                string = "N" + str((int)(random.random() * 9)+1) + self.generate_random_letter()
                print(string)
            elif number_of_nums == 2:
                string = "N" + str((int)(random.random() * 9)+1) +str(((int)(random.random() * 10))) + self.generate_random_letter()
                print(string)
            elif number_of_nums == 3:
                string = "N" + str((int)(random.random() * 9)+1) +str(((int)(random.random() * 10)))+str(((int)(random.random() * 10))) + self.generate_random_letter()
                print(string)
            else:
                string = "N" + str((int)(random.random() * 9)+1)+str(((int)(random.random() * 10)))+str(((int)(random.random() * 10)))+str(((int)(random.random() * 10))) +self.generate_random_letter()
                print(string)
        else:
            number_of_nums = (int)(random.random()*4)+1
            if number_of_nums == 1:
                string = "N"+ str((int)(random.random() * 9)+1) + self.generate_random_letter() + self.generate_random_letter()
                print(string)
            elif number_of_nums == 2:
                string = "N"+ str((int)(random.random() * 9)+1) + str(((int)(random.random() * 10))) + self.generate_random_letter() + self.generate_random_letter()
                print(string)
            else:
                string = "N"+ str((int)(random.random() * 9)+1) + str(((int)(random.random() * 10))) + str(((int)(random.random() * 10))) +  self.generate_random_letter() + self.generate_random_letter()
                print(string)

    def generate_random_letter(self):
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
        print(self.text_bar_words)

    def delete_a_pathfinding_str(self):
        self.it_pathfinds = self.it_pathfinds[:len(self.it_pathfinds)-2]
        print(self.it_pathfinds)

    # def readback(self):

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
                        print('hanger via')
                        self.get_the_text_bar("hangers via ")
                        self.make_it_read_back("hangers via ")
                        self.last_input_len = 12
                    elif self.fbo_button.collidepoint(mouse_pos):
                        print('FBO via ')
                        self.get_the_text_bar('FBO via ')
                        self.make_it_read_back("FBO via")
                        self.last_input_len = 8
                    elif self.rnwy04_button.collidepoint(mouse_pos):
                        print('to runway 04 via ')
                        self.get_the_text_bar('runway 04 via ')
                        self.make_it_read_back("runway 04 via ")
                        self.last_input_len = 14
                    elif self.rnwy09_button.collidepoint(mouse_pos):
                        print('to runway 09 via ')
                        self.get_the_text_bar('runway 09 via ')
                        self.make_it_read_back('runway 09 via ')
                        self.last_input_len = 14
                    elif self.rnwy22_button.collidepoint(mouse_pos):
                        print('to runway 22 via ')
                        self.get_the_text_bar('runway 22 via ')
                        self.make_it_read_back('runway 22 via ')
                        self.last_input_len = 14
                    elif self.rnwy27_button.collidepoint(mouse_pos):
                        print('to runway 27 via ')
                        self.get_the_text_bar('runway 27 via ')
                        self.make_it_read_back('runway 27 via ')
                        self.last_input_len = 14
                    elif self.twaya_button.collidepoint(mouse_pos):
                        print("a")
                        self.get_the_text_bar("alpha ")
                        self.make_it_read_back('alpha ')
                        self.get_the_pathfinding_str("a ")
                        self.last_input_len = 6
                    elif self.twayc_button.collidepoint(mouse_pos):
                        print("c")
                        self.get_the_text_bar("charlie ")
                        self.make_it_read_back('charlie ')
                        self.get_the_pathfinding_str("c ")
                        self.last_input_len = 8
                        print(str)
                    elif self.twayd_button.collidepoint(mouse_pos):
                        print("d")
                        self.get_the_text_bar("delta ")
                        self.make_it_read_back('delta ')
                        self.get_the_pathfinding_str("d ")
                        self.last_input_len = 6
                    elif self.twaye_button.collidepoint(mouse_pos):
                        print("e")
                        self.get_the_text_bar("echo ")
                        self.make_it_read_back('echo ')
                        self.get_the_pathfinding_str("e ")
                        self.last_input_len = 5
                    elif self.twayf_button.collidepoint(mouse_pos):
                        print("f")
                        self.get_the_text_bar("foxtrot ")
                        self.make_it_read_back('foxtrot ')
                        self.get_the_pathfinding_str("f ")
                        self.last_input_len = 8
                    elif self.twayg_button.collidepoint(mouse_pos):
                        print("g")
                        self.get_the_text_bar("golf ")
                        self.make_it_read_back('golf ')
                        self.get_the_pathfinding_str("g ")
                        self.last_input_len = 5
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        print("a")
                        self.get_the_text_bar("alpha ")
                        self.make_it_read_back('alpha ')
                        self.get_the_pathfinding_str("a ")
                        self.last_input_len = 6
                    elif event.key == pygame.K_c:
                        print("c")
                        self.get_the_text_bar("charlie ")
                        self.make_it_read_back('charlie ')
                        self.get_the_pathfinding_str("c ")
                        self.last_input_len = 8
                        print(str)
                    elif event.key == pygame.K_d:
                        print("d")
                        self.get_the_text_bar("delta ")
                        self.make_it_read_back('delta ')
                        self.get_the_pathfinding_str("d ")
                        self.last_input_len = 6
                    elif event.key == pygame.K_e:
                        print("e")
                        self.get_the_text_bar("echo ")
                        self.make_it_read_back('echo ')
                        self.get_the_pathfinding_str("e ")
                        self.last_input_len = 5
                    elif event.key == pygame.K_f:
                        print("f")
                        self.get_the_text_bar("foxtrot ")
                        self.make_it_read_back('foxtrot ')
                        self.get_the_pathfinding_str("f ")
                        self.last_input_len = 8
                    elif event.key == pygame.K_g:
                        print("g")
                        self.get_the_text_bar("golf ")
                        self.make_it_read_back('golf ')
                        self.get_the_pathfinding_str("g ")
                        self.last_input_len = 5
                    elif event.key==pygame.K_BACKSPACE:
                        print("delete")
                        self.removes_some_of_readback()
                        self.delete_a_word()
                        self.delete_a_pathfinding_str()
                    elif event.key==pygame.K_ESCAPE:
                        running = False
                    elif event.key==pygame.K_t:
                        print("to")
                        self.get_the_text_bar("to ")
                    elif event.key==pygame.K_UP:
                        print("execute")
                        self.text_bar_words = ""
                        self.readback()
                    elif event.key==pygame.K_DOWN:
                        print("clear")
                        self.text_bar_words = ""

            #Do logical updates here:

            #Update graphics here:
            self.screen.fill('white') # Inspiration for UI https://www.google.com/url?sa=i&url=https%3A%2F%2Fflighttrainingcentral.com%2F2017%2F04%2Fatc-controller-sees-tech-tower%2F&psig=AOvVaw03ilNX_wzU7_oEnfBFeLcc&ust=1727441791395000&source=images&cd=vfe&opi=89978449&ved=0CBcQjhxqFwoTCNCdz6TU4IgDFQAAAAAdAAAAABAx
            runway = (60, 60, 60)
            taxiway = (100, 100, 100)
            self.screen.blit(self.image, (0, 0))
            text_surface = self.font.render(self.text_bar_words, True, 'black')  # True for anti-aliasing
            text_rect = text_surface.get_rect(topleft=(80-40, 715))
            self.screen.blit(text_surface, text_rect)
            # self.generate_aircraft()

            # pygame.draw.line(screen, taxiway, (660, 10), (500, 550), 23)
            # pygame.draw.line(screen, taxiway, (660, 10), (500, 550), 23)
            pygame.draw.rect(self.screen, 'black', (75-40, 705, 900+40, 40), 2)
            pygame.draw.rect(self.screen, 'black', (973, 300+150, (1200-983), 245+50), 2)

            i=0
            while i < 4:
                temp_rect = (983, 460+64*i+20, 197, 50)
                pygame.draw.rect(self.screen, 'black', temp_rect, 2)
                if i ==0:
                    button_one = pygame.Rect(temp_rect)
                    text_surface = self.font.render('...taxi to...', True, 'black')  # True for anti-aliasing
                    text_rect = text_surface.get_rect(topleft=(983+30+10, 544-64+15))
                    self.screen.blit(text_surface, text_rect)
                elif i==1:
                    button_two = pygame.Rect(temp_rect)
                    text_surface = self.font.render('...hold short of...', True, 'black')  # True for anti-aliasing
                    text_rect = text_surface.get_rect(topleft=(983+3, 608 -64+15))
                    self.screen.blit(text_surface, text_rect)
                elif i==2:
                    button_three = pygame.Rect(temp_rect)
                    text_surface = self.font.render('...give way to...', True, 'black')  # True for anti-aliasing
                    text_rect = text_surface.get_rect(topleft=(983+10, 672 -64+15))
                    self.screen.blit(text_surface, text_rect)
                else:
                    button_four = pygame.Rect(temp_rect)
                    text_surface = self.font.render('...stop...', True, 'black')  # True for anti-aliasing
                    text_rect = text_surface.get_rect(topleft=(983+55, 736 -64+15))
                    self.screen.blit(text_surface, text_rect)
                i += 1
            pygame.display.flip()  # Refresh on-screen display
            self.clock.tick(60)  # wait until next frame (at 60 FPS)


main = Main()
main.run()
