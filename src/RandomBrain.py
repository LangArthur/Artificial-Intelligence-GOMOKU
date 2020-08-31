#!/usr/bin/python3
# -*-coding:Utf-8 -*

import random
from src.ABrain import ABrain

class RandomBrain (ABrain) :
    def __init__(self):
        self.name = "Random Brain"
        self.version = "0.1"
        self.author = "A. Lang"
        self.country = "France"

    def initBrain(self, size):
        self.boardSize = size;

    def action(self, board):
        self.debug(board);
        res = [random.randint(0, self.boardSize - 1), random.randint(0, self.boardSize - 1)]
        while (board[res[1] * self.boardSize + res[0]] != 0):
            res = [random.randint(0, self.boardSize - 1), random.randint(0, self.boardSize - 1)]
        print("DEBUG " + str(board[res[0] * self.boardSize + res[1]]), flush=True)
        return res

    def debug(self, board):
        debug = ""
        for y in range(0, self.boardSize):
            debug += "DEBUG "
            for x in range(0, self.boardSize):
                debug += str(board[y * self.boardSize + x]) + ':'
            if (y != len(board) - 1):
                debug += '\n'
        print ("{}".format(debug), flush=True)
        print("MESSAGE Game State", flush=True)