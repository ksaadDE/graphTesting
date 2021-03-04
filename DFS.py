#!/usr/bin/python3
'''
    Written by Karim (ksaadDE) - 03/2021
    Studying & Research purposes, no practical or commerical use intended!
    
'''
import pygame as pg
import os, sys, time
from Colors import Colors

class DFS:
    def __init__(self, graph):
        self.graph = graph
        self.visited = []
    
    def run(self, screen=False):
        self.visited = []
        i=0
        firstNode = self.graph.nodes[0]
        firstNode.color = Colors.BLUE
        self.visited.append(firstNode)
        for node in firstNode.getConnectedNodes():
            if i <= len(firstNode.getConnectedNodes()):
                pg.draw.line(screen, Colors.WHITE, firstNode.getPos(), node.getPos(), 4)
                pg.display.update()
            startPos = node.getPos()
            node.color = Colors.BLUE
            self.visited.append(node)
            pg.display.update()
            for child in node.getConnectedNodes():
                time.sleep(0.25)
                endPos = child.getPos()
                child.color = Colors.BLUE
                self.visited.append(child)
                pg.draw.line(screen, Colors.WHITE, startPos, endPos, 4)
                pg.display.update()
            i+=1
        time.sleep(2)
        for node in self.visited:
             node.color = Colors.RED
             pg.display.update()
        
