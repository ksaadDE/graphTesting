#!/usr/bin/python3
'''
    Written by Karim (ksaadDE) - 03/2021
    Studying & Research purposes, no practical or commerical use intended!
    
'''
import pygame as pg
import os, sys
from Colors import Colors

# Button(pos, text, rect)
class Button:
    def __init__(self, rect, text="", bgColor=Colors.RED, fontColor=Colors.WHITE, borderWidth=3, borderColor=Colors.RED):
        self.text = text
        self.bgColor = bgColor
        self.fontColor = fontColor
        self.borderColor = borderColor
        self.borderWidth = borderWidth
        self.rect = rect
        minimalPos = self.calcMinimalPos(rect, borderWidth)
        rect = (minimalPos[0], minimalPos[1], rect[2], rect[3])
        self.rect = rect
        self.bgRect = pg.Rect((rect[0]-borderWidth, rect[1]-borderWidth, rect[2]+borderWidth+borderWidth,rect[3]+borderWidth+borderWidth))
        self.pgButton = pg.Rect(rect)
    
    def calcMinimalPos(self,rect, borderWidth):
        # prevents the "it goes out of the window"-'Bug' and it helps to determine the best position to have the border shown
        posX = rect[0]
        posY = rect[1]
        while (posX-borderWidth) <= 0:
                posX+=1
        while (posY-borderWidth) <= 0:
                posY+=1
        return (posX, posY)
    
    def setRect(self, rect):
        self.rect = rect
    def getRect(self):
        return self.rect
    
    def setBorderWidth(self, w):
        self.borderWidth = w
    def getBorderWidth(self):
        return self.borderWidth
        
    def setText(self, text=""):
        self.text = text
    def getText(self):
        return self.text
    
    def setPgButton(self, pgBtn):
        self.pgButton = pgBtn
    def getPgButton(self):
        return self.pgButton
        
    def setBgColor(self, c):
        self.bgColor = c
    def getBgColor(self):
        return self.bgColor
        
    def setFontColor(self, c):
        self.fontColor = c
    def getFontColor(self):
        return self.fontColor
    
    def setBorderColor(self, c):
        self.borderColor = c
    def getBorderColor(self):
        return self.borderColor
        
    def drawAText(self,screen, text, pos, fontSize, color):
        font = pg.font.SysFont(None, fontSize)
        img = font.render(text, True, color)
        screen.blit(img, pos)
    
    def draw(self, screen):
        textX = self.rect[0] + (self.rect[2]/4) - (len(self.text)/2)
        textY = self.rect[1] + (self.rect[3]/4) - (len(self.text)/2)
        pg.draw.rect(screen, self.borderColor, self.bgRect)
        pg.draw.rect(screen, self.bgColor, self.pgButton)
        self.drawAText(screen, self.text, (textX, textY), 30, self.fontColor)
        
    def wasPressed(self, event):
        return self.pgButton.collidepoint(event.pos)
