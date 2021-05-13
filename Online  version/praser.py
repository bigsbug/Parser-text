import re
from random import choice


def Get_Paragraphs(str_data):
    data = str(str_data).strip().split('\n\n')
    data = list(map(str.strip,data))
    return data
def Re_Space(str_data,size = 2):
    str_data = str_data.replace('\n\n\n','\n\n')
    str_data = str_data.replace(' '*size,' ')
    new_data = ''
    for text in Get_Paragraphs(str_data):
        new_data += str(text).replace('\n','') +'\n\n'
    return new_data

def Add_Dot(str_data : str):
    new_data = ''
    str_data = str_data.strip()
    for c,text in enumerate(Get_Paragraphs(str_data)): 
        try:
            if text[-1] != '.':
                new_data += text+'.\n\n'
            else:
                new_data += text + '\n\n'
        except:
            pass
    return new_data
    
def Limit_Words(str_data,limit):
    new_data = ''
    str_data = str_data.strip()
    for c,text in enumerate(Get_Paragraphs(str_data)):
        data = str(text).split(' ')[0:int(limit)]
        new_data += ' '.join(map(str,data)) +'\n\n'
    return new_data

def Clear_Symbols(str_data):
    pattern = r'\W'
    new_data = ''
    for i in str(str_data).split('\n'):
        new_data += re.sub(pattern,' ',i) 
        new_data += '\n'

    return new_data

def Clear_English(str_data):
    pattern = '[A-Za-z]'
    new_data = ''
    for i in str(str_data).split('\n'):
        new_data += re.sub(pattern,'',i) 
        new_data += '\n'
    
    return new_data

def Clear_Numbers(str_data):
    pattern = '[\u06f0-\u06f9 0-9]'# 0-9 in arabic and persian & 0-9 
    new_data = ''
    for i in str(str_data).split('\n'):
        new_data += re.sub(pattern,' ',i) 
        new_data += '\n'
    
    return new_data

def Swap_Word(str_data,pos_swap):
    new_data = ''
    for text in Get_Paragraphs(str_data):
        list_words = text.split()
        for c,i in enumerate(pos_swap):
            if i <= len(list_words) and c+1 <= len(pos_swap)-1:
                try:
                    reminder = list_words[i]
                    list_words[i] = list_words[pos_swap[c+1]]
                    list_words[pos_swap[c+1]] = reminder
                except:
                    pass
            else:
                break
            
        new_data += ' '.join(list_words)+'\n\n'
    return new_data

def Random_Title(perfix_title:list,title:str,text_data:str):
    new_data = ''
    counter = 3
    for text in Get_Paragraphs(text_data):
        if counter == 3:
            Title = str(choice(perfix_title)).strip()
            new_data += f"<h2>{Title} {title}</h2>\n{text}\n\n"
            counter = 0
        else:
            new_data += f'{text}\n\n'
        
        counter +=1
    return new_data