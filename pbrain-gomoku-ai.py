#!/usr/bin/python3
# -*-coding:Utf-8 -*

from src.GameManager import GameManager
from src.RandomBrain import RandomBrain

def main():
    brain = RandomBrain()
    m = GameManager(brain)
    m.launch()
    return 0

if __name__ == '__main__':
	main()