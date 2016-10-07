# -*- coding: cp1251 -*-
'''
Попытка написать компилятор по Вирту.
'''

#CONST
idLen=32 # длина идентификатора. Константа.
ident=0
leteral=2
lparen=3
lbrak=4
lbrace=5
bar=6
eql=7
rparen=8
rbrak=9
rbrace=10
period=11
other=12

#TYPE ARRAY OF CHAR
idetifier=''

#VAR
ch=''#CHAR
sym=0#INTEGER
id={} #identifier
for i in xrange(0, 32):
    id[i]=''


txt='''
   
MODULE hello;

PROCEDURE Test;
BEGIN
END Test;

END hello.
'''

def inc(i):
    i += i
    return i

class clsReader(object):
    '''
    Эмуляция класса текста.
    '''
    def __init__(self, txt=''):
        self.txt=txt
        self.pos=0
        self.eot=False
    
    def get_ch(self):
        if self.pos<len(self.txt):
            ch=self.txt[self.pos]
            self.pos += 1
            self.eot=False
        else:
            ch=''
            self.eot=True
        return ch

R=clsReader(txt)#Text.Reader(R,ch) R - global reader

class clsTexts(object):
    def __init__(self, R):
        self.R=R
    def Read(self, R):
        return R.get_ch()

Texts=clsTexts(R)

def GetSym():
    ch='\0'
    while (not R.eot) and (ch<'!'):
        ch=Texts.Read(R)
        print 'scip space: ch="'+ch+'"'
    #CASE OF
    if ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
        print 'find ch! ch=', ch
        sym=ident
        i=0
        #REPEAT
        id[i]=ch.upper(); i=inc(i)
        ch=Texts.Read(R)
        while ch.upper()>='A' or ch.upper()<='Z':
            id[i]=ch; i=inc(i)
            ch=Texts.Read(R)
            print 'i=', i, 'ch="'+ch+'"'
        print 'id=', str(id)
    elif ch==0x22:
        pass
        
if __name__=='__main__':
    for i in range (0, len(txt)-1):
       ch0=Texts.Read(R)
       print ch0,
    print '\n=========================\n'
    GetSym()
