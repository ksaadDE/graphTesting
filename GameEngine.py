#!/usr/bin/python3
'''
    Written by Karim (ksaadDE) - 03/2021
    Studying & Research purposes, no practical or commerical use intended!
    
'''
import pygame as pg
import os, sys
from Colors import Colors

class GameEngine:
    def __init__(self, objects, windowTitle="Test Graph", windowSize=(640,480)):
        self.windowTitle = windowTitle
        self.windowSize = windowSize
        self.objects = objects
        self.zoom = 4
        self.lastZoom = 4
        self.cameraPos = [0,0]
        self.cameraPosChanged = True
    
    def setZoomForObjects(self):
        for graph in self.objects:
            graph.setZoomForNodes(self.zoom)
    
    def setZoom(self, x):
        self.zoom += x*0.01
        self.limitZoom()
        if not self.lastZoom == self.zoom:
            self.setZoomForObjects()
        self.lastZoom = self.zoom
    def getZoom(self):
        return self.zoom
        
    def limitZoom(self):
        if self.zoom < 4:
            self.zoom = 4
        if self.zoom > 15:
            self.zoom = 15
    
    def sumGraphData(self):
        allN = 0
        allE = 0
        for graph in self.objects:
            allE += graph.getEdgesCount()
            allN += graph.getNodesCount()
        return (allN, allE)
    
    def drawInfoText(self, screen):
        arg0 = int(round(self.zoom))
        gData = self.sumGraphData()
        text="Zoom: {0} | Graphs count: {1} | Nodes: {2}: Edges: {3} ".format(arg0, len(self.objects), gData[0], gData[1])
        color = Colors.WHITE
        screenSize = screen.get_rect()
        pos = pg.Vector2(screenSize.width/2-len(text)-100, 0)
        fontSize = int(round(6*self.zoom+0.5))
        #print(fontSize)
        font = pg.font.SysFont(None, fontSize)
        img = font.render(text, True, color)
        screen.blit(img, pos)
        
    def clearScreen(self, screen):
        screen.fill((0,0,0))
    
    def run(self):
        # see if we can load more than standard BMP
        if not pg.image.get_extended():
            raise SystemExit("Sorry, extended image module required")

        pg.init()
        main_dir = os.path.split(os.path.abspath(__file__))[0]

        pg.display.set_caption(self.windowTitle)
        all = pg.sprite.RenderUpdates()

        SCREENRECT = pg.Rect(0, 0, self.windowSize[0], self.windowSize[1])
        fullscreen = False
        
        # Set the display mode
        winstyle = pg.RESIZABLE  # |FULLSCREEN
        bestdepth = pg.display.mode_ok(SCREENRECT.size, winstyle, 32)
        screen = pg.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
        
        while True:
            background = pg.Surface(SCREENRECT.size)
            
            keysPressed = pg.key.get_pressed()
            if keysPressed[pg.K_c] and keysPressed[pg.K_LCTRL]:
                pg.quit()
                sys.exit()
            
            if self.cameraPosChanged:
                self.cameraPos = [0,0]
                self.cameraPosChanged = False
            
            if keysPressed[pg.K_w]:
                self.cameraPos[1] += 0.5
                self.cameraPosChanged=True
            if keysPressed[pg.K_s]:
                self.cameraPos[1] -= 0.5
                self.cameraPosChanged=True
            if keysPressed[pg.K_a]:
                self.cameraPos[0] += 0.5
                self.cameraPosChanged=True
            if keysPressed[pg.K_d]:
                self.cameraPos[0] -= 0.5
                self.cameraPosChanged = True
            
            if self.cameraPosChanged:
                self.clearScreen(screen)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEWHEEL:
                    self.setZoom(event.y)
                    self.clearScreen(screen)
                
            for obj in self.objects:
                    try:
                        obj.draw(screen, self.cameraPos)
                    except Exception as e:
                        print(e)
                        pass
                        
            self.drawInfoText(screen)
            #pg.display.flip()

            # clear/erase the last drawn sprites
            all.clear(screen, background)

            # update all the sprites
            all.update()

        pg.time.wait(1000)
        pg.quit()
