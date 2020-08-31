#!/usr/bin/python3
# -*-coding:Utf-8 -*

import sys

from src.ABrain import *

# GameManager class
#
# It handle all communication with the interface Piswork

class GameManager:

    def __init__(self, brain):
        self.inGame = True
        self.limit = 20
        self.boardSize = 0
        self.board = []
        self.brain = brain
        self.oppenent = -1
        self.player = 1
        self.cmd = {
            "START": self.start,
            "END": self.end,
            "BEGIN": self.begin,
            "TURN": self.turn,
            "BOARD": self.boardFct,
            "INFO": self.info,
            "ABOUT": self.about,
            "RESTART": self.restart,
        }

    def launch(self):
        try:
            while self.inGame:
                line = input()
                if (line and len(line) != 0):
                    self.interpreter(line)
        except BaseException as e:
            self.myWrite("ERROR: {}".format(e))

    def myWrite(self, text):
        print(text, flush=True)

    def interpreter(self, line):
        elems = line.split()
        if (elems[0] in self.cmd):
            self.cmd[elems[0]](elems)

    def start(self, elems):
        if (len(elems) == 2):
            size = int(elems[1])
            if (size > self.limit or size < 5):
                self.myWrite("ERROR unsupported size.")
                exit(84)
            else:
                self.boardSize = size
                self.board = [0] * size * size
                self.brain.initBrain(size)
                self.myWrite("OK")
        else:
            self.myWrite("ERROR No size given")

    def turn(self, elems):
        if (self.boardSize == 0):
            self.myWrite("ERROR board was not correctly initialisze")
        elif (len(elems) < 2):
            self.myWrite("ERROR no position is given")
        else:
            val = [int(x) for x in elems[1].split(',')]
            x = val[0]
            y = val[1]
            self.board[y * self.boardSize + x] = self.oppenent
            move = [int(x) for x in self.brain.action(self.board)]
            self.board[move[1] * self.boardSize + move[0]] = self.player
            self.myWrite("{},{}".format(move[0], move[1]))

    def boardFct(self, elems):
        line = input()
        while (line != "DONE"):
            coord = [int(x) for x in line.split(",")]
            self.board[coord[1] * self.boardSize + coord[0]] = (1 if coord[2] == 1 else -1)
            line = input()
        move = [int(x) for x in self.brain.action(self.board)]
        self.board[move[1] * self.boardSize + move[0]] = self.player
        self.myWrite("{},{}".format(move[0], move[1]))

    def info(self, elems):
        return 0

    def begin(self, elems):
        move = [int(self.boardSize / 2), int(self.boardSize / 2)]
        self.myWrite("{},{}".format(move[0], move[1]))
        self.board[move[1] * self.boardSize + move[0]] = self.player

    def restart(self, elems):
        self.board = [[0 for x in range(self.boardSize)] for y in range(self.boardSize)]
        self.start(int(elems[1]))
        self.myWrite("OK")

    def end(self, elems):
        self.inGame = False

    def about(self, elems):
        self.myWrite(self.brain)