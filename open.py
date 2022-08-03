import pygame
import win32api
import win32con
import win32gui
import time
import pyttsx3
import speech_recognition
import numpy as np
import cv2

from image import Image
from pygame.locals import *
from tkinter import *
 

#find screen height and width
root = Tk()
scr_w = root.winfo_screenwidth()
scr_h = root.winfo_screenheight()

#start library pygame 
pygame.init()

# For borderless, use pygame.NOFRAME
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN) 
clock = pygame.time.Clock()
# Transparency color
transparency = (255, 0, 128)  
pygame.display.set_caption("Z-Wings")
font = pygame.font.Font("font\coders_crux.ttf", 40)
fullscreen = True
run = 1
#neccessary for transparant screen, add layer
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*transparency), 0, win32con.LWA_COLORKEY)

#function to put sprite
def img(x,y,z,scr_h,scr_w,i):
    if not i:
        # read image
        img = pygame.image.load(z)
        # height, width of image
        height = img.get_height()
        width = img.get_width()
        o = 1
        h=height
        while h > y:
            o = o - 0.01
            w = width * o
            h = height * o
            img_resize = pygame.transform.scale(img, (w, h))
        # while h < y:
        #     o = o - 0.01
        #     w = width * o
        #     h = height * o
        #     img_resize = pygame.transform.scale(img, (w, h))
        textRect = img_resize.get_rect()

        #w/16, h/7.5 is the width between eadge
        textRect.center = (scr_w-w/2-w/16, scr_h-h/2-h/7.5)
        screen.blit(img_resize,textRect)
        return
    
    return 1
    
#function to put text
def text(texter, scr_h, scr_w, font):
    global screen
    text = font.render(texter, True, (0,0,0), (100,10,255))
    textRect = text.get_rect()
    textRect.center = (scr_w // 2, scr_h // 2)
    screen.blit(text, textRect)
    return

while run:
    tolx = scr_w/2
    toly = scr_h/4
    check = 0
    screen.fill(transparency)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0
        if event.type == KEYDOWN:
            if event.key == K_F11:
                if fullscreen and not check:
                    scr_w = 1600
                    scr_h = 900
                    screen = pygame.display.set_mode((scr_w, scr_h))
                    fullscreen = False
                    check = 1
                    time.sleep(0.1)
                if not fullscreen and not check:
                    scr_w = root.winfo_screenwidth()
                    scr_h = root.winfo_screenheight()
                    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
                    fullscreen = True
                    time.sleep(0.1)
                    check = 1
    
    text("test text, this text should not disappear at anytime!!!", scr_h, scr_w, font)
    
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(scr_w-tolx, scr_h-toly, tolx, toly),1)
    img(tolx, toly, 'img/sprite.png', scr_h, scr_w, 0)
    
    pygame.display.update()
    clock.tick(60)
