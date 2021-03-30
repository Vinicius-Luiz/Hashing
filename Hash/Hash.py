class Hash_Aberto():
    def __init__(self, tam):
        self.lista = []
        for x in range(tam):
            self.lista.append(None)

    def hash_funcao(self, x, i):
        return (3*x+i)%tam

    def hash_inserir(self, valor, i = 0):
        tabela = self.lista       
        while i <= tam:
            j = self.hash_funcao(valor, i)
            if tabela[j] is None:
                tabela[j] = valor
                return j
            i += 1
        print('ERRO: Estouro da tabela')

    def hash_buscar(self, valor, i=0):
        tabela = self.lista
        while i <= tam:
            j = self.hash_funcao(valor, i)
            if tabela[j] == valor:
                return j
            elif tabela[j] == None:
                return None
            i += 1
        return None

    def hash_remover(self, valor):
        j = self.hash_buscar(valor)
        if j == None:
            return None
        else:
            tabela[j] = False
            return j

    def imprimir(self):
        print(self.lista)


class Elemento():
    def __init__(self, valor, anterior = None, proximo = None):
        self.valor    = valor
        self.anterior = anterior
        self.proximo  = proximo

class Hash_Fechado():
    def __init__(self, tam):
        self.lista = []
        for x in range(tam):
            self.lista.append(None)

    def hash_funcao(self, x, i):
        return (3*x+i)%tam

    def hash_inserir(self, valor, i = 0):
        novoEle = Elemento(valor)
        tabela = self.lista
        j = self.hash_funcao(valor, i)
        if tabela[j] == None:
            tabela[j] = novoEle
            return j
        else:
            self.aux_ponteiro(tabela[j], novoEle)
            return j

    def aux_ponteiro(self, elemento, novoEle):
        if elemento.proximo == None:
            elemento.proximo = novoEle
            novoEle.anterior = elemento
            return
        else:
            return self.aux_ponteiro(elemento.proximo, novoEle)

    def hash_buscar(self, valor, i = 0):
        tabela = self.lista
        j = self.hash_funcao(valor, i)
        elemento = tabela[j]
        r = self._hash_buscar(valor, elemento, j)
        return r

    def _hash_buscar(self, valor, elemento, j):
        if elemento == None:
            return None
        
        elif elemento.valor == valor:
            return j
        
        else:
            return self._hash_buscar(valor, elemento.proximo, j)

    def hash_remover(self, valor):
        j = self.hash_buscar(valor)
        if j == None:
            return None
        else:
            tabela = self.lista
            elemento = tabela[j]
            achou = False
            while not achou:
                if elemento.valor == valor:
                    if elemento.anterior == None and elemento.proximo == None:
                        tabela[j] = None
                    elif elemento.proximo != None:
                        elemento.proximo.anterior = elemento.anterior
                        if elemento.anterior == None:
                            tabela[j] = elemento.proximo
                    return f'deletado do índice: {j}'

                else:
                    if elemento.proximo != None:
                        elemento = elemento.proximo
                    else:
                        return None
            
        
                
tam = int(input('tamanho da tabela de espalhamento de comprimento: '))
h = Hash_Fechado(tam)
