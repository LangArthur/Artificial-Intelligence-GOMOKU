#!/usr/bin/python3
# -*-coding:Utf-8 -*

from src.Pattern import *
from src.Node import *

class ABrain:
    
    def __init__(self):
        self.name = "bot name"
        self.version = "0.0"
        self.author = "authors name"
        self.country = "country of the bot"
        self.boardSize = 0
        self.fig = {
            self.isLong5: 10000,
            self.isLong4: 1000,
            self.isBlock4: 750,
            self.isStraight4: 500,
            self.isDead4: -5,
            self.isBlock3: 300,
            self.isLong3: 200,
            self.isStraight3: 50,
            self.isDead3: -5,
            self.isLong2: 10,
            self.isBlock2: 8,
            self.isStraight2: 4,
            self.isDead2: -5,
            self.isStraight: -2,
            self.isDead: -5,
        }

    def __str__(self):
        return ("name=\"{}\", version=\"{}\", author=\"{}\", country=\"{}\"".format(self.name, self.version, self.author, self.country))

    def initBrain(self, size):
        pass

    def action(self, board):
        pass

    def debug(self, board):
        pass

    def isLong5(self, p):
        if (p.size >= 5):
            return True
        else:
            return False

    def isBlock4(self, p):
        if (p.size == 4 and p.player == -1):
            return True
        else:
            return False

    def isStraight4(self, p):
        if (p.size == 4 and p.straight):
            return True
        else:
            return False

    def isLong4(self, p):
        if (p.size == 4 and not(p.straight) and not(p.dead)):
            return True
        else:
            return False

    def isDead4(self, p):
        if (p.size == 4 and p.dead):
            return True
        else:
            return False

    def isBlock3(self, p):
        if (p.size == 3 and p.player == -1):
            return True
        else:
            return False

    def isStraight3(self, p):
        if (p.size == 3 and p.straight):
            return True
        else:
            return False

    def isLong3(self, p):
        if (p.size == 3 and not(p.straight) and not(p.dead)):
            return True
        else:
            return False

    def isDead3(self, p):
        if (p.size == 3 and p.dead):
            return True
        else:
            return False

    def isStraight2(self, p):
        if (p.size == 2 and p.straight and p.player == 1):
            return True
        else:
            return False

    def isLong2(self, p):
        if (p.size == 2 and not(p.straight) and not(p.dead) and p.player == 1):
            return True
        else:
            return False

    def isBlock2(self, p):
        if (p.size == 2 and p.player == -1):
            return True
        else:
            return False

    def isDead2(self, p):
        if (p.size == 2 and p.dead):
            return True
        else:
            return False

    def isStraight(self, p):
        if (p.straight):
            return True
        else:
            return False

    def isDead(self, p):
        if (p.dead):
            return True
        else:
            return False
