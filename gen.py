#! /usr/bin/env python

import svgwrite
from math import floor
from random import randint

class EqualSeparator:

    def __init__(self, n, max_num_width,offset):
        self.n = n
        self.width = max_num_width
        self.offset = offset

    def translate(self,n):
        return n * (self.width / self.n) + self.offset

dwg = svgwrite.Drawing('test.svg', profile='tiny')

# Sizes from Arena specs
ZONE_SIZE = 2850
SEP_DIST = 150
TOKEN_WIDTH = 120
GRID_NUM = 5

MARGIN = SEP_DIST * 2

# Arena outline
dwg.add(svgwrite.shapes.Rect((0,0),(ZONE_SIZE,ZONE_SIZE),fill='white'))

dwg.add(svgwrite.shapes.Rect((MARGIN,MARGIN),(ZONE_SIZE - MARGIN * 2,ZONE_SIZE - MARGIN * 2),fill='white'))

es = EqualSeparator(GRID_NUM,ZONE_SIZE - MARGIN + TOKEN_WIDTH,MARGIN)

token_set = set()

while len(token_set) < 5:
    token_set.add(randint(0,(GRID_NUM ** 2) - 1))

text = dwg.add(dwg.g(font_size=100))
text.add(dwg.text("Token Positions: " + str(token_set), (MARGIN, ZONE_SIZE - 100)))
text.add(dwg.text("Centre -->", (ZONE_SIZE - MARGIN * 2, ZONE_SIZE - 100)))

for x_num in range(0,GRID_NUM):
    for y_num in range(0,GRID_NUM):

        num = x_num + y_num * GRID_NUM

        if num in token_set:
            fillcolour = 'black'
        else:
            fillcolour = 'white'

        dwg.add(svgwrite.shapes.Rect((es.translate(x_num),es.translate(y_num)),(TOKEN_WIDTH,TOKEN_WIDTH),stroke='black',stroke_width=3,fill=fillcolour))
        text.add(dwg.text(str(num), (es.translate(x_num) + TOKEN_WIDTH + 2, es.translate(y_num))))


dwg.save()
