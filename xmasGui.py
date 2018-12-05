#My GUI Interface
import datetime
from Tkinter import *
import sys
import pygame
import random
import time

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)

def setOffGPIO():
    GPIO.output(29,GPIO.LOW)
    GPIO.output(31,GPIO.LOW)
    GPIO.output(33,GPIO.LOW)
    GPIO.output(35,GPIO.LOW)
    GPIO.output(37,GPIO.LOW)
    GPIO.output(38,GPIO.LOW)
    GPIO.output(36,GPIO.LOW)
    GPIO.output(40,GPIO.LOW)
    GPIO.cleanup
def setOnGPIO():
    GPIO.output(29,GPIO.HIGH)
    GPIO.output(31,GPIO.HIGH)
    GPIO.output(33,GPIO.HIGH)
    GPIO.output(35,GPIO.HIGH)
    GPIO.output(37,GPIO.HIGH)
    GPIO.output(38,GPIO.HIGH)
    GPIO.output(36,GPIO.HIGH)
    GPIO.output(40,GPIO.HIGH)
    GPIO.cleanup
setOffGPIO()
#======================================================
mw = Tk()
#======================================================
def PlayMusic(intLoop,strMusicFile):
    #for x in range(0,3):
    pygame.mixer.init()
    pygame.mixer.music.load(strMusicFile)
    #pygame.mixer.music.load("/home/pi/Music/12daysxmas.mid")
    #pygame.mixer.music.load("/home/pi/Music/Trans-Siberian_Orchestra_.mid")
    #pygame.mixer.music.set_endevent(pygame.constants.USERVENT)
    pygame.mixer.music.play(intLoop)
    #while pygame.mixer.music.get_busy() == True:
    #       print ('start GPIO CODE HERE')
     
    #continue

#CREATE BUTTON HERE
def button(msg,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()
    if h+w > mouse[0] > x and y+50 > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

#======================================================
#Create color array
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 180, 0)
RED = (255, 0, 0)
BRIGHT_GREEN = (0, 255, 0)
#create LED simulation Color
GPIOC = [WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE]
#======================================================
#Open Pygame
#======================================================

def openPygame(intMusicLoop,strMusicFile,intSystemOffCounter,StopTime,StartTime):

    PlayMusic(intMusicLoop,strMusicFile)
    #set pygame loop
    LightLoop = intMusicLoop
    pygame.init()
    # set the width and height
    size = (400, 400)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("My XMAS GUI")
    
    def LNoteA(ch1,ch2,ch3,ch4,ch5,ch6,ch7,ch8):
        if ch1 == 1:
            GPIO.output(29, GPIO.HIGH)
        else:
            GPIO.output(29, GPIO.LOW)
            
        if ch2 == 1:
            GPIO.output(31, GPIO.HIGH)
        else:
            GPIO.output(31, GPIO.LOW)
            
        if ch3 == 1:
            GPIO.output(33, GPIO.HIGH)
        else:
            GPIO.output(33, GPIO.LOW)
            
        if ch4 == 1:
            GPIO.output(35, GPIO.HIGH)
        else:
            GPIO.output(35, GPIO.LOW)
            
        if ch5 == 1:
            GPIO.output(37, GPIO.HIGH)
        else:
            GPIO.output(37, GPIO.LOW)
            
        if ch6 == 1:
            GPIO.output(38, GPIO.HIGH)
        else:
            GPIO.output(38, GPIO.LOW)
            
        if ch7 == 1:
            GPIO.output(40, GPIO.HIGH)
        else:
            GPIO.output(40, GPIO.LOW)
            
        if ch8 == 1:
            GPIO.output(36, GPIO.HIGH)
        else:
            GPIO.output(36, GPIO.LOW)
        
    # create an empty array
    snow_list = []

    #loop 50 times and add a snow flake in ramdom x, y position
    for i in range(50):
        x = random.randrange(0, 400)
        y = random.randrange(0, 400)
        snow_list.append([x, y])
    #use to manage how fast the screen updates
    clock = pygame.time.Clock()
    #clock tick
    ctick = 10
    
    #switcher counter
    SW = 0
    intMusicIndex = 1
    #SET MUSIC INDEX COUNTER
    intMusicIndxCounter = 0
        
    #loop until user clicks the close button
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                setOffGPIO()  
                done = True

        #if you want background image, replace this clear with a blit'ing the
        #background image
        screen.fill(BLACK)
        #Drawing code here
    
        #snow flakes here
        for i in range(len(snow_list)):
            #draw the snow flake in the list
            pygame.draw.circle(screen, WHITE, snow_list[i], 2)
            # move the snow flake down one pixel
            snow_list[i][1] += 1
            #if snow flake has moved off the bottom of the screen 
            if snow_list[i][1] > 400:
                #reset it just above the top
                y = random.randrange(-50, -10)
                snow_list[i][1] = y
                #give it a new x positon
                x = random.randrange(0, 400)
                snow_list[i][0] = x
        #===================================================================        
        #Music #1
        #===================================================================

##        now = datetime.datetime.now()
##        if now.hour == 8:
##           if now.minute == 55:
##                intMusicIndxCounter += 1
##                intMusicIndex = 1
##           else:
##                intMusicIndxCounter = 0
##                intMusicIndex = 0

                
        now = datetime.datetime.now()
        if now.hour == StopTime:
           SW = 0
           intMusicIndex = 12
           intMusicIndxCounter == 9600
        
        intMusicIndxCounter += 1
        if intMusicIndex == 1: 
            SW += 1
            if SW == 1:
                 LNoteA(1,0,0,0,0,0,0,0)
                 GPIOC = [1,0,0,0,0,0,0,0]
                 ctick = 8
            if SW == 4:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,0]
            if SW == 8:
                 LNoteA(1,0,0,0,0,0,0,0)
                 GPIOC = [1,0,0,0,0,0,0,0]
            if SW == 12:
                 LNoteA(0,0,0,0,0,0,0,1)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 14:
                 LNoteA(0,0,0,1,0,0,0,1)
                 GPIOC = [0,0,0,1,0,0,0,1]
            if SW == 20:
                 LNoteA(0,1,0,0,0,1,0,0)
                 GPIOC = [0,1,0,0,0,1,0,0]
                 ctick = 10
            if SW == 24:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,0]
            if SW == 28:
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [1,1,1,1,1,1,1,1]
            if SW == 32:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,0]              
            if SW == 34:
                 LNoteA(0,0,0,1,0,0,0,1)
                 GPIOC = [0,0,0,1,0,0,0,1]
            if SW == 36:
                 LNoteA(0,0,1,0,0,1,0,0)
                 GPIOC = [0,0,1,0,0,1,0,0]
            if SW == 38:
                 LNoteA(0,1,0,0,1,0,0,1)
                 GPIOC = [0,1,0,0,1,0,0,1]
            if SW >= 40:
                 LNoteA(1,0,1,0,1,0,0,0)
                 GPIOC = [1,0,1,0,1,0,0,0]
                 SW = 0
            if intMusicIndxCounter  == 375:
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [1,1,1,1,1,1,1,1]
                 
            if intMusicIndxCounter  == 435:
                 LNoteA(1,1,0,0,0,0,0,0)
                 GPIOC = [1,1,0,0,0,0,0,0]
                 time.sleep(.5)
                 LNoteA(0,0,0,0,0,0,1,1)
                 GPIOC = [0,0,0,0,0,0,1,1]
                 time.sleep(.5)
                 LNoteA(1,1,0,0,0,0,0,0)
                 GPIOC = [1,1,0,0,0,0,0,0]
                 time.sleep(.5)
                 LNoteA(0,0,0,0,0,0,1,1)
                 GPIOC = [0,0,0,0,0,0,1,1]
                 time.sleep(.5)
                 LNoteA(1,1,1,1,0,0,0,0)
                 GPIOC = [1,1,1,1,0,0,0,0]
                 time.sleep(.5)
                 LNoteA(0,0,0,0,1,1,1,1)
                 GPIOC = [0,0,0,0,1,1,1,1]
                 time.sleep(.5)
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,0]
                 time.sleep(.5)
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [1,1,1,1,1,1,1,1]
                 time.sleep(.5)
                 LNoteA(1,1,1,0,0,1,1,1)
                 GPIOC = [1,1,1,0,0,1,1,1]
                 time.sleep(.5)
                 LNoteA(1,1,0,0,0,0,1,1)
                 GPIOC = [1,1,0,0,0,0,1,1]
                 time.sleep(.5)
                 LNoteA(1,0,0,0,0,0,0,1)
                 GPIOC = [1,0,0,0,0,0,0,1]
                 time.sleep(.5)
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,0]
                 time.sleep(.5)
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,0]
                 time.sleep(.5)
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,0]
                 time.sleep(.5)
                 intMusicIndex = 2
                 PlayMusic(1,"/home/pi/Music/Trans-Siberian_Orchestra_.mid")
                 SW = 0
        #=============================================================
        #MUSIC #2
        #=============================================================
        if intMusicIndex == 2: 
            SW += 1
            if SW == 1:
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [1,0,0,0,0,0,0,1]
                 ctick = 50
            if SW == 4:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [0,0,1,0,1,0,0,0]
            if SW == 8:
                 LNoteA(1,0,1,0,1,0,1,0)
                 GPIOC = [1,0,0,0,1,0,0,0]
            if SW == 12:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 14:
                 LNoteA(1,0,0,0,0,0,0,0)
                 GPIOC = [0,0,0,1,0,0,0,1]
            if SW == 16:
                 LNoteA(0,1,0,0,0,0,0,0)
                 GPIOC = [0,0,0,1,0,0,0,1]
            if SW == 18:
                 LNoteA(0,0,1,0,0,0,0,0)
                 GPIOC = [0,0,0,1,0,0,0,1]
            if SW == 20:
                 LNoteA(0,0,0,1,0,0,0,0)
                 GPIOC = [0,0,0,1,0,0,0,1]
            if SW == 22:
                 LNoteA(0,0,0,0,1,0,0,0)
                 GPIOC = [0,0,0,1,0,0,0,1]
            if SW == 24:
                 LNoteA(0,0,0,0,0,1,0,0)
                 GPIOC = [0,0,0,1,0,0,0,1]
            if SW == 26:
                 LNoteA(0,0,0,0,0,0,1,0)
                 GPIOC = [0,1,0,0,0,1,0,0]
            if SW == 28:
                 LNoteA(0,0,0,0,0,0,0,1)
                 GPIOC = [0,1,0,0,0,1,0,0]
            if SW == 30:
                 LNoteA(0,0,0,0,0,0,0,1)
                 GPIOC = [0,1,0,0,0,1,0,0]
            if SW == 32:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [0,1,0,0,0,1,0,0]
            if SW == 34:
                 LNoteA(0,0,0,0,0,0,0,1)
                 GPIOC = [0,1,0,0,0,1,0,0]
            if SW == 36:
                 LNoteA(0,0,0,0,0,0,1,0)
                 GPIOC = [0,1,0,0,0,1,0,0]
            if SW == 38:
                 LNoteA(0,0,0,0,0,1,0,0)
                 GPIOC = [0,1,0,0,0,1,0,0]
            if SW == 40:
                 LNoteA(0,0,0,0,1,0,0,0)
                 GPIOC = [0,1,0,0,0,1,0,0]
            if SW == 42:
                 LNoteA(0,0,0,1,0,0,0,0)
                 GPIOC = [0,1,0,0,0,1,0,0]
            if SW == 44:
                 LNoteA(0,0,1,0,0,0,0,0)
                 GPIOC = [0,1,0,0,0,1,0,0]
            if SW == 46:
                 LNoteA(0,1,0,0,0,0,0,0)
                 GPIOC = [0,1,0,0,0,1,0,0]
            if SW >= 48:
                 LNoteA(1,0,0,0,0,0,0,0)
                 GPIOC = [1,0,1,0,1,0,0,0]
            if SW >= 50:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [1,0,1,0,1,0,0,0]
                 SW = 0
            if intMusicIndxCounter >= 750:
                 intMusicIndex = 3
                 SW = 0
        #=============================================================
        #MUSIC #3 GUITAR START HERE
        #=============================================================
        if intMusicIndex == 3: 
            SW += 1
            if SW == 1:
                 LNoteA(1,0,0,0,0,0,0,1)
                 GPIOC = [1,0,0,0,0,0,0,1]
                 ctick = 10
            if SW == 4:
                 LNoteA(1,0,0,1,0,1,0,0)
                 GPIOC = [0,0,1,0,1,0,0,0]
            if SW == 8:
                 LNoteA(1,0,1,0,0,1,0,1)
                 GPIOC = [1,0,0,0,1,0,0,0]
            if SW == 12:
                 LNoteA(0,0,1,0,1,0,0,1)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 14:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [0,0,0,1,0,0,0,1]
            if SW == 20:
                 LNoteA(0,1,0,0,0,1,0,0)
                 GPIOC = [0,1,0,0,0,1,0,0]
            if SW == 30:
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [0,1,0,0,0,1,0,0]
            if SW >= 40:
                 LNoteA(1,0,1,0,1,0,0,0)
                 GPIOC = [1,0,1,0,1,0,0,0]
                 SW = 0
            if intMusicIndxCounter >= 800:
                 intMusicIndex = 4
                 SW = 0
                 print ('PIANO ')
        #=============================================================
        #MUSIC #4 FAST
        #=============================================================
        if intMusicIndex == 4: 
            SW += 1
            if SW == 1:
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [1,0,0,0,0,0,0,1]
                 ctick = 50
            if SW == 3:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [1,0,0,0,0,0,0,1]
            if SW == 5:
                 LNoteA(0,0,0,1,0,1,0,0)
                 GPIOC = [0,0,1,0,1,0,0,0]
            if SW == 8:
                 LNoteA(1,0,1,0,0,1,0,0)
                 GPIOC = [1,0,0,0,1,0,0,0]
            if SW == 12:
                 LNoteA(0,0,0,0,0,0,0,1)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 14:
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [0,0,0,1,0,0,0,1]
            if SW == 20:
                 LNoteA(0,1,0,0,0,1,0,0)
                 GPIOC = [0,1,0,0,0,1,0,0]
            if SW == 24:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,0]
            if SW >= 28:
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [1,0,1,0,1,0,0,0]
            if SW >= 30:
                 LNoteA(1,0,1,0,1,0,1,0)
                 GPIOC = [1,0,1,0,1,0,0,0]
            if SW >= 34:
                 LNoteA(0,1,0,1,0,1,0,1)
                 GPIOC = [1,0,1,0,1,0,0,0]
                 SW = 0
            if intMusicIndxCounter >= 980:
                 intMusicIndex = 5
                 SW = 0
        #=============================================================
        #MUSIC #5 FAST
        #=============================================================
        if intMusicIndex == 5: 
            SW += 1
            if SW == 1:
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [1,0,0,0,0,0,0,1]
                 ctick = 50
            if SW == 4:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [0,0,1,0,1,0,0,0]
            if SW == 8:
                 LNoteA(1,0,1,0,1,0,1,0)
                 GPIOC = [1,0,0,0,1,0,0,0]
            if SW == 12:
                 LNoteA(0,1,0,1,0,1,0,1)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW >= 14:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [1,0,1,0,1,0,0,0]
                 SW = 0
            if intMusicIndxCounter == 1250 or intMusicIndxCounter == 1280 \
                 or intMusicIndxCounter == 1325 or intMusicIndxCounter == 1335 \
                 or intMusicIndxCounter == 1438 or intMusicIndxCounter == 1402 \
                 or intMusicIndxCounter == 1405 or intMusicIndxCounter == 1408:
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [1,0,1,0,1,0,0,0]
                 time.sleep(.5)
                 LNoteA(0,0,0,0,0,0,0,0)
            if intMusicIndxCounter >= 1570:
                 intMusicIndex = 6
                 SW = 0
        #=============================================================
        #MUSIC #6 FAST
        #=============================================================
        if intMusicIndex == 6: 
            SW += 1
            if SW == 1:
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [1,0,0,0,0,0,0,1]
                 ctick = 50
            if SW == 3:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [0,0,1,0,1,0,0,0]
            if SW == 5:
                 LNoteA(1,0,1,0,1,0,1,0)
                 GPIOC = [1,0,0,0,1,0,0,0]
            if SW == 8:
                 LNoteA(0,1,0,1,0,1,0,1)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW >= 11:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [1,0,1,0,1,0,0,0]
                 SW = 0
            
            if intMusicIndxCounter == 2730:
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [1,0,1,0,1,0,0,0]
                 time.sleep(.5)
                 LNoteA(0,0,0,0,0,0,0,0)
            if intMusicIndxCounter >= 2500:
                 intMusicIndex = 7
                 SW = 0
        #=============================================================
        #MUSIC #7 FAST
        #=============================================================
        if intMusicIndex == 7: 
            SW += 1
            if intMusicIndxCounter == 2500:
                 ctick = 30
            if SW == 1:
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [1,0,0,0,0,0,0,1]
            if SW == 10:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [0,0,1,0,1,0,0,0]
            if SW == 12:
                 LNoteA(1,0,1,0,1,0,1,0)
                 GPIOC = [1,0,0,0,1,0,0,0]
            if SW == 14:
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 16:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 18:
                 LNoteA(1,0,0,0,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 20:
                 LNoteA(0,0,1,0,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 22:
                 LNoteA(0,0,0,0,1,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 24:
                 LNoteA(0,0,0,0,0,0,1,0)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 26:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 28:
                 LNoteA(0,0,0,0,0,0,0,1)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 30:
                 LNoteA(0,0,0,0,0,1,0,0)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 32:
                 LNoteA(0,0,0,1,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 34:
                 LNoteA(0,1,0,0,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW >= 36:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [1,0,1,0,1,0,0,0]
                 SW = 0
            if intMusicIndxCounter >= 2890:
                 intMusicIndex = 8
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,0]
                 time.sleep(1)
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [1,1,1,1,1,1,1,1]
                 time.sleep(1)
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,0]
                 ctick = 20
                 SW = 0
        #=============================================================
        #MUSIC #8 FAST
        #=============================================================
        if intMusicIndex == 8: 
            SW += 1
            if SW == 1:
                 LNoteA(1,1,0,0,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 5:
                 LNoteA(0,0,0,0,0,0,1,1)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 10:
                 LNoteA(0,0,1,1,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 15:
                 LNoteA(0,0,0,0,0,1,1,0)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 20:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 25:
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW >= 30:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [1,0,1,0,1,0,0,0]
                 SW = 0
            if intMusicIndxCounter == 3500:
                intMusicIndex = 9
                SW = 0
                
        if intMusicIndex == 9: 
            SW += 1
            if intMusicIndxCounter == 3600:
                 ctick = 20
            if SW == 1:
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 10:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [1,0,1,0,1,0,0,0]
            if SW == 20:
                 LNoteA(1,0,1,0,1,0,1,0)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 30:
                 LNoteA(1,0,0,0,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 35:
                 LNoteA(1,1,0,0,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 36:
                 LNoteA(1,1,1,0,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 36:
                 LNoteA(1,1,1,1,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 37:
                 LNoteA(1,1,1,1,1,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 38:
                 LNoteA(1,1,1,1,1,1,0,0)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 39:
                 LNoteA(1,1,1,1,1,1,1,0)
                 GPIOC = [0,0,0,0,0,0,0,0]
            if SW == 40:
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [0,0,0,0,0,0,0,0]
            if SW >= 45:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,0]
                 SW = 0
            if intMusicIndxCounter  == 5200:
               PlayMusic(1,"/home/pi/Music/littldrm.mid")
               SW = 0
               ctick = 30
               intMusicIndex = 10
        #============================================================================
        # music 10
        #============================================================================
        if intMusicIndex == 10:
            SW += 1
            if SW == 1:
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [1,1,1,1,1,1,1,1]
            if SW == 5:
                 LNoteA(1,0,1,0,1,0,1,0)
                 GPIOC = [1,0,1,0,1,0,1,0]
            if SW == 10:
                 LNoteA(0,1,0,1,0,1,0,1)
                 GPIOC = [0,1,0,1,0,1,0,1]
            if SW == 15:
                 LNoteA(1,0,0,0,0,0,0,0)
                 GPIOC = [1,0,0,0,0,0,0,0]
            if SW == 20:
                 LNoteA(0,0,0,0,0,0,0,1)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 25:
                 LNoteA(1,0,0,1,0,0,0,1)
                 GPIOC = [1,0,0,1,0,0,0,1]
            if SW == 30:
                 LNoteA(0,1,0,0,1,0,1,0)
                 GPIOC = [0,1,0,0,1,0,1,0]
            if SW == 35:
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [1,1,1,1,1,1,1,1]
            if SW == 40:
                 LNoteA(0,1,0,1,0,1,0,1)
                 GPIOC = [0,1,0,1,0,1,0,1]
            if SW == 45:
                 LNoteA(1,0,0,0,0,0,0,0)
                 GPIOC = [1,0,0,0,0,0,0,0]
            if SW == 50:
                 LNoteA(0,1,0,0,0,0,0,0)
                 GPIOC = [0,1,0,0,0,0,0,0]
            if SW == 55:
                 LNoteA(0,0,1,0,0,0,0,0)
                 GPIOC = [0,0,1,0,0,0,0,0]
            if SW == 60:
                 LNoteA(0,0,0,1,0,0,0,0)
                 GPIOC = [0,0,0,1,0,0,0,0]
            if SW == 65:
                 LNoteA(0,0,0,0,1,0,0,0)
                 GPIOC = [0,0,0,0,1,0,0,0]
            if SW == 70:
                 LNoteA(0,0,0,0,0,0,1,0)
                 GPIOC = [0,0,0,0,0,0,1,0]
            if SW == 75:
                 LNoteA(0,0,0,0,0,0,0,1)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 80:
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [1,1,1,1,1,1,1,1]
            if SW == 85:
                 LNoteA(0,0,0,0,0,0,0,1)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 90:
                 LNoteA(0,0,0,0,0,0,1,0)
                 GPIOC = [0,0,0,0,0,0,1,0]
            if SW == 95:
                 LNoteA(0,0,0,0,0,1,0,0)
                 GPIOC = [0,0,0,0,0,1,0,0]
            if SW == 100:
                 LNoteA(0,0,0,0,1,0,0,0)
                 GPIOC = [0,0,0,0,1,0,0,0]
            if SW == 105:
                 LNoteA(0,0,0,1,0,0,0,0)
                 GPIOC = [0,0,0,1,0,0,0,0]
            if SW == 110:
                 LNoteA(0,0,1,0,0,0,0,0)
                 GPIOC = [0,0,1,0,0,0,0,0]
            if SW == 115:
                 LNoteA(0,1,0,0,0,0,0,0)
                 GPIOC = [0,1,0,0,0,0,0,0]
            if SW == 120:
                 LNoteA(1,0,0,0,0,0,0,0)
                 GPIOC = [1,0,0,0,0,0,0,0]
            if SW == 125:
                 LNoteA(0,1,0,1,0,1,0,1)
                 GPIOC = [0,1,0,1,0,1,0,1]
            if SW == 130:
                 LNoteA(1,0,1,0,1,0,1,0)
                 GPIOC = [1,0,1,0,1,0,1,0]
            if SW == 135:
                 LNoteA(1,1,0,0,0,0,0,0)
                 GPIOC = [1,1,0,0,0,0,0,0]
            if SW == 140:
                 LNoteA(0,0,0,0,0,0,1,1)
                 GPIOC = [0,0,0,0,0,0,1,1]
            if SW == 145:
                 LNoteA(1,1,1,0,0,0,0,0)
                 GPIOC = [1,1,1,0,0,0,0,0]
            if SW == 150:
                 LNoteA(0,0,0,0,1,1,1,1)
                 GPIOC = [0,0,0,0,1,1,1,1]
            if SW == 155:
                 LNoteA(1,1,1,1,0,0,0,0)
                 GPIOC = [1,1,1,1,0,0,0,0]
            if SW == 160:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,0]
            if SW == 165:
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [1,1,1,1,1,1,1,1]
                 SW = 0
            if intMusicIndxCounter == 10000:
                PlayMusic(1,"/home/pi/Music/RockinAroundTheChristmasTree.mid")
                SW = 0
                ctick = 30
                intMusicIndex = 11
        
        #============================================================================
        # music 11
        #============================================================================
        if intMusicIndex == 11:
            SW += 1
            if SW == 1:
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [1,1,1,1,1,1,1,1]
            if SW == 5:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [1,0,1,0,1,0,1,0]
            if SW == 10:
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [0,1,0,1,0,1,0,1]
            if SW == 15:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [1,0,0,0,0,0,0,0]
            if SW == 20:
                 LNoteA(1,1,0,0,0,0,0,1)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 25:
                 LNoteA(0,0,0,0,0,0,1,1)
                 GPIOC = [1,0,0,1,0,0,0,1]
            if SW == 30:
                 LNoteA(1,1,0,0,0,0,0,0)
                 GPIOC = [0,1,0,0,1,0,1,0]
            if SW == 35:
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [1,1,1,1,1,1,1,1]
            if SW == 40:
                 LNoteA(0,0,0,0,0,0,0,1)
                 GPIOC = [0,1,0,1,0,1,0,1]
            if SW == 45:
                 LNoteA(1,0,0,0,0,0,0,0)
                 GPIOC = [1,0,0,0,0,0,0,0]
            if SW == 50:
                 LNoteA(0,1,0,0,0,0,0,0)
                 GPIOC = [0,1,0,0,0,0,0,0]
            if SW == 55:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [0,0,1,0,0,0,0,0]
            if SW == 60:
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [0,0,0,1,0,0,0,0]
            if SW == 65:
                 LNoteA(0,0,0,0,0,0,0,1)
                 GPIOC = [0,0,0,0,1,0,0,0]
            if SW == 70:
                 LNoteA(0,0,0,0,0,0,1,0)
                 GPIOC = [0,0,0,0,0,0,1,0]
            if SW == 75:
                 LNoteA(0,0,0,0,0,0,0,1)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 80:
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [1,1,1,1,1,1,1,1]
            if SW == 85:
                 LNoteA(0,0,0,0,0,0,0,1)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 90:
                 LNoteA(0,0,0,0,0,0,1,0)
                 GPIOC = [0,0,0,0,0,0,1,0]
            if SW == 95:
                 LNoteA(0,0,0,0,0,1,0,0)
                 GPIOC = [0,0,0,0,0,1,0,0]
            if SW == 100:
                 LNoteA(0,0,0,0,1,0,0,0)
                 GPIOC = [0,0,0,0,1,0,0,0]
            if SW == 105:
                 LNoteA(0,0,0,1,0,0,0,0)
                 GPIOC = [0,0,0,1,0,0,0,0]
            if SW == 110:
                 LNoteA(0,0,1,0,0,0,0,0)
                 GPIOC = [0,0,1,0,0,0,0,0]
            if SW == 115:
                 LNoteA(0,1,0,0,0,0,0,0)
                 GPIOC = [0,1,0,0,0,0,0,0]
            if SW == 120:
                 LNoteA(1,0,0,0,0,0,0,0)
                 GPIOC = [1,0,0,0,0,0,0,0]
            if SW == 125:
                 LNoteA(0,1,0,1,0,1,0,1)
                 GPIOC = [0,1,0,1,0,1,0,1]
            if SW == 130:
                 LNoteA(1,0,1,0,1,0,1,0)
                 GPIOC = [1,0,1,0,1,0,1,0]
            if SW == 135:
                 LNoteA(1,1,0,0,0,0,0,0)
                 GPIOC = [1,1,0,0,0,0,0,0]
            if SW == 140:
                 LNoteA(0,0,0,0,0,0,1,1)
                 GPIOC = [0,0,0,0,0,0,1,1]
            if SW == 145:
                 LNoteA(1,1,1,0,0,0,0,0)
                 GPIOC = [1,1,1,0,0,0,0,0]
            if SW == 150:
                 LNoteA(0,0,0,0,1,1,1,1)
                 GPIOC = [0,0,0,0,1,1,1,1]
            if SW == 155:
                 LNoteA(1,1,1,1,0,0,0,0)
                 GPIOC = [1,1,1,1,0,0,0,0]
            if SW == 160:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,0]
            if SW == 165:
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [1,1,1,1,1,1,1,1]
                 SW = 0
            if intMusicIndxCounter == 15000:
                 PlayMusic(1,"/home/pi/Music/JingleBells.mid")
                 SW = 0
                 ctick = 30
                 intMusicIndex = 12


        #============================================================================
        # music 12
        #============================================================================
        if intMusicIndex == 12:
            SW += 1
            if SW == 1:
                 LNoteA(0,0,0,0,0,0,1,1)
                 GPIOC = [1,1,1,1,1,1,1,1]
            if SW == 5:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [1,0,1,0,1,0,1,0]
            if SW == 10:
                 LNoteA(1,1,0,0,0,0,0,0)
                 GPIOC = [0,1,0,1,0,1,0,1]
            if SW == 15:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [1,0,0,0,0,0,0,0]
            if SW == 20:
                 LNoteA(0,0,0,0,0,0,1,1)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 25:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [1,0,0,1,0,0,0,1]
            if SW == 30:
                 LNoteA(0,0,0,1,1,0,0,0)
                 GPIOC = [0,1,0,0,1,0,1,0]
            if SW == 35:
                 LNoteA(0,0,0,0,0,0,1,1)
                 GPIOC = [1,1,1,1,1,1,1,1]
            if SW == 40:
                 LNoteA(1,1,0,0,0,0,0,1)
                 GPIOC = [0,1,0,1,0,1,0,1]
            if SW == 45:
                 LNoteA(0,0,1,1,0,0,0,0)
                 GPIOC = [1,0,0,0,0,0,0,0]
            if SW == 50:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [0,1,0,0,0,0,0,0]
            if SW == 55:
                 LNoteA(0,0,0,1,0,0,0,0)
                 GPIOC = [0,0,1,0,0,0,0,0]
            if SW == 60:
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [0,0,0,1,0,0,0,0]
            if SW == 65:
                 LNoteA(0,0,0,0,0,0,0,1)
                 GPIOC = [0,0,0,0,1,0,0,0]
            if SW == 70:
                 LNoteA(0,0,0,0,0,1,1,0)
                 GPIOC = [0,0,0,0,0,0,1,0]
            if SW == 75:
                 LNoteA(0,1,1,1,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 80:
                 LNoteA(0,0,0,0,1,1,1,1)
                 GPIOC = [1,1,1,1,1,1,1,1]
            if SW == 85:
                 LNoteA(0,1,0,1,0,1,0,1)
                 GPIOC = [0,0,0,0,0,0,0,1]
            if SW == 90:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,1,0]
            if SW == 95:
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [0,0,0,0,0,1,0,0]
            if SW == 100:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [0,0,0,0,1,0,0,0]
            if SW == 105:
                 LNoteA(0,0,0,1,1,1,0,0)
                 GPIOC = [0,0,0,1,0,0,0,0]
            if SW == 110:
                 LNoteA(1,1,1,0,0,0,0,0)
                 GPIOC = [0,0,1,0,0,0,0,0]
            if SW == 115:
                 LNoteA(0,0,0,0,1,1,1,0)
                 GPIOC = [0,1,0,0,0,0,0,0]
            if SW == 120:
                 LNoteA(1,0,0,0,0,0,0,1)
                 GPIOC = [1,0,0,0,0,0,0,0]
            if SW == 125:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [0,1,0,1,0,1,0,1]
            if SW == 130:
                 LNoteA(1,1,1,1,1,1,1,1)
                 GPIOC = [1,0,1,0,1,0,1,0]
            if SW == 135:
                 LNoteA(0,0,0,0,0,0,0,0)
                 GPIOC = [1,1,0,0,0,0,0,0]
            if SW == 140:
                 LNoteA(0,0,0,0,0,1,1,1)
                 GPIOC = [0,0,0,0,0,0,1,1]
            if SW == 145:
                 LNoteA(1,0,0,0,0,0,0,0)
                 GPIOC = [1,1,1,0,0,0,0,0]
            if SW == 150:
                 LNoteA(0,1,0,0,0,0,0,0)
                 GPIOC = [0,0,0,0,1,1,1,1]
            if SW == 155:
                 LNoteA(0,0,1,0,0,0,0,0)
                 GPIOC = [1,1,1,1,0,0,0,0]
            if SW == 160:
                 LNoteA(0,0,0,1,0,0,0,0)
                 GPIOC = [0,0,0,0,0,0,0,0]
            if SW == 165:
                 LNoteA(0,0,0,0,1,0,0,0)
                 GPIOC = [1,1,1,1,1,1,1,1]
            if SW == 170:
                 LNoteA(0,0,0,0,0,1,0,0)
                 GPIOC = [1,1,1,1,1,1,1,1]
            if SW == 175:
                 LNoteA(0,0,0,0,0,0,1,0)
                 GPIOC = [1,1,1,1,1,1,1,1]
            if SW == 180:
                 LNoteA(0,0,0,0,0,0,0,1)
                 GPIOC = [1,1,1,1,1,1,1,1]
                 SW = 0
            if intMusicIndxCounter == 19000:
                 intMusicIndex == 13
                 SW = 0
                
        #============================================================================
        # no music
        #============================================================================
        if intMusicIndex == 13:
            SW += 1
            if SW == 1:
                LNoteA(1,1,1,1,1,1,1,0)
                GPIOC = [1,1,1,1,1,1,1,0]
            if SW == 10:
                LNoteA(1,1,1,1,1,1,0,0)
                GPIOC = [1,1,1,1,1,1,0,0]
            if SW == 20:
                LNoteA(1,1,1,1,1,0,0,0)
                GPIOC = [1,1,1,1,1,0,0,0]
            if SW == 30:
                LNoteA(1,1,1,0,0,0,0,0)
                GPIOC = [1,1,1,0,0,0,0,0]
            if SW == 30:
                LNoteA(1,1,0,0,0,0,0,0)
                GPIOC = [1,1,0,0,0,0,0,0]
            if SW == 40:
                LNoteA(1,0,0,0,0,0,0,0)
                GPIOC = [1,0,0,0,0,0,0,0]
            if SW == 50:
                LNoteA(0,0,0,0,0,0,0,0)
                GPIOC = [0,0,0,0,0,0,0,0]
            if SW == 60:
                LNoteA(1,1,1,1,1,1,1,1)
                GPIOC = [1,1,1,1,1,1,1,1]
            if SW == 70:
                LNoteA(0,0,0,0,0,0,0,0)
                GPIOC = [0,0,0,0,0,0,0,0]
                SW = 0
               
        #=============================================================        
        #Music End
        #=============================================================
        if intMusicIndxCounter == 19000:
            now = datetime.datetime.now()
            if now.hour == StopTime:
                SW = 0
                intMusicIndex = 14
                intMusicIndxCounter == 19000
            else:
                intMusicIndxCounter = 0
                SW = 0
                openPygame(1,"/home/pi/Music/12daysxmas.mid",intSystemOffCounter,StopTime,StartTime)

        
        print ('start GPIO CODE HERE ' + str(SW) + ' ' + str(intMusicIndxCounter)  + ' ' + str(intMusicIndex))
        print str(intSystemOffCounter)
        print ('Start Time: ' + str(StartTime))
        print ('Stop Time: ' + str(StopTime))

        #=============================================================
        if intMusicIndex == 14:
            now = datetime.datetime.now()
            SW += 1
            if now.hour == StopTime:
                setOffGPIO()
                SW = 901
                intMusicIndex = 14
            if SW == 1:
                LNoteA(1,1,1,1,1,1,1,1)
                GPIOC = [1,1,1,1,1,1,1,1]
            if SW == 100:
                LNoteA(0,0,0,0,0,0,0,0)
                GPIOC = [0,0,0,0,0,0,0,0]
            if SW == 200:
                LNoteA(1,0,0,0,0,0,0,0)
                GPIOC = [0,0,0,0,0,0,0,0]
            if SW == 300:
                LNoteA(0,1,0,0,0,0,0,0)
                GPIOC = [0,0,0,0,0,0,0,0]
            if SW == 400:
                LNoteA(0,0,1,0,0,0,0,0)
                GPIOC = [0,0,0,0,0,0,0,0]
            if SW == 500:
                LNoteA(0,0,0,1,0,0,0,0)
                GPIOC = [0,0,0,0,0,0,0,0]
            if SW == 600:
                LNoteA(0,0,0,0,1,0,0,0)
                GPIOC = [0,0,0,0,0,0,0,0]
            if SW == 700:
                LNoteA(0,0,0,0,0,1,0,0)
                GPIOC = [0,0,0,0,0,0,0,0]
            if SW == 800:
                LNoteA(0,0,0,0,0,0,1,0)
                GPIOC = [0,0,0,0,0,0,0,0]
            if SW == 900:
                LNoteA(1,0,1,0,1,0,1,0)
                GPIOC = [0,0,0,0,0,0,0,0]

            if now.hour == StartTime:
                intMusicIndxCounter = 0
                SW = 0
                openPygame(1,"/home/pi/Music/12daysxmas.mid",intSystemOffCounter,StopTime,StartTime)
            else:
                LNoteA(0,0,0,0,0,0,0,0)
                GPIOC = [0,0,0,0,0,0,0,0]
                intMusicIndex == 14
                intMusicIndxCounter = 0
                SW = 0
                print ('Start Time: ' + str(StartTime))
                time.sleep(3600)
            
        #button("Play",200,350,50,20,GREEN,BRIGHT_GREEN)
        # go ahead and update teh screen with what we've drawn
        #CONVERT NUMBERS
        if GPIOC[0] == 1:
            GPIOC[0] = RED
        else:
            GPIOC[0] = WHITE
        if GPIOC[1] == 1:
            GPIOC[1] = RED
        else:
            GPIOC[1] = WHITE
        if GPIOC[2] == 1:
            GPIOC[2] = RED
        else:
            GPIOC[2] = WHITE
        if GPIOC[3] == 1:
            GPIOC[3] = RED
        else:
            GPIOC[3] = WHITE
        if GPIOC[4] == 1:
            GPIOC[4] = RED
        else:
            GPIOC[4] = WHITE
        if GPIOC[5] == 1:
            GPIOC[5] = RED
        else:
            GPIOC[5] = WHITE
        if GPIOC[6] == 1:
            GPIOC[6] = RED
        else:
            GPIOC[6] = WHITE
        if GPIOC[7] == 1:
            GPIOC[7] = RED
        else:
            GPIOC[7] = WHITE
              
        #pygame.draw.circle(screen, GPIOC[0], [60, 40], 10)
        #pygame.draw.circle(screen, GPIOC[1], [60, 80], 10)
        #pygame.draw.circle(screen, GPIOC[2], [60, 120], 10)
        #pygame.draw.circle(screen, GPIOC[3], [60, 160], 10)
        #pygame.draw.circle(screen, GPIOC[4], [60, 200], 10)
        #pygame.draw.circle(screen, GPIOC[5], [60, 240], 10)
        #pygame.draw.circle(screen, GPIOC[6], [60, 280], 10)
        #pygame.draw.circle(screen, GPIOC[7], [60, 320], 10)
        #pygame.display.flip()
        
        #Clock limit to 60 frames per second
        clock.tick(ctick)


#buton play click
def buttonPlayClick():
    start = False
    endtime = int(E1.get())
    starttime = int(E2.get())
    if endtime != 0:
        while not start:
            now = datetime.datetime.now()
            print now.hour
            if now.hour == starttime:
                start = True
                openPygame(1,"/home/pi/Music/12daysxmas.mid",0,endtime,starttime)
            else:
                start = False
            time.sleep(3600)

def buttonStopClick():
    setOffGPIO();
    pygame.quit()
    #done = true
          
#======================================================
#create tkinter form here
#======================================================
mw.title("Play Stop")
mw.geometry("400x200")
L1 = Label(mw, text="Stop Time:")
L1.pack(anchor = CENTER)
E1 = Entry(mw, bd = 1)
E1.insert(END,'1')
E1.pack(anchor = CENTER)

L2 = Label(mw, text="Start Time")
L2.pack(anchor = CENTER)
E2 = Entry(mw, bd = 1)
E2.insert(END,'1')
E2.pack(anchor = CENTER)

btnStop = Button(mw,text="Stop", command=buttonStopClick, width=10)
btnStop.pack(side = BOTTOM)
btnPlay = Button(mw,text="Play", command=buttonPlayClick, width=10)
btnPlay.pack(side = BOTTOM)
mw.mainloop()

#openPygame(1,"/home/pi/Music/12daysxmas.mid",0)


            







