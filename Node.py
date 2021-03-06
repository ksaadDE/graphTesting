#!/usr/bin/python3
'''
    Written by Karim (ksaadDE) - 2021
    Studying & Research purposes, no practical or commerical use intended!
    
'''
import pygame as pg
from Colors import Colors

class Node:
    def __init__(self,x,y,name, cNodes=[]):
        self.x = x
        self.y = y
        self.name = name
        self.color = Colors.RED
        self.connectedNodesColor = Colors.GREEN
        if len(cNodes) > 0:
            self.connectedNodes = cNodes
        else:
            self.connectedNodes = []
        self.grade = self.calcGrade()
        self.dotSize = 3
        self.connectionWidth = 1
        self.zoom = 4
        self.edges = []
        self.calcEdges()
        
    def calcGrade(self):
        if len(self.connectedNodes) == 0:
            return 0
        
        i=0
        for node in self.connectedNodes:
           i += 2 if (node == self) else 1
        return i
    
    def calcEdges(self):
        p = self.getPos()
        if len(self.edges) != len(self.connectedNodes):
            self.edges = []
        
        for node in self.connectedNodes:
            tpl = (p, node.getPos())
            self.edges.append( (p, node.getPos()) )
    
    def getX(self):
        x = self.x
        if self.zoom > 1:
            x += 4*self.zoom
        
        x = int(round(x))
        return x
    def getY(self):
        y = self.y
        if self.zoom > 1:
            y -= 4*self.grade*self.zoom
        y = int(round(y))
        return y
        
    def setZoom(self, z):
        self.zoom = z
    def getZoom(self):
        return self.zoom
        
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y
    
    def setPos(self, v):
        self.x = v.x
        self.y = v.y
    def getPos(self):
        return pg.Vector2(self.getX(), self.getY())
    
    def getConnectedNodes(self):
        return self.connectedNodes
    
    def getEdges(self):
        return self.edges
        
    def connect(self, node):
        self.connectedNodes.append(node)
        self.grade = self.calcGrade()
        self.calcEdges()
    
    def disconnect(self, node):
        if node in self.connectedNodes:
            self.connectedNodes.remove(node)
        self.grade = self.calcGrade()
        self.calcEdges()
        return self.connectedNodes
    
    def drawNameText(self, screen):
        text = "N: {0}".format(self.name)
        color = Colors.WHITE
        add = 2 if self.grade == 0 else 5*self.zoom+self.grade
        pos = self.getPos()+pg.Vector2(15, 20+add)
        fontSizeC = 10*self.zoom-24
        if fontSizeC > 20 and self.zoom > 4:
            fontSizeC = 24
        fontSize = int(round(fontSizeC))
        font = pg.font.SysFont(None, fontSize)
        img = font.render(text, True, color)
        screen.blit(img, pos)
    
    # Dot == Node "point" (the red Dot mostly)
    def drawDot(self, screen):
        color = self.color
        pos = self.getPos()
        dotSize = self.dotSize
        pg.draw.circle(screen, color, pos, int(round(dotSize*self.zoom)))
    
    # Draws the connection either cirlce(s) or line
    def drawConnection(self, screen, connectedNode, i=0):
        color = self.connectedNodesColor
        pos = self.getPos()
        connectionWidth = self.connectionWidth
        if connectedNode is self:
            # HERE'S a loop! :o
            height = (50 + 5*i+2)*0.25*self.zoom
            width = (35 + 5*i+2)*0.25*self.zoom
            pg.draw.ellipse(screen, Colors.BLUE, pg.Rect((pos.x-(width/2), pos.y-height), (width,height)), 2)
            #pg.draw.circle(screen, Colors.BLUE, pos, int(round(10+(2*i+2)*self.zoom)), 1) <--- old circles, if you want
        else:
            # if connected to somewhere else :o
            pg.draw.line(screen, color, pos, connectedNode.getPos(), int(round(connectionWidth*self.zoom)))
    
    def draw(self, screen, cameraPos=[0,0]):
        self.x+=cameraPos[0]
        self.y+=cameraPos[1]
        
        self.drawDot(screen)
        self.drawNameText(screen)
        if len(self.connectedNodes) > 0:
            for i in range(0, len(self.connectedNodes)):
                self.drawConnection(screen, self.connectedNodes[i], i)
