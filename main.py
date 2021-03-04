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

# Empty List with Graphs
graphs = [

]

# List with Nodes
nodes = [
    # Coordinates x,y and the name of this node
    Node(350,100, "root"), # 0
    
    Node(200,200, "n1"),    # 1
    Node(500,200, "n2"),    # 2
    
    Node(150,300, "n1,1"),  # 3
    Node(250,300, "n1,2"),  # 4
    
    Node(450,300, "n2,1"),  # 5
    Node(550,300, "n2,2"),  # 6
]

# Connecting the Nodes
nodes[0].connect(nodes[1])
nodes[0].connect(nodes[2])

nodes[1].connect(nodes[3])
nodes[1].connect(nodes[4])

nodes[2].connect(nodes[5])
nodes[2].connect(nodes[6])

# Generate a Graph "testG" and add it to the Graphs

testG = Graph("testgraph", nodes)
graphs.append(testG)

GameEngine = GameEngine(graphs, "Graph Testing", (800,600)).run()
