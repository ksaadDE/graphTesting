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
    Node(200,200, "test"),
    Node(200,250, "test2"),
    Node(100,350, "test4"),
]

# Connecting the Nodes
nodes[0].connect(nodes[0])
nodes[0].connect(nodes[0])
nodes[0].connect(nodes[0])
nodes[0].connect(nodes[1])

# Generate a Graph "testG" and add it to the Graphs

testG = Graph("testgraph", nodes)
graphs.append(testG)

GameEngine = GameEngine(graphs, "Graph Testing", (800,600)).run()
