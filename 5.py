class Producao:
    def __init__(self, num: int, status, detalhe, prazo):
        self.num = num
        self.status = status
        self.detalhe = detalhe
        self.prazo = prazo
    def __str__(self):
        return self.status, self.detalhe, self.prazo
    def __repr__(self):
        return f'N° da ordem de produção: {self.num}, Status: {self.status}, Detalhe: {self.detalhe}, Prazo: {self.prazo}'

class Tabela:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho
    
    def hash(self, value):
        return value % self.tamanho
    
    def push(self, valor: Producao):
        chave = self.hash(valor.num)
        if self.tabela[chave] is None:
            self.tabela[chave] = [valor]
        else:
            self.tabela[chave].append(valor)
            
    def search(self, id: int):
        chave = self.hash(id)
        return self.tabela[chave]
    
    def remove(self, valor: Producao):
        chave = self.hash(valor.id)
        self.tabela.pop(chave)

if __name__ == '__main__':
    tabela = Tabela(10)
    producao1 = Producao(123, 'Aguardando entrada','---', 'Indefinido')
    producao2 = Producao(456, 'Entrada efetuada','Deu entrada hoje', '15 Dias')
    producao3 = Producao(789, 'Finalizado','Produto encaminhado', 'Concluido')
    tabela.push(producao1)
    tabela.push(producao2)
    tabela.push(producao3)
    print(tabela.search(789))