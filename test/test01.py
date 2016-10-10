#-*- coding:utf8 -*-

import sys
if True:
    # всё выражение
    look='95+'
    # отдельный символ
    lookahead=''

def getchar():
    global lookahead, look
    print 'look= "' + look + '"',
    lookahead = look[0]
    look=look[1:]
    print '    lookahead="'+lookahead+'" len=', len(lookahead)

def putchar(char):
    print char

def error():
    print 'Syntax error'
    sys.exit()

def math(term):
    print '"'+term+'"'
    if lookahead == term:
        lokahead = getchar()
    else:
        error()

def term():
    global lookahead
    if lookahead.isdigit():
        print 'True'
        math(lookahead)
    else:
        error()

def expr():
    term()
    while True:
        if  lookahead=='+':
            math('+')
            term()
            putchar('+')
        elif lookahead == '-':
            math('-')
            term()
            puthcar('-')
        else:
            print 'ERROR: Unknown char="'+\
                lookahead+'" ord=' + str(ord(lookahead))
            break

def main():
    lookahead=getchar()
    expr()

main()
