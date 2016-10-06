# -*- coding: utf8 -*-
'''
Модуль содержит правила нормализации для кода на обероне.
'''
lst_keyword=(
'MODULE', 'МОДУЛЬ',
'END', 'КОНЕЦ',
'BEGIN', 'НАЧАТЬ',
'BEG', 'нач',
'PROCEDURE','ПРОЦЕДУРА',
'PROC','ПРОЦ',
'END;', 'КОНЕЦ;',
'PRINT', 'ПЕЧАТЬ')

def normalize(lex):
    '''
    Перебирает по порядку все возможные значения в ходе нормализации.
    выясняет, считается ли слово ключевым.
    '''
    for i in lst_keyword:
        if lex==i.decode('utf8'):
            return True
    return False
