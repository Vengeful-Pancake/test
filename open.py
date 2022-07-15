import pygame
import win32api
import win32con
import win32gui
import time
import pyttsx3
import speech_recognition
import numpy as np
import cv2

from pygame.locals import *
from tkinter import *
import cv2
 


root = Tk()
scr_w = root.winfo_screenwidth()
scr_h = root.winfo_screenheight()

transparency = (255, 0, 128)  # Transparency color

pygame.init()

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN) # For borderless, use pygame.NOFRAME
pygame.display.set_caption("Z-Wings")
font = pygame.font.Font("font\coders_crux.ttf", 40)
fullscreen = True
run = 1

hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*transparency), 0, win32con.LWA_COLORKEY)





def img(x,y,z):
    global scr_w, scr_h
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
    return w, h, img_resize
    

def text(texter):
    global scr_h, scr_w, font, screen
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
    text("rep")
    w, h, img_resize = img(tolx, toly, 'img/sprite.png')
    screen.blit(img_resize,scr_w - w, scr_h - h)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(scr_w-tolx, scr_h-toly, tolx, toly),1)
    pygame.display.update()
