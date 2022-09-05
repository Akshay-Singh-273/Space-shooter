from sup_functions import *
from graphics import *
import keyboard
from pygame import *
import random

winx,winy = 700, 700
win = GraphWin("Model", winx, winy, autoflush=False)

press_start = Image(Point(350,350),"start-game.gif")
press_start.draw(win)
win.getKey()
press_start.undraw()
instructions = Text(Point(350,350),"Controls : w,a,s,d\npress h to shoot")
instructions.setSize(26)
instructions.setStyle("bold")
instructions.draw(win)
win.getKey()

x = 300
y = 600
es_width = 80
es_height = 70
player_width = 130
player_height = 130
player_point = Point(x,y)
i = 1
M = 3
frame = 0
score = 0

es_frame = 0
s1 = 0
s2 = 0
smol_enmy1_fire = 0
smol_enmy2_fire = 0

player_bullet1_Y = -30
player_bullet2_Y = -30

es1_life = 1
es2_life = 1
h_rad = 1

player_lives = 3
player_immunity = 0
player_frame_count = 0
player_hit_conf = 0
bullet1_hit = 1
bullet2_hit = 1

life1 = Image(Point(35,26), "life_1.gif")
life2 = Image(Point(35,66), "life_1.gif")
life3 = Image(Point(35,106), "life_1.gif")
life11 = Image(Point(35,26), "life_2.gif")
life12 = Image(Point(35,66), "life_2.gif")
life13 = Image(Point(35,106), "life_2.gif")

background_anchor = Point(winx/2, winy/2)
background = Image(background_anchor, "background_1.gif")
background.draw(win)

es1 = Image(Point(200,-30), "small_enemy_1.gif")
es2 = Image(Point(300,-30), "small_enemy_1.gif")

smol_enmy1_bullet = Image(Point(200,-30), "bullet_type_1.gif")
smol_enmy2_bullet = Image(Point(200,-30), "bullet_type_1.gif")

es_frame, s1, s2, es1, es2, h_rad, es1_life, es2_life, player_lives, score = Small_enemy(0, 0, 0, es1, es2, -36, -36, h_rad, 1, 1, player_lives, es_width, es_height, Point(-100,-100), Point(-100,-100), Point(-100,-100), Point(-100,-100), 0, score, win)

player = Image(player_point, "player_1.gif")
player = Player_gif(player_frame_count, player, player_point, win)

player_bullet1 = Image(Point(0,-30), "bullet_1.gif")
player_bullet2 = Image(Point(0,-30), "bullet_1.gif")

mixer.init()
player_bullet_sound = mixer.Sound('player_bullet.wav')
mixer.music.load('stage1_music.mp3')
mixer.music.play(-1)

while(player_lives > 0):
    update(60)

    frame += 1
    if(frame == 61):
        frame = 1

    Life_display(player_lives, life1, life2, life3, life11, life12, life13, frame, win)
    
    background_anchor = background.getAnchor()
    background_X = background_anchor.getX()
    background_Y = background_anchor.getY()

    es1_anchor = es1.getAnchor()
    es1_Y = es1_anchor.getY()
    es1_X = es1_anchor.getX()
    es2_anchor = es2.getAnchor()
    es2_Y = es2_anchor.getY()
    es2_X = es2_anchor.getX()
    
    player_anchor = player.getAnchor()
    player_X = player_anchor.getX()
    player_Y = player_anchor.getY()

    player_bullet1_anchor = player_bullet1.getAnchor()
    player_bullet1_Y = player_bullet1_anchor.getY()
    player_bullet2_anchor = player_bullet2.getAnchor()
    player_bullet2_Y = player_bullet2_anchor.getY()

    smol_enmy1_fire_anchor = smol_enmy1_bullet.getAnchor()
    bullet1_Y = smol_enmy1_fire_anchor.getY()
    smol_enmy2_fire_anchor = smol_enmy2_bullet.getAnchor()
    bullet2_Y = smol_enmy2_fire_anchor.getY()
    

   # background = Background_gif(frame, background, background_anchor, win)
    
    es_frame += 1
    s_enemy_spawn = random.randint(1,100)
    s_enemy1_fire = random.randint(1,70)
    s_enemy2_fire = random.randint(1,70)
    es_frame, s1, s2, es1, es2, h_rad, es1_life, es2_life, player_lives, score = Small_enemy(es_frame, s1, s2, es1, es2, es1_Y, es2_Y, h_rad, es1_life, es2_life, player_lives, es_width, es_height, es1_anchor, es2_anchor, player_bullet1, player_bullet2, s_enemy_spawn, score, win)
    smol_enmy1_fire, smol_enmy1_bullet, bullet1_Y = enemy_fire(s1, es1_X, es1_Y, smol_enmy1_fire, s_enemy1_fire, smol_enmy1_bullet, bullet1_Y, win)
    smol_enmy2_fire, smol_enmy2_bullet, bullet2_Y = enemy_fire(s2, es2_X, es2_Y, smol_enmy2_fire, s_enemy2_fire, smol_enmy2_bullet, bullet2_Y, win)
    
    if(es_frame == 8):
        es_frame = 1
    
    player_frame_count += 1
    player = Player_gif(player_frame_count, player, player_anchor, win)

    if(player_frame_count == 8):
        player_frame_count = 1

    if(player_immunity > 0):
        player_immunity -= 1
    if(player_immunity == 0):
        player_lives, player_hit_conf, player_immunity = Collision(smol_enmy1_bullet, player_anchor, 130, 130, player_lives, player_immunity, 1)
        player_lives, player_hit_conf, player_immunity = Collision(smol_enmy2_bullet, player_anchor, 130, 130, player_lives, player_immunity, 1)

    if(keyboard.is_pressed('h')):
        if(player_bullet1_Y < -5):
            player_bullet1.undraw()
            player_bullet1 = Image(Point(player_X, (player_Y - player_height / 2)), "bullet_1.gif")
            player_bullet1.draw(win)
            player_bullet_sound.play()
            timer = frame
        if(frame == timer + 30):
            player_bullet2.undraw()
            player_bullet2 = Image(Point(player_X, (player_Y - player_height / 2)), "bullet_1.gif")
            player_bullet2.draw(win)
            player_bullet_sound.play()

    player_bullet1.move(0,-40)
    player_bullet2.move(0,-40)

    if(keyboard.is_pressed('d')):
        if((player_X + (player_width / 2)) < 693):
            if(keyboard.is_pressed('w') and (player_Y - (player_height / 2)) > 4):
                mx=4
                my=-4
                player.move(mx,my)
                if(background_X > 310 and background_Y < 390):
                    background.move(-1,1)
                
            elif(keyboard.is_pressed('s') and (player_Y + (player_height / 2) - 40) < 693):
                mx=4
                my=4
                player.move(mx,my)
                if(background_X > 310 and background_Y > 310):
                    background.move(-1,-1)
                
            else:
                mx=6
                my=0
                player.move(mx,my)
                if(background_X > 310):
                    background.move(-1,0)
                
        else:
            continue

    elif(keyboard.is_pressed('w')):
        if((player_Y - (player_height / 2)) > 4):
            if(keyboard.is_pressed('d') and (player_X + (player_width / 2)) < 693):
                mx=4
                my=-4
                player.move(mx,my)
                if(background_X > 310 and background_Y < 390):
                    background.move(-1,1)
                
            elif(keyboard.is_pressed('a') and (player_X - (player_width / 2)) > 4):
                mx=-4
                my=-4
                player.move(mx,my)
                if(background_X < 390 and background_Y < 390):
                    background.move(1,1)
                    
            else:
                mx=0
                my=-6
                player.move(mx,my)
                if(background_Y < 390):
                    background.move(0,1)
        
        else:
            continue

    elif(keyboard.is_pressed('a')):
        if((player_X - (player_width / 2)) > 4):
            if(keyboard.is_pressed('s') and (player_Y + (player_height / 2) - 40) < 693):
                mx=-4
                my=4
                player.move(mx,my)
                if(background_X < 390 and background_Y > 310):
                    background.move(1,-1)
                
            elif(keyboard.is_pressed('w') and (player_Y - (player_height / 2)) > 4):
                mx=-4
                my=-4
                player.move(mx,my)
                if(background_X < 390 and background_Y < 390):
                    background.move(1,1)
                
            else:
                mx=-6
                my=0
                player.move(mx,my)
                if(background_X < 390):
                    background.move(1,0)
                
        else:
            continue

    elif(keyboard.is_pressed('s')):
        if((player_Y + (player_height / 2) - 40) < 693):
            if(keyboard.is_pressed('a') and (player_X - (player_width / 2)) > 4):
                mx=-4
                my=4
                player.move(mx,my)
                if(background_X < 390 and background_Y > 310):
                    background.move(1,-1)
                
            elif(keyboard.is_pressed('d') and (player_X + (player_width / 2)) < 693):
                mx=4
                my=4
                player.move(mx,my)
                if(background_X > 310 and background_Y > 310):
                    background.move(-1,-1)
                
            else:
                mx=0
                my=6
                player.move(mx,my)
                if(background_Y > 310):
                    background.move(0,-1)
        else:
            continue
gameover = Image(Point(350,350), "gameover.gif")
gameover.draw(win)
win.setBackground("black")
background.undraw()
es1.undraw()
es2.undraw()
player.undraw()
player_bullet1.undraw()
player_bullet2.undraw()
message = Text(Point(350,600),"SCORE:")
score = Text(Point(400,600),score)
message.setTextColor("grey")
score.setTextColor("grey")
message.setStyle("bold")
score.setStyle("bold")
message.draw(win)
score.draw(win)
win.getKey()
win.close()
