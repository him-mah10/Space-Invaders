import time
import datetime
import sys
import select
import tty
import termios
import os
import random
from bNs import *
from alien import *
from missiles import *

old_time = datetime.datetime.now()
old_time = (old_time.hour * 3600 + old_time.minute * 60 +
            old_time.second) * 1000 + old_time.microsecond / 1000


def isData():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [],
            [])


old_settings = termios.tcgetattr(sys.stdin)


missile = []
count = 0
board = Board()
spaceship = SpaceShip()
aliens = []
score = 0
checkTime = 1
flag = 0

try:
    tty.setcbreak(sys.stdin.fileno())
    while True:
        cur_time = datetime.datetime.now()
        cur_time = (cur_time.hour * 3600 + cur_time.minute * 60
                    + cur_time.second) * 1000 + cur_time.microsecond \
            / 1000
        if cur_time - old_time >= 1000:
            for mm in missile:
                if mm.x == 1:
                    missile.remove(mm)
                    board.matrix[mm.x][mm.y] = ' '
                else:
                    board.matrix[mm.x][mm.y] = ' '
                    mm.x -= mm.speed
                    if (board.matrix[mm.x][mm.y] == 'O'
                        or board.matrix[mm.x][mm.y] == '0') \
                        and mm.speed == 1:
                        board.matrix[mm.x][mm.y] = ' '
                        for al in aliens:
                            if al.x == mm.x and al.y == mm.y:
                                aliens.remove(al)
                                break
                        missile.remove(mm)
                        score += 1
                    elif board.matrix[mm.x][mm.y] == 'O' \
                        or board.matrix[mm.x + 1][mm.y] == 'O' \
                        or board.matrix[mm.x][mm.y] == '0' \
                        or board.matrix[mm.x + 1][mm.y] == '0':
                        for al in aliens:
                            if (al.x == mm.x or al.x == mm.x + 1) \
                                and (al.y == mm.y or al.y == mm.y + 1):
                                board.matrix[mm.x][mm.y] = ' '
                                board.matrix[al.x][al.y] = '0'
                                al.endTime[0] += 5
                                flag = 1
                                break
                        if flag == 1:
                            flag = 0
                            missile.remove(mm)
                        else:
                            board.matrix[mm.x][mm.y] = mm.character
                    else:
                        board.matrix[mm.x][mm.y] = mm.character
            old_time = cur_time
            os.system('clear')
            board.Print()
            print 'Score: ', score
            for al in aliens:
                if al.endTime[0] == count:
                    board.matrix[al.x][al.y] = ' '
                    os.system('clear')
                    board.Print()
                    print 'Score: ', score
                    aliens.remove(al)
            if count % 10 == 0:
                ali = Alien(board, count)
                board.matrix[ali.x][ali.y] = 'O'
                aliens.append(ali)
                os.system('clear')
                board.Print()
                print 'Score: ', score
            count += 1
        if isData():
            c = sys.stdin.read(1)
            if c == 'a':
                if spaceship.pos > 1:
                    board.matrix[8][spaceship.pos] = '_'
                    spaceship.pos -= 1
                    board.matrix[8][spaceship.pos] = '^'
                    os.system('clear')
                    board.Print()
                    print 'Score: ', score
            elif c == 'd':
                if spaceship.pos < 8:
                    board.matrix[8][spaceship.pos] = '_'
                    spaceship.pos += 1
                    board.matrix[8][spaceship.pos] = '^'
                    os.system('clear')
                    board.Print()
                    print 'Score: ', score
            elif c == 'q':
                os.system('clear')
                print 'Final Score: ', score
                print
                break
            elif c == ' ':
                im = i_Missile(spaceship)
                if board.matrix[im.x][im.y] == ' ':
                    board.matrix[im.x][im.y] = 'i'
                    missile.append(im)
                    os.system('clear')
                    board.Print()
                    print 'Score: ', score
            elif c == 's':
                lm = l_Missile(spaceship)
                if board.matrix[lm.x][lm.y] == ' ':
                    board.matrix[lm.x][lm.y] = 'l'
                    missile.append(lm)
                    os.system('clear')
                    board.Print()
                    print 'Score: ', score
finally:

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
