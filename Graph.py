#!/usr/bin/python3
'''
    Written by Karim (ksaadDE) - 03/2021
    Studying & Research purposes, no practical or commerical use intended!
    
'''
import pygame as pg
from Colors import Colors

class Graph:
    # nodes = []
    def __init__(self, name, nodes=[]):
        self.name = name
        self.nodes = nodes
        self.edges = []
        self.edges = self.calcEdges()
        self.grade = self.calcGrade()
        self.nodesCount = len(self.nodes)
    
    def draw(self, screen, cameraPos=[0,0]):
        i=0
        for node in self.nodes:
            node.draw(screen, cameraPos)
            i+=1
        if i != self.nodesCount:
            self.nodesCount = i
        pg.display.flip()
        
    def setZoomForNodes(self,zoom=1):
        for i in range(0, len(self.nodes)):
            self.nodes[i].setZoom(zoom)
    def resetZoomForNodes(self,zoom=1):
        self.setZoomForNodes(zoom)
    
    def calcEdges(self):
        self.edges = [node.getEdges() for node in self.nodes][0] # [ [tuple1, tuple2... tuplen] ]
        self.edgesCount = len(self.edges)
    
    def getEdges(self):
        return self.edges
    
    def getEdgesCount(self):
        return self.edgesCount
    
    def calcGrade(self):
        e = 0
        for node in self.nodes:
            e+=node.grade
        return e
    
    def getGrade(self):
        return self.grade

    def getNodesCount(self):
        return self.nodesCount
        
    def getNodes(self):
        return self.nodes
