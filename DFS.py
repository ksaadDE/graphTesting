#!/usr/bin/python3
'''
    Written by Karim (ksaadDE) - 03/2021
    Studying & Research purposes, no practical or commerical use intended!
    
'''
import pygame as pg
import os, sys
from Colors import Colors

class DFS:
    def __init__(self, graph):
        self.graph = graph
    
    def run(self):
        for node in self.graph.nodes:
            node.getNodes()
