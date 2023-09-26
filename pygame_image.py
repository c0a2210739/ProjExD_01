import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg2_img = pg.transform.flip(bg_img,True,False)
    ko_img = pg.image.load("ex01/fig/3.png")
    ko_img = pg.transform.flip(ko_img,True,False)
    ko2_img = pg.transform.rotozoom(ko_img,10,1.0)
    ko3_img = pg.transform.rotozoom(ko_img,7,1.0)
    ko4_img = pg.transform.rotozoom(ko_img,5,1.0)
    ko5_img = pg.transform.rotozoom(ko_img,3,1.0)
    img_lst = [ko_img,ko2_img,ko3_img,ko4_img,ko5_img]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%1600
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg2_img,[1600-x,0])
        screen.blit(bg2_img,[1600-x,0])
        screen.blit(img_lst[tmr%2],[300,200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()