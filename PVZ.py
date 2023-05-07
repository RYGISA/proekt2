#Створи власний Шутер!
from pygame import *

#урок 2
from random import randint


# фонова музика
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')
# нам потрібні такі картинки:
img_back = "galaxy.jpg" # фон гри
img_hero = "дива_-removebg-preview (1).png" # герой



#урок 2
# шрифти і написи
font.init()
font2 = font.Font(None, 36)
img_enemy = "ufo.png" # ворог
score = 0 # збито кораблів
lost = 0 # пропущено кораблів



# клас-батько для інших спрайтів
class GameSprite(sprite.Sprite):
    # конструктор класу
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
    # викликаємо конструктор класу (Sprite):
        sprite.Sprite.__init__(self)
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    # метод, що малює героя на вікні
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
# клас головного гравця
class Player(GameSprite):
    # метод для керування спрайтом стрілками клавіатури
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_height - 80:
            self.rect.x += self.speed
    # метод "постріл" (використовуємо місце гравця, щоб створити там кулю)
    def fire(self):
        #-----------------------------------------------------
        #3 instead of pass
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)
        #----------------------------------------------------------


#урок 2
# клас спрайта-ворога
class Enemy(GameSprite):
    # рух ворога
    def update(self):
        self.rect.x -= self.speed
        global lost
        # зникає, якщо дійде до краю екрана
        if self.rect.x > win_width:
            self.rect.y = randint(80, win_height - 80)
            self.rect.x = 0
            lost = lost + 1




#-----------------------------------------------------------------------
# урок 3
# шрифти і написи
font1 = font.Font(None, 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))
# додамо картинку куль
img_bullet = "bullet.png" # куля
img_ast = "asteroid.png" # астероїд
max_lost = 3 # програли, якщо пропустили стільки
# клас спрайта-кулі
class Bullet(GameSprite):
    # рух ворога
    def update(self):
        self.rect.x -= self.speed
    # зникає, якщо дійде до краю екрана
        if self.rect.x < 0:
            self.kill()
# Створити групу для куль
bullets = sprite.Group()
# створення групи спрайтів-астероїдів
asteroids = sprite.Group()
for i in range(1, 2):
    asteroid = Enemy(img_ast, randint(30, 670), -40, 80, 50, randint(1, 7))
    asteroids.add(asteroid)
#--------------------------------------------------------------------------------



# створюємо віконце
win_width = 1250
win_height = 700
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
# створюємо спрайти
ship = Player(img_hero, 5, win_height - 100, 80, 100,20)



#урок 3
# change count of monsters 
monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy(img_enemy, 690, randint(80, win_height - 80), 80, 50, randint(1, 5))
    monsters.add(monster)


#-----------------------------
#4
life = 3  # кількість життів
goal = 10 # стільки кораблів потрібно збити для перемоги
#-----------------------------------

# змінна "гра закінчилася": як тільки вона стає True, в основному циклі перестають працювати спрайти
finish = False
# Основний цикл гри:
run = True # прапорець скидається кнопкою закриття вікна
while run:
# подія натискання на кнопку Закрити
    for e in event.get():
        if e.type == QUIT:
            run = False
#---------------------------------------------------------------
        #3 подія натискання на пробіл - спрайт стріляє
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                ship.fire()
#-------------------------------------------------------------------


    if not finish:
        # оновлюємо фон
        window.blit(background, (0, 0))

        #----------------------------------------------
        #4
        # якщо спрайт торкнувся ворога зменшує життя
        if sprite.spritecollide(ship, monsters, False):
            sprite.spritecollide(ship, monsters, True) 
            life = life -1
        # якщо спрайт торкнувся астероїда плюс життя
        if sprite.spritecollide(ship, asteroids, False):
            sprite.spritecollide(ship, asteroids, True)
            life = life + 1        

        #програш
        if life == 0 or lost >= max_lost:
            finish = True # проиграли, ставим фон и больше не управляем спрайтами.
            window.blit(lose, (200, 200))

        # перевірка виграшу: скільки очок набрали?
        if score >= goal:
            finish = True
            window.blit(win, (200, 200))
                # задаємо різний колір залежно від кількості життів
        #------------------------------------------



        
        #урок2
        # пишемо текст на екрані
        text = font2.render("Рахунок: " + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))
        text_lose = font2.render("Пропущено: " + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))
        # рухи спрайтів
        ship.update()
        #урок2
        monsters.update()
        #3---------------
        bullets.update()
        asteroids.update()
        # оновлюємо їх у новому місці при кожній ітерації циклу
        ship.reset()
        #урок2
        monsters.draw(window)



        #3-----------------
        bullets.draw(window)
        asteroids.draw(window)
        #перевірка зіткнення кулі та монстрів (і монстр, і куля при дотику зникають)
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            #Цей цикл повториться стільки разів, скільки монстрів підбито
            score = score + 1
            
            monster = Enemy(img_enemy, 690, randint(80, win_height - 80), 80, 50, randint(1, 5))
            monsters.add(monster)


    #-----------------------------
    #4
        if life == 3:
            life_color = (0, 150, 0)
        if life == 2:
            life_color = (150, 150, 0)
        if life == 1:
            life_color = (150, 0, 0)

        
        text_life = font1.render(str(life), 1, life_color)
        window.blit(text_life, (650, 10))
    #-------------------------------------    
        display.update()

#бонус: автоматичний перезапуск гри
    else:
        finish = False
        score = 0
        lost = 0
        num_fire = 0
        life = 3
        for b in bullets:
            b.kill()
        for m in monsters:
            m.kill()
        for a in asteroids:
            a.kill

        time.delay(3000)
        for i in range(1, 6):
            monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)
        for i in range(1, 3):
            asteroid = Enemy(img_ast, randint(30, win_width - 30), -40, 80, 50, randint(1, 7))
            asteroids.add(asteroid)    

    # цикл спрацьовує кожні 0.05 секунд
    time.delay(30)