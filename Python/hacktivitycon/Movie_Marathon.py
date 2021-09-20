# -*- coding: utf-8 -*-
from urllib import request
import socket
import re
import string
from bs4 import BeautifulSoup

#regex1, coletar nome do filme '^> .+$'
#regex2,remover data ' \(\d+-\d+-\d+\)'


filmes_respondidos = 0
while 1:
    ip = 'challenge.ctf.games' 
    port = 31260

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    '''
    problema, eu recebo dois pacotes, mas acho que quando ele manda
    a flag vem mais um pacote e acabo não coletando ele.

    tentei sempre printar um a mais mas isso não esta funcionando.
    ''' 
    packet1 = (s.recv(1024).decode())
    packet2 = (s.recv(1024).decode())
    #packet3 = (s.recv(1024).decode())
    print(packet1)
    print(packet2)
    #print(packet3)


    #deixando o nome do filme pronto para virar um parametro na url
    p = re.compile(r'> .+')
    m = p.findall(packet2)
    a = re.sub(r' \(\d+-\d+-\d+\)', '',m[0])
    b = re.sub(r'^>\s', '',a)
    c = b.replace(' ','-')
    d = c.lower()
    e = d.replace("'", '')
    f = e.replace(":", '')
    g = f.replace('!', '')
    h = g.replace('&', '-')
    i = h.replace('.', '')
    j = i.replace('ó', 'o')
    k = j.replace('á', 'a')
    l = k.replace(';', '')
    m = l.replace('é', 'e')
    n = m.replace('ç', 'c')
    o = n.replace('/', '-')
    p2 = o.replace(',', '-')
    q = p2.replace('?', '')
    param = q

    funciona_desgraca = param.replace('&', '-')
    porfavor = re.sub(r'(---)','-',funciona_desgraca)
    porfavor2 = re.sub(r'(--)','-',porfavor)

    print('PARAMETRO ENVIADO: '+porfavor2)

    #url final para enviar para o letterbox e fazer o scrape
    url = ("https://letterboxd.com/film/" + porfavor2)


    #Colentado o source da pagina
    page = request.urlopen(url)
    soup = BeautifulSoup(page,)
    result = soup.find("div", {"class":"cast-list text-sluglist"})


    #filtrando os nomes do atores
    aw = str(result)
    renomes = re.compile(r'>[\w+\s+]+<')
    atores = renomes.findall(aw)
    atores_limps = []
    for i in atores:
        ri = i.replace('\n', '')
        rem = ri.replace('>', ' ')
        rem2 = rem.replace('<', ';')
        atores_limps.append(rem2)

    limpos2 = []

    for i in atores_limps:
        if len(i) >= 5:
            limpos2.append(i)
        else:
            pass
    try:
        name1 = limpos2[0]
        name2 = limpos2[1]
        name3 = limpos2[2]
        name4 = limpos2[3]
        name5 = limpos2[4]
    except:
        pass

    #nomes limpos e no formato
    finalmente = name1+name2+name3+name4+name5


    #enviando os dados
    filmes_respondidos +=1
    print('='*90)
    print('MANDANDO OS  NOMES:')
    print(finalmente)
    print('FILMES RESPONDIDOS:')
    print(filmes_respondidos)
    print('='*90)
    s.send(finalmente.encode())