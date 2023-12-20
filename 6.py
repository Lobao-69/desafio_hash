class Produto:
    def __init__(self, id: int, controle):
        self.id = id
        self.controle = controle
    
    def __str__(self):
        return self.controle
    def __repr__(self):
        return f'ID: {self.id}, Controle de qualidade: {self.controle}'
    
class Tabela:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho
    
    def hash(self, value):
        return value % self.tamanho
    
    def push(self, valor: Produto):
        chave = self.hash(valor.id)
        if self.tabela[chave] is None:
            self.tabela[chave] = [valor]
        else:
            self.tabela[chave].append(valor)
            
    def search(self, id: int):
        chave = self.hash(id)
        return self.tabela[chave]
    
    def remove(self, valor: Produto):
        chave = self.hash(valor.id)
        self.tabela.pop(chave)
        
if __name__ == '__main__':
    tabela = Tabela(10)
    produto1 = Produto(1, 'Produto danificado')
    produto2 = Produto(2, 'Produto aprovado')
    produto3 = Produto(3, 'Produto aprovado')
    produto4 = Produto(4, 'Produto com falha')
    tabela.push(produto1)
    tabela.push(produto2)
    tabela.push(produto3)
    tabela.push(produto4)
    print(tabela.search(4))