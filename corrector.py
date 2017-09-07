import re

def reader():
    file=open('Words.csv', 'r', encoding='UTF-8')
    arr=[line.strip('\n') for line in file]
    return arr

def search_space_dash():
    arr=reader()
    for el in arr:
        reg=re.search('[0-9XVI].{1,5} – [0-9XVI].{1,5}', el)
        if reg!=None:
            found=reg.group()
            print(found, '-----', el)

def search_space_tilde():
    arr=reader()
    for el in arr:
        reg = re.search('[0-9XVI].{1,5} (в\.|г\.)~[0-9XVI].{1,5} (в\.|г\.)',el)
        if reg!=None:
            found=reg.group()
            print(found, '-----', el)

def search_sources():
    arr = reader()
    source_list=[]
    d={}
    table = open('table.cvs', 'w', encoding='utf-8')
    for el in arr:
        reg = re.findall(' ([А-ЯЁ][а-яёА-ЯЁ\.].{0,20}), [0-9XVI]', el)
        for i in reg:
            source_list.append(el[:4]+'-----'+i)
        for i in reg:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
    for key in d:
        text = table.write(key + '\t' + '----- ' + str(d[key]) +'\n')
    print ('Done')

def search_round_parenthesis():
    table = open('list.txt', 'w', encoding='utf-8')
    arr = reader()
    source_list = []
    for el in arr:
        reg = re.findall('\(.*?\)', el)
        for i in reg:
            text = table.write(i + '\n')
    print('Done')


search_space_dash()
#search_space_tilde()
#search_sources()
#search_round_parenthesis()