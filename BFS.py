#!/usr/bin/python3
'''
    Written by Karim (ksaadDE) - 03/2021
    Studying & Research purposes, no practical or commerical use intended!
    
'''
import pygame as pg
import os, sys, time
from Colors import Colors

class BFS:
    def __init__(self, graph):
        self.graph = graph
        self.visited = []
    
    def run(self, screen=False):
        self.visited = []
        nodeID = 0
        connectedNodeID = 0
        for node in self.graph.getNodes():
            nodeID += 1
            if screen != False:
                for conNode in node.getConnectedNodes():
                    connectedNodeID += 1
                    time.sleep(0.25)
                    startPos = node.getPos()
                    endPos = conNode.getPos()
                    conNode.color = Colors.BLUE
                    conNode.draw(screen)
                    self.visited.append(conNode)
                    pg.draw.line(screen, Colors.WHITE, startPos, endPos, 4)
                    pg.display.update()
        time.sleep(2)
        for node in self.visited:
            node.color = Colors.RED
            node.draw(screen)
            pg.display.update()
        self.visited = []
