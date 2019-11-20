#!/usr/bin/python3
# -*-coding:Utf-8 -*

class Pattern():

    def __init__(self, x, y, board, boardSize, player):
        self.size = 0
        self.dead = False
        self.straight = False
        self.player = player
        line = self.checkLine(x, y, board, boardSize)
        row = self.checkRow(x, y, board, boardSize)
        diag = self.checkDiag(x, y, board, boardSize)
        self.setPattern(x, y, max(line, row, diag), boardSize)

    def __str__(self):
        res = "size of the pattern : {}".format(self.size)
        if (self.dead):
            res += " and it is dead"
        elif (self.straight):
            res += " and it is straight"
        return (res)

    def setPattern(self, x, y, val, boardSize):
        self.size = val[0]
        if (val[1] == 1 or self.isBoarded(x, y, boardSize)):
            self.straight = True
        elif (val[1] == 2 or (val[1] == 1 and self.isBoarded(x, y, boardSize))):
            self.dead = True

    def checkLine(self, x, y, board, boardSize):
        count = 1
        stat = 0
        i = x + 1
        while (i < boardSize and i < x + 5 and board[y * boardSize + i] == self.player):
            i += 1
            count += 1
        if (i < boardSize and board[y * boardSize + i] == -(self.player)):
            stat += 1
        i = x - 1
        while (i > 0 and i > x - 5 and board[y * boardSize + i] == self.player):
            i -= 1
            count += 1
        if (i > 0 and board[y * boardSize + i] == -(self.player)):
            stat += 1
        return count, stat
    
    def checkRow(self, x, y, board, boardSize):
        count = 1
        stat = 0
        i = y + 1
        while i < boardSize and i < y + 5 and board[i * boardSize + x] == self.player:
            i += 1
            count += 1
        if (i < boardSize and board[i * boardSize + x] == -(self.player)):
            stat += 1
        i = y - 1
        while i > 0 and i > y - 5 and board[i * boardSize + x] == self.player:
            i -= 1
            count += 1
        if (i > 0 and board[i * boardSize + x] == -(self.player)):
            stat += 1
        return count, stat

    def checkFirstDiag(self, x, y, board, boardSize):
        count = 1
        stat = 0
        i = x + 1
        j = y + 1
        while i < boardSize and i < x + 5 and j < boardSize and j < y + 5 and board[j * boardSize + i] == self.player:
            i += 1
            j += 1
            count += 1
        if (i < boardSize and j < boardSize and board[j * boardSize + i] == -(self.player)):
            stat += 1
        i = x - 1
        j = y - 1
        while i > 0 and i > x - 5 and j > 0 and j > y - 5 and board[j * boardSize + i] == self.player:
            i -= 1
            j -= 1
            count += 1
        if (i > 0 and j > 0 and board[j * boardSize + i] == -(self.player)):
            stat += 1
        return count, stat

    def checkSecDiag(self, x, y, board, boardSize):
        count = 1
        stat = 0
        i = x + 1
        j = y - 1
        while i < boardSize and i < x + 5 and j > 0 and j > y - 5 and board[j * boardSize + i] == self.player:
            i += 1
            j -= 1
            count += 1
        if (i < boardSize and j > 0 and board[j * boardSize + i] == -(self.player)):
            stat += 1
        i = x - 1
        j = y + 1
        while i > 0 and i > x - 5 and j < boardSize and j < y + 5 and board[j * boardSize + i] == self.player:
            i -= 1
            j += 1
            count += 1
        if (i > 0 and j < boardSize and board[j * boardSize + i] == -(self.player)):
            stat += 1
        return count, stat

    def checkDiag(self, x, y, board, boardSize):
        first = self.checkFirstDiag(x, y, board, boardSize)
        sec = self.checkSecDiag(x, y, board, boardSize)
        if (first[0] == sec[0]):
            return sec if first[1] < sec[1] else first
        else:
            return sec if first[0] < sec[0] else first

    def isBoarded(self, x, y, boardSize):
        if (x == 0 or x == boardSize - 1):
            return True
        elif (y == 0 or y == boardSize - 1):
            return True
        else:
            return False
