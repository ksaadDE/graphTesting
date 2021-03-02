#!/usr/bin/python3
'''
    Written by Karim (ksaadDE) - 03/2021
    Studying & Research purposes, no practical or commerical use intended!
    
'''

# import basic pygame modules
import pygame as pg
import os
import random

from Graph import Graph
from Node import Node
from Colors import Colors
from GameEngine import GameEngine

# Liste mit Knoten
nodes = [
    # Koordinaten (x,y); name
    Node(200,200, "test"),
    Node(200,250, "test2"),
    Node(100,350, "test4"),
]

# Verbindungen der Knoten herstellen
nodes[0].connect(nodes[0])
nodes[0].connect(nodes[0])
nodes[0].connect(nodes[0])
nodes[0].connect(nodes[1])

for x in nodes:
    print(x.name, x.grade)

# Graph generieren und Knoten übergeben
testG = Graph("testgraph", nodes)

GameEngine = GameEngine([testG], "Graph Testing", (800,600)).run()
