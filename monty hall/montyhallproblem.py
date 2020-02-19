# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:17:23 2020

@author: cherryb
"""

import random

# Set number of boxes
nBox = 50
# Set number of simulations
n = 1000

scoreLoyal = 0
scoreSwap = 0

# Simulate n times
for i in range(n):
    
    listBox = []
    listBox = list(range(1, nBox+1))
    
    # Randomly choose box number with the ferarri key inside
    ferrariBox = random.choice(listBox)
    # Randomly choose box number
    chosenBox = random.choice(listBox)
    
    # Case A: if your chosen box has the ferrari key inside
    if chosenBox == ferrariBox:
        listBox.remove(chosenBox)
        # Randomly pick box that has not the ferrari key inside
        remainingBox = random.choice(listBox)
    else:
        # Case B: if your chosen box does not have the ferrari key inside
        remainingBox = ferrariBox


    # You decided NOT to swap your original box for the remaining box
    if chosenBox == ferrariBox:
        scoreLoyal += 1

    # You decided to swap your original box for the remaining box
    chosenBox = remainingBox
    if chosenBox == ferrariBox:
        scoreSwap += 1

# Probability of winning, if you did not swap
probLoyal = (scoreLoyal/n)*100
print('Probability of winning (did not swap) ', '%.2f' % probLoyal, '%')

# Probability of winning, if you swap
probSwap = (scoreSwap/n)*100
print('Probability of winning (swap) ', '%.2f' % probSwap, '%')