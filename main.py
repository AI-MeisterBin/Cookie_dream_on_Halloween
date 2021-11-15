import pygame

#창 크기
win_w = 800
win_h = 480

#색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#몬스터인 호박 클래스
class Pumkin:
    image_pum = ['pum1.png', 'pum2.png', 'pum3.png', 'pum4.png', 'pum5.png', 'pum6.png', 'pum7.png', 'pum8.png',
                 'pum9.png', 'pum10.png']

    def __init__(self, x=0, y=0, dx=0, dy=0):
        self.image = ""
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def load_image(self):
        self.image = pygame.image.load(random.choice(self.image_pum))
        self.width = self.image.get_rect().size[0]
        self.height = self.image.get_rect().size[1]

    def draw_image(self):
        screen.blit(self.image, [self.x, self.y])

    def move_x(self):
        self.x += self.dx

    def move_y(self):
        self.y += self.dy

    def check_screen_out(self):
        if self.y + self.height > win_h or self.y < 0:
            self.y -= self.dy

    def check_crash(self, pum):
        if (self.x + self.width > pum.x) and (self.x < pum.x + pum.width) and (self.y < pum.y + pum.height) and (
                self.y + self.height > pum.y):
            return True
        else:
            return False

#캐릭터 쿠키 클래스
class Cookie:
    image_cookie = ['cookie.png']

    def __init__(self, x=0, y=0, dx=0, dy=0):
        self.image = ""
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def load_image(self):
        self.image = pygame.image.load(random.choice(self.image_cookie))
        self.width = self.image.get_rect().size[0]
        self.height = self.image.get_rect().size[1]

    def draw_image(self):
        screen.blit(self.image, [self.x, self.y])

    def move_x(self):
        self.x += self.dx

    def move_y(self):
        self.y += self.dy

    def check_screen_out(self):
        if self.y + self.height > win_h or self.y < 0:
            self.y -= self.dy

    def check_crash(self, cookie):
        if (self.x + self.width > cookie.x) and (self.x < cookie.x + cookie.width) and (
                self.y < cookie.y + cookie.height) and (self.y + self.height > cookie.y):
            return True
        else:
            return False


def draw_menu():
    screen.blit(pygame.image.load('backimage.jpg'), [0, 0])

def draw_score():
    font_30 = pygame.font.SysFont("FixedSys", 30, True, False)
    text_score = font_30.render("Score: " + str(score), True, BLACK)
    screen.blit(text_score, [15, 15])