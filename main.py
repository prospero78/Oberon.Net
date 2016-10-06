# -*- coding: utf8 -*-
'''
Это компилятор на питоне для языка oberon.
Обеспечивает разбор типовых конструкций и транслирует их в MSIL.
'''
import os, sys
import modNormalize as mNorm

verifer = 'c:\\Program Files\\Microsoft SDKs\\Windows\\v10.0A\\bin\NETFX 4.6.1 Tools\\PEVerify.exe'
compiler = 'c:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319\\ilasm.exe'

def input_name_file():
    '''
    Запрашивает имя файла для компиляции.
    '''
    print u'1. name file <Привет.ob>: ',
    name_file=raw_input()
    if name_file=='':
        name_file=u'Привет.ob'
    print 'name_file:', name_file
    f=open(name_file, 'r')
    file_txt=f.read()
    f.close()
    return name_file, file_txt

def split_txt_to_string(txt=None):
    '''
    Разделяет полученный файл на строки кода.
    '''
    if len(txt)<5:
        print 'split_txt_none(): not find text for split!\n'
        sys.exit()
    else:
        txt_lst=txt.split('\n')
        txt_dict={}
        for i in xrange(0, len(txt_lst)):
            if len(txt_lst[i])>1:
                txt_dict[i]=txt_lst[i]
        # контрольный вывод
        for i in txt_dict:
            print i, txt_dict[i].decode('utf8')
        return txt_dict

def split_string_lex(txt=None):
    '''
    Разделяет строки кода на лексемы через пробел.
    '''
    txt_lst=txt.split(' ')
    txt_dict={}
    for i in xrange(0, len(txt_lst)):
        txt_dict[i]=txt_lst[i]
        print '"'+txt_lst[i].decode('utf8')+'"   ',
    print 
    return txt_dict

def normalize_str(lex):
    '''
    Анализирует на ключевые слова.
    '''
    lex_up=lex.decode('utf8').upper()
    if mNorm.normalize(lex_up):
        lex=lex_up
    else:
        lex = lex.decode('utf8')
    print lex
    return lex
    
def normalize_file(name_file, txt_dict):
    txt_out=''
    for i in txt_dict:
        str_dict=txt_dict[i]
        # сборка строки
        for i1 in str_dict:
            if i1==0:
                txt_out += str_dict[i1]
            else:
                if str_dict[i1]<>'\n\r':
                    txt_out += ' ' +str_dict[i1]
        txt_out += '\n'
    f=open(name_file, 'w')
    f.write(txt_out.encode('utf8'))
    f.close()
    return txt_out

def control_name_module(name_file, txt_dict):
    '''
    Контролирует соответсвие имени модуля и фактическому значению.
    '''
    print 'module name: "'+name_file[:-3]+'"   ',
    name_mod=txt_dict[0][1]
    print '"'+name_mod+'"'
    if name_file[:-3]<>name_mod:
        print u'Имя файла и имя модуля не совпадают: "' + name_file[:-3] +'"    "'+ name_mod+'"'
        sys.exit()
    else:
        print u'Имя файла и имя модуля совпали'
    
    sys.exit()
    
    
def translate_mcil(name_file, txt_dict):
    # 
    name=name_file[:-3]
    name_il=name+'.il'
    txt_cil_ish='''
.assembly extern mscorlib {}
.assembly ''' + name+ '''{}
.method static public void main() cil managed 
{ .entrypoint 
  .maxstack 1 
  ldstr "Hello world!" 
  call void [mscorlib]System.Console::WriteLine(class System.String) 
  ret 
}  '''
    txt_asm=''
    txt_cil='''
.assembly extern mscorlib {}
.assembly ''' + name+ '''{}
.namespace ''' + name +'''{
.method static public void main() cil managed 
{ .entrypoint 
  ''' + txt_asm+'''
  ret 
}
}  '''
    
    f=open(name_il, 'w')
    f.write(txt_cil)
    f.close()
    os.system(compiler+ ' /debug '+name_il)
    
    
if __name__=='__main__':
    name_file, file_txt=input_name_file()
    print 'file text:\n\n', file_txt.decode('utf8'), '\n'
    
    # разделение на строки
    print u'\n\n2. разделение на строки file_txt\n\n'
    txt_dict=split_txt_to_string(file_txt)
    
    
    # разделение на лексемы
    print u'\n\n3. разделение на лексемы\n\n'
    for i in txt_dict:
        str_dict=split_string_lex(txt_dict[i])
        txt_dict[i]=str_dict
    
    print u'\n\n3. нормализация лексем \n\n'
    for i in txt_dict:
        str_dict=txt_dict[i]
        # нормализация ключевых слов
        for i1 in str_dict:
            str_dict[i1]=normalize_str(str_dict[i1])
    
    print u'\n\n4. сохранение нормализации модуля\n\n'
    txt_str=normalize_file(name_file, txt_dict)
    
    print u'\n\n5. контроль имени файли и модуля\n\n'
    control_name_module(name_file, txt_dict)
    
    translate_mcil(name_file, txt_str)
