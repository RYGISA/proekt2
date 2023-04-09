from pygame import *
#створи вікно гри
window = display.set_mode((700, 500))
display.set_caption("Doganyalki")
background =  transform.scale(image.load("1653494054_12-celes-club-p-fon-kliker-krasivie-12.png"), (700, 500))
x1 = 100
y1 = 300

x2 = 200
y2 = 300
#задай фон сцени
sprite1 = transform.scale(image.load('sprite1.png'), (100, 100))
#створи 2 спрайти та розмісти їх на сцені
sprite2 = transform.scale(image.load('sprite2.png'), (100, 100))
#оброби подію «клік за кнопкою "Закрити вікно"»
speed = 10

run = True
clock = time.Clock()

FPS = 144
while run:
    window.blit(background,(0,0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    for e in event.get():
        if e.type == QUIT:
            run = False 
    keys_pressed = key.get_pressed()
    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += speed
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 395:
        y1 += speed

    if keys_pressed[K_a] and x2 > 5:
        x2 -= speed
    if keys_pressed[K_d] and x2 < 595:
        x2 += speed
    if keys_pressed[K_w] and y2 > 5:
        y2 -= speed
    if keys_pressed[K_s] and y2 < 395:
        y2 += speed

    display.update()
    clock.tick(FPS)
    