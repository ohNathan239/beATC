import pygame
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
        self.screen = pygame.display.set_mode((1200, 767))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)  # Use None for the default font
        self.image = pygame.image.load('airport v1.1.png')
        self.button_one = pygame.Rect(983, 460+64*0+20, 197, 50)
        self.button_two = pygame.Rect(983, 460+64*1+20, 197, 50)
        self.button_three = pygame.Rect(983, 460+64*2+20, 197, 50)
        self.button_four = pygame.Rect(983, 460+64*3+20, 197, 50)
        self.last_input_len = 0

    def get_the_text_bar(self, text):
        self.text_bar_words += text

    def get_the_pathfinding_str(self, text):
         self.it_pathfinds += text

    def delete_a_word(self):
        self.text_bar_words = self.text_bar_words[:len(self.text_bar_words)-self.last_input_len]
        print(self.text_bar_words)

    def delete_a_pathfinding_str(self):
        self.it_pathfinds = self.it_pathfinds[:len(self.it_pathfinds)-2]
        print(self.it_pathfinds)

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
                        print("taxi via")
                        self.get_the_text_bar(" taxi via ")
                        self.last_input_len = 10
                    elif self.button_two.collidepoint(mouse_pos):
                        print("hold short of")
                        self.get_the_text_bar(" hold short of ")
                        self.last_input_len = 15
                    elif self.button_three.collidepoint(mouse_pos):
                        print("give way to")
                        self.get_the_text_bar(" give way to ")
                        self.last_input_len = 13
                    elif self.button_four.collidepoint(mouse_pos):
                        print(" stop")
                        self.get_the_text_bar(" stop")
                        self.last_input_len = 5
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        print("a")
                        self.get_the_text_bar("alpha ")
                        self.get_the_pathfinding_str("a ")
                        self.last_input_len = 6
                    elif event.key == pygame.K_c:
                        print("c")
                        self.get_the_text_bar("charlie ")
                        self.get_the_pathfinding_str("c ")
                        self.last_input_len = 8
                    elif event.key == pygame.K_d:
                        print("d")
                        self.get_the_text_bar("delta ")
                        self.get_the_pathfinding_str("d ")
                        self.last_input_len = 6
                    elif event.key == pygame.K_e:
                        print("e")
                        self.get_the_text_bar("echo ")
                        self.get_the_pathfinding_str("e ")
                        self.last_input_len = 5
                    elif event.key == pygame.K_f:
                        print("f")
                        self.get_the_text_bar("foxtrot ")
                        self.get_the_pathfinding_str("f ")
                        self.last_input_len = 8
                    elif event.key == pygame.K_g:
                        print("g")
                        self.get_the_text_bar("golf ")
                        self.get_the_pathfinding_str("g ")
                        self.last_input_len = 5
                    elif event.key==pygame.K_BACKSPACE:
                        print("delete")
                        self.delete_a_word()
                        self.delete_a_pathfinding_str()
                    elif (event.key==pygame.K_ESCAPE):
                        running = False
                        print(running)

            #Do logical updates here:

            #Update graphics here:
            self.screen.fill('white') # Inspiration for UI https://www.google.com/url?sa=i&url=https%3A%2F%2Fflighttrainingcentral.com%2F2017%2F04%2Fatc-controller-sees-tech-tower%2F&psig=AOvVaw03ilNX_wzU7_oEnfBFeLcc&ust=1727441791395000&source=images&cd=vfe&opi=89978449&ved=0CBcQjhxqFwoTCNCdz6TU4IgDFQAAAAAdAAAAABAx
            runway = (60, 60, 60)
            taxiway = (100, 100, 100)
            self.screen.blit(self.image, (0, 0))
            text_surface = self.font.render(self.text_bar_words, True, 'black')  # True for anti-aliasing
            text_rect = text_surface.get_rect(topleft=(80, 715))
            self.screen.blit(text_surface, text_rect)

            # pygame.draw.line(screen, taxiway, (660, 10), (500, 550), 23)
            # pygame.draw.line(screen, taxiway, (660, 10), (500, 550), 23)
            pygame.draw.rect(self.screen, 'black', (75, 705, 900, 40), 2)
            pygame.draw.rect(self.screen, 'black', (973, 300+150, (1200-983), 245+50), 2)
            i=0
            while i < 4:
                temp_rect = (983, 460+64*i+20, 197, 50)
                pygame.draw.rect(self.screen, 'black', temp_rect, 2)
                if i ==0:
                    button_one = pygame.Rect(temp_rect)
                    text_surface = self.font.render('...taxi via...', True, 'black')  # True for anti-aliasing
                    text_rect = text_surface.get_rect(topleft=(983+30, 544-64+15))
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