import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    ko_img = pg.image.load("ex01/fig/3.png")
    ko_img = pg.transform.flip(ko_img,True,False)
    ko2_img = pg.transform.rotozoom(ko_img,10,1.0)
    img_lst = [ko_img,ko2_img]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])
        if tmr % 2 == 1:
            screen.blit(ko_img,[300,200])
        else:
            screen.blit(ko2_img,[300,200])
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()