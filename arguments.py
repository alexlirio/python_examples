#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Use *args para aceitar uma lista de argumentos posicionais.
# Use **kwargs para aceitar um dicionario de argumentos identificados por palavras-chave
#
# Exemplo:
# def method(nome, *args, **kwargs):
def method(nome, *args, **kwargs):
    saida = ['<' + nome]
    for par in kwargs.items():
        saida.append(' %s="%s"' % par)
    if args:
        saida.append('>')
        if len(args) == 1:
            saida.append(args[0])
        else:
            saida.append('\n')
            for linha in args:
                saida.append('\t%s\n' % linha)
        saida.append('</%s>' % nome)
    else:
        saida.append(' />')
    return ''.join(saida)


if __name__ == '__main__':
    print method('br')
    print method('img',src='foto.jpg',width=3,height=4)
    print method('a','Wikipédia',
              href='http://wikipedia.org')
    print method('p','Eu não devia te dizer',
        'mas essa lua','mas esse conhaque',
        'botam a gente comovido como o diabo.',
        id='poesia')