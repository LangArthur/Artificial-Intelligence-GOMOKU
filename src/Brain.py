#!/usr/bin/python3
# -*-coding:Utf-8 -*

import random

from src.Pattern import *
from src.Node import *

class Brain:
    
    def __init__(self):
        self.name = "Plague"
        self.version = "1.3"
        self.author = "A. Lang"
        self.country = "France"
        self.tmpBoard = []
        self.boardSize = 0
        self.depthLimit = 4
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
        self.boardSize = size;

    def action(self, board):
        if (self.boardSize != 0):
            tmpBoard = [0] *  self.boardSize * self.boardSize
            res = [int(self.boardSize / 2), int(self.boardSize / 2)]
            bigger = -5;
            self.setMoveImpact(board, tmpBoard)
            for y in range(0, self.boardSize):
                for x in range(0, self.boardSize):
                    if tmpBoard[y * self.boardSize + x] > bigger:
                        bigger = tmpBoard[y * self.boardSize + x]
                        res[0] = x
                        res[1] = y
            return (res)
        else:
            return -1

    def setMoveImpact(self, board, tmpBoard):
        for y in range(0, self.boardSize):
            for x in range(0, self.boardSize):
                tmpBoard[y * self.boardSize + x] = self.heuristic(x, y, board)
                # if (board[y * self.boardSize + x] == 0):
                #     n = Node(y, x, self.boardSize, board, False)
                #     childValue = n.getChildValue
                #     n.setValue(self.minMax(0, True, n, childValue))
                #     tmpBoard[y * self.boardSize + x] = n.getValue()
                # else:
                #     tmpBoard[y * self.boardSize + x] = board[y * self.boardSize + x]
                # print("({},{}) -> {}".format(x, y, n.getValue()))
        return 0

    def minMax(self, depth, opponent, node, prev):
        if depth == self.depthLimit:
            return prev
        for child in node.getChild():
            if (opponent):
                n = Node(child[1], child[2], self.boardSize, node.getBoard(), True)
                prev = n.getChildValue()
                n.setValue(self.minMax(depth + 1, False, n, prev))
            else:
                n = Node(child[1], child[2], self.boardSize, node.getBoard(), False)
                prev = n.getChildValue()
                n.setValue(self.minMax(depth + 1, True, n, prev))
            val = max(val, n.getValue())
        return val

    def heuristic(self, x, y, board):
        if (board[y * self.boardSize + x] == 0):
            val = 0;
            pAttack = Pattern(x, y, board, self.boardSize, 1)
            pDefense = Pattern(x, y, board, self.boardSize, -1)
            for f in self.fig:
                if (f(pAttack)):
                    val += self.fig[f]
                if (f(pDefense)):
                    val += self.fig[f] / 2
            return val
        else:
            return (board[y * self.boardSize + x])

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

    def debug(self, board):
        debug = ""
        for y in range(0, self.boardSize):
            debug += "DEBUG "
            for x in range(0, self.boardSize):
                debug += str(board[y * self.boardSize + x]) + ':'
            if (y != len(board) - 1):
                debug += '\n'
        print ("{}".format(debug), flush=True)
        print("MESSAGE Etat jeu", flush=True)

def randomBrain():
    res = [random.randint(0, self.boardSize - 1), random.randint(0, self.boardSize - 1)]
    while (board[res[0] * self.boardSize + res[1]] != 0):
        res = [random.randint(0, self.boardSize - 1), random.randint(0, self.boardSize - 1)]
    return res