def a():
    return float(input('Coloque seu primeiro numero: ')) #pega o input do primeiro numero

def b():
    return float(input('Coloque seu segundo numero: ')) #pega o input do segundo numero

def soma():
    print('\nResultado:',a() + b())
    print("=" * 50)

def mul():
    print('\nResultado:',a() * b())
    print("=" * 50)

def sub ():
    print('\nResultado:',a() - b())
    print("=" * 50)

def div():
    try:
        print('\nResultado:',a()/b())
        print("=" * 50)
    except ZeroDivisionError:
        print("\nNao da pra dividir por 0.")
    print("=" * 50)




'''feito por Eugenio 15/05/20'''
