class Mercado:
    def __init__(self, id: int, dados, demanda, avaliacoes):
        self.id = id
        self.dados = dados
        self.demanda = demanda
        self.avaliacoes = avaliacoes
    
    def __str__(self):
        return self.id, self.dados, self.demanda, self.avaliacoes
    def __repr__(self):
        return f'ID: {self.id}, Dados de vendas: {self.dados}, Demanda: {self.demanda}, Avaliações dos Clientes: {self.avaliacoes}'
class Tabela:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho
    
    def hash(self, value):
        return value % self.tamanho
    
    def push(self, valor: Mercado):
        chave = self.hash(valor.id)
        if self.tabela[chave] is None:
            self.tabela[chave] = [valor]
        else:
            self.tabela[chave].append(valor)
            
    def search(self, id: int):
        chave = self.hash(id)
        return self.tabela[chave]
    
    def remove(self, valor: Mercado):
        chave = self.hash(valor.id)
        self.tabela.pop(chave)

if __name__ == '__main__':
    tabela = Tabela(10)
    mercado1 = Mercado(1, 'Vendas incompletas', 'Baixa', 'Negativas')
    mercado2 = Mercado(2, 'Vendas quase concluidas', 'Boa', 'Pode melhorar')
    mercado3 = Mercado(3, 'Vendas concluidas', 'Muito Boa', 'Otima')
    mercado4 = Mercado(4, 'Vendas superadas', 'Otimas', 'Excelente')
    tabela.push(mercado1)
    tabela.push(mercado2)
    tabela.push(mercado3)
    tabela.push(mercado4)
    print(tabela.search(4))