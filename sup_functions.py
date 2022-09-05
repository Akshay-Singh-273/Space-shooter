from graphics import *
from math import*
import random
from pygame import *

def Life_display(life, life1, life2, life3, life11, life12, life13, frame, win):
    if(frame == 1 and life <= 3):
        if(life == 3):
            life1.draw(win)
            life2.draw(win)
            life3.draw(win)
            life11.undraw()
            life12.undraw()
            life13.undraw()
        elif(life == 2):
            life1.draw(win)
            life2.draw(win)
            life3.undraw()
            life11.undraw()
            life12.undraw()
            life13.undraw()
        elif(life == 1):
            life1.draw(win)
            life2.undraw()
            life3.undraw()
            life11.undraw()
            life12.undraw()
            life13.undraw()
    elif(frame == 31 and life <= 3):
        if(life == 3):
            life11.draw(win)
            life12.draw(win)
            life13.draw(win)
            life1.undraw()
            life2.undraw()
            life3.undraw()
        elif(life == 2):
            life11.draw(win)
            life12.draw(win)
            life13.undraw()
            life1.undraw()
            life2.undraw()
            life3.undraw()
        elif(life == 1):
            life11.draw(win)
            life12.undraw()
            life13.undraw()
            life1.undraw()
            life2.undraw()
            life3.undraw()

def Collision(obj, mid_point, width, height, life, immunity, entity_type):
    incident_P = obj.getAnchor()
    P_X = incident_P.getX()
    P_Y = incident_P.getY()
    M_X = mid_point.getX()
    M_Y = mid_point.getY()
    w = width/2
    h = height/2
    hit = 0

    if(P_X > (M_X - w) and P_X < (M_X + w) and P_Y > (M_Y - h) and P_Y < (M_Y + h)):
         life-=1
         immunity = 60
         hit = 1
    if(entity_type == 1):
        return life, hit, immunity
    elif(entity_type == 0):
        return life

def Player_bullet(bullet_type, bullet1, bullet1_Y, bullet2, bullet2_Y, player_X, player_Y, frame, timer, win):
    if(bullet1_hit == 1 ):
        bullet1 = Image(Point(player_X,(player_Y - 65)), "bullet_1.gif")
        bullet1.draw(win)
        mixer.init()
        bullet_sound = mixer.Sound('player_bullet.wav')
        bullet_sound.play()
        timer = frame
        bullet1_hit = 0
    if(frame == timer + 30 and bullet2_hit == 1):
        bullet2 = Image(Point(player_X,(player_Y - 65)), "bullet_1.gif")
        bullet2.draw(win)
        mixer.init()
        bullet_sound = mixer.Sound('player_bullet.wav')
        bullet_sound.play()
        bullet2_hit = 0

def enemy_fire(enemy_spawn, enemy_X, enemy_Y, bullet_fired, trigger, bullet, bullet_Y, win):
    if(enemy_spawn == 1 and bullet_fired == 0 and trigger == 1):
        bullet_X = enemy_X
        bullet_Y = enemy_Y
        mixer.init()
        bullet_sound = mixer.Sound('pew_pew.mp3')
        bullet = Image(Point(bullet_X, bullet_Y), "bullet_type_1.gif")
        bullet.draw(win)
        bullet_sound.play()
        bullet_fired = 1
    if(bullet_fired == 1):
        if(bullet_Y > 700):
            bullet_fired = 0
            bullet.undraw()
        else:
            bullet.move(0,15)       #add collision check
    return bullet_fired, bullet, bullet_Y

def Enemy_S_gif(frame, enemy, mode, enemy_anchor, win):
    if(mode == 0):
        enemy.undraw()
        enemy = Image(enemy_anchor, "small_enemy_1.gif")
        enemy.draw(win)
        return enemy, enemy_anchor
    if(mode == 1):
        if(frame == 2):
            enemy.undraw()
            enemy = Image(enemy_anchor, "small_enemy_1.gif")
            enemy.draw(win)
        elif(frame == 4):
            enemy.undraw()
            enemy = Image(enemy_anchor, "small_enemy_2.gif")
            enemy.draw(win)
        elif(frame == 6):
            enemy.undraw()
            enemy = Image(enemy_anchor, "small_enemy_3.gif")
            enemy.draw(win)
        elif(frame == 8):
            enemy.undraw()
            enemy = Image(enemy_anchor, "small_enemy_4.gif")
            enemy.draw(win)
        return enemy

def Small_enemy(es_frame, s1, s2, es1, es2, es1_Y, es2_Y, h_rad, es1_life, es2_life, player_lives, es_width, es_height, es1_anchor, es2_anchor, bullet1, bullet2, randm, score, win):
    if(s1 == 0 and randm == 7):
        s1 = 1
        es1_life = 1
        es1, es1_anchor = Enemy_S_gif(es_frame, es1, 0, es1_anchor, win)
    if(s2 == 0 and randm == 6):
        s2 = 1
        es2_life = 1
        es2, es2_anchor = Enemy_S_gif(es_frame, es2, 0, es2_anchor, win)
    if(s1 == 1 and es1_life == 1):
        dx1 = 8 * sin(radians(h_rad))
        h_rad += 0.5
        es1.move(dx1, 8)
        es1 = Enemy_S_gif(es_frame, es1, 1, es1_anchor, win)
        es1_life = Collision(bullet1, es1_anchor, es_width, es_height, 1, 0, 0)
        if(es1_life == 1):
            es1_life = Collision(bullet2, es1_anchor, es_width, es_height, 1, 0, 0)
        if(es1_Y > 736 or es1_life == 0):
            s1 = 0
            if(es1_life == 0):
                score += 100
            es1.undraw()
            es1_X = random.randint(150,550)
            es1_Y = -36
            es1, es1_anchor = Enemy_S_gif(es_frame, es1, 0, Point(es1_X,es1_Y), win)
            
    if(s2 == 1 and es2_life == 1):
        dx2 = 5 * sin(radians(h_rad))
        h_rad += 0.5
        es2.move(dx2, 5)
        es2 = Enemy_S_gif(es_frame, es2, 1, es2_anchor, win)
        es2_life = Collision(bullet1, es2_anchor, es_width, es_height, 1, 0, 0)
        if(es2_life == 1):
            es2_life = Collision(bullet2, es2_anchor, es_width, es_height, 1, 0, 0)
        if(es2_Y > 736 or es2_life == 0):
            s2 = 0
            if(es2_life == 0):
                score += 100
            es2.undraw()
            es2_X = random.randint(100,600)
            es2_Y = -36
            es2, es2_anchor = Enemy_S_gif(es_frame, es2, 0, Point(es2_X,es2_Y), win)

    return  es_frame, s1, s2, es1, es2, h_rad, es1_life, es2_life, player_lives, score

def Background_gif(frame, background, background_anchor, win):
    if(frame == 0):
        background.anchordraw(win)
    elif(frame == 1):
        background.undraw()
        background = Image(background_anchor, "1.gif")
        background.draw(win)
    elif(frame == 7):
        background.undraw()
        background = Image(background_anchor, "2.gif")
        background.draw(win)
    elif(frame == 13):
        background.undraw()
        background = Image(background_anchor, "3.gif")
        background.draw(win)
    elif(frame == 19):
        background.undraw()
        background = Image(background_anchor, "4.gif")
        background.draw(win)
    elif(frame == 25):
        background.undraw()
        background = Image(background_anchor, "5.gif")
        background.draw(win)
    elif(frame == 31):
        background.undraw()
        background = Image(background_anchor, "6.gif")
        background.draw(win)
    elif(frame == 37):
        background.undraw()
        background = Image(background_anchor, "7.gif")
        background.draw(win)
    elif(frame == 43):
        background.undraw()
        background = Image(background_anchor, "8.gif")
        background.draw(win)
    elif(frame == 49):
        background.undraw()
        background = Image(background_anchor, "9.gif")
        background.draw(win)
    elif(frame == 55):
        background.undraw()
        background = Image(background_anchor, "10.gif")
        background.draw(win)
    return background

def Player_gif(frame, player, player_anchor, win):
    if(frame == 0):
        player.draw(win)
    elif(frame == 2):
        player.undraw()
        player = Image(player_anchor, "player_1.gif")
        player.draw(win)
    elif(frame == 4):
        player.undraw()
        player = Image(player_anchor, "player_2.gif")
        player.draw(win)
    elif(frame == 6):
        player.undraw()
        player = Image(player_anchor, "player_3.gif")
        player.draw(win)
    elif(frame == 8):
        player.undraw()
        player = Image(player_anchor, "player_4.gif")
        player.draw(win)
    return player

def Bullet_gif(bullet_type, bullet_frame, frame, bullet_anchor, bullet, win):
    if(bullet_type == 1):
        if(bullet_frame == frame - 2):
            bullet.undraw()
            bullet = Image(bullet_anchor, "bullet_3.gif")
            bullet.draw(win)
        elif(bullet_frame == frame - 4):
            bullet.undraw()
            bullet = Image(bullet_anchor, "bullet_4.gif")
            bullet.draw(win)
        elif(bullet_frame == frame - 6):
            bullet.undraw()
            bullet = Image(bullet_anchor, "bullet_5.gif")
            bullet.draw(win)
        elif(bullet_frame == frame - 8):
            bullet.undraw()
            bullet = Image(bullet_anchor, "bullet_6.gif")
            bullet.draw(win)
        elif(bullet_frame == frame - 9):
            bullet.undraw()
            hit_conf = 0
    return bullet
