#!/usr/bin/python3
# -*-coding:Utf-8 -*

from src.Pattern import *

#54,3

class Node():

    def __init__(self, x, y, boardSize, board, opponent):
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
            self.isLong2: 5,
            self.isBlock2: 4,
            self.isStraight2: 2,
            self.isDead2: -5,
            self.isStraight: -2,
            self.isDead: -5,
        }
        self.opponent = opponent
        self.x = x
        self.y = y
        self.boardSize = boardSize
        self.board = board[:]
        self.board[y * boardSize + x] = -1 if opponent else 1
        self.tmpBoard = [0] * boardSize * boardSize
        self.child = self.findChild()
        self.value = 0
        # print("({},{})".format(x, y))
        # self.debug(self.tmpBoard)
        # print("Child: {}".format(self.child))

    def setValue(self, value):
        self.value = value

    def getChild(self):
        return self.child

    def getChildValue(self):
        if (len(self.child) > 0):
            return self.child[0][0]
        else:
            return -5

    def getValue(self):
        return self.value

    def getBoard(self):
        return self.board

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def findChild(self):
        bigger = 0
        child = []
        for y in range(0, self.boardSize):
            for x in range(0, self.boardSize):
                self.tmpBoard[y * self.boardSize + x] = self.heuristic(x, y)
                if (bigger < self.tmpBoard[y * self.boardSize + x]):
                    bigger = self.tmpBoard[y * self.boardSize + x]
                    child = []
                    child.append([bigger, x, y])
                elif (bigger == self.tmpBoard[y * self.boardSize + x]):
                    child.append([bigger, x, y])
        # print("Number of child: {}\nchild detail: {}".format(len(child), child))
        # self.debug(self.board)
        return child

    def getBestChild(self):
        if (self.child != []):
            return self.child[0][0]
        else:
            return -5
    
    def heuristic(self, x, y):
        if (self.board[y * self.boardSize + x] == 0):
            val = 0;
            pAttack = Pattern(x, y, self.board, self.boardSize, 1 if self.opponent else -1)
            pDefense = Pattern(x, y, self.board, self.boardSize, -1 if self.opponent else 1)
            for f in self.fig:
                if (f(pAttack)):
                    val += self.fig[f]
                if (f(pDefense)):
                    val += self.fig[f]
            return val
        else:
            return (self.board[y * self.boardSize + x])

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
