import pygame
import random
from time import sleep

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
    font_30 = pygame.font.SysFont("나눔스퀘어", 30, True, False)
    font_50 = pygame.font.SysFont("나눔스퀘어", 50, True, False)
    text_score = font_30.render("Score: " + str(score), True, BLACK)
    screen.blit(text_score, [350, 60])
    text_title = font_50.render("Cookie's dream on Halloween", True, WHITE)
    screen.blit(text_title, [120, 200])
    pygame.display.flip()

def draw_score():
    font_30 = pygame.font.SysFont("FixedSys", 30, True, False)
    text_score = font_30.render("Score: " + str(score), True, BLACK)
    screen.blit(text_score, [15, 15])

if __name__ == '__main__':
    pygame.init()                                                          #pygame 실행
    screen = pygame.display.set_mode((win_w, win_h))                       #화면 크기 설정
    pygame.display.set_caption("Cookie's dream on Halloween")              #이름 설정
    clock = pygame.time.Clock()

    bgm = pygame.mixer.Sound('bgm.wav')                                    #배경음악설정
    bgm.play(-1)                                                           #무한재생
    sound_crash = pygame.mixer.Sound('crash.wav')

    player = Cookie((win_w - 200), (win_h / 2), 0, 0)                      #플레이어의 위치 설정
    player.load_image()                                                    #플레이어 배치

    #몬스터인 호박의 처음 위치와 속도를 설정
    pums = []
    pum_count = 5
    for i in range(pum_count):
        x = random.randrange(-150, -50)
        y = random.randrange(0, win_h - 55)
        pum = Pumkin(x, y, random.randint(5, 10), 0)
        pum.load_image()
        pums.append(pum)                                                   #pum이라는 배열에 추가

    #점수, 게임실행 코드
    score = 0
    crash = True
    game_on = True
    while game_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False

            #충돌유무에 따른 화면 세팅
            if crash:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:     #게임시작 = crash False
                    crash = False
                    for i in range(pum_count):                                       #호박위치 설정
                        pums[i].x = random.randrange(-150, -50)
                        pums[i].y = random.randrange(0, win_h - pums[i].height)
                        pums[i].load_image()

                    player.y = win_h / 2                                             #위치 초기화
                    player.dx = 0
                    player.dy = 0
                    score = 0
                    pygame.mouse.set_visible(False)

            if not crash:                                                            #플레이어가 움직임
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player.dy = -7
                    elif event.key == pygame.K_DOWN:
                        player.dy = 7
                    elif event.key == pygame.K_RIGHT:
                        player.dx = 7
                    elif event.key == pygame.K_LEFT:
                        player.dx = -7

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        player.dy = 0
                    elif event.key == pygame.K_DOWN:
                        player.dy = 0
                    elif event.key == pygame.K_RIGHT:
                        player.dx = 0
                    elif event.key == pygame.K_LEFT:
                        player.dx = 0

        screen.blit(pygame.image.load('backimage2.jpeg'), [0, 0])

        if not crash:
            player.draw_image()
            player.move_x()
            player.move_y()
            player.check_screen_out()

            for i in range(pum_count):
                pums[i].draw_image()
                pums[i].x += pums[i].dx
                if pums[i].x > win_w:
                    score += 10
                    pums[i].x = random.randrange(-150, -50)
                    pums[i].y = random.randrange(0, win_h - pums[i].height)
                    pums[i].dx = random.randint(5, 10)
                    pums[i].load_image()

            for i in range(pum_count):
                if player.check_crash(pums[i]):
                    crash = True
                    sound_crash.play()
                    sleep(2)
                    pygame.mouse.set_visible(True)
                    break
            draw_score()
            pygame.display.flip()

        else:
            draw_menu()

        clock.tick(60)

    pygame.quit()