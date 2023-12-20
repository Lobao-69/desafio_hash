class Rastreamento:
    def __init__(self, num: int, localizacao, status, detalhe):
        self.num = num
        self.localizacao = localizacao
        self.status = status
        self.detalhe = detalhe
    
    def __str__(self):
        return self.localizacao, self.status, self.detalhe
    def __repr__(self):
        return f'N° de rastreio da remessa: {self.num}, Localização atual: {self.localizacao}, Status da entrega: {self.status}, Detalhe do destinatário: {self.detalhe}'

class Tabela:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho
    
    def hash(self, value):
        return value % self.tamanho
    
    def push(self, valor: Rastreamento):
        chave = self.hash(valor.num)
        if self.tabela[chave] is None:
            self.tabela[chave] = [valor]
        else:
            self.tabela[chave].append(valor)
            
    def search(self, num: int):
        chave = self.hash(num)
        return self.tabela[chave]
    
    def remove(self, valor: Rastreamento):
        chave = self.hash(valor.num)
        self.tabela.pop(chave)

if __name__ == '__main__':
    tabela = Tabela(10)
    rastreamento1 = Rastreamento(147, 'Aguardando entrada', 'Indefinido', 'Loja 1')
    rastreamento2 = Rastreamento(258, 'Entrada concluida', 'Prazo de 10 dias', 'Loja 2')
    rastreamento3 = Rastreamento(369, 'Saiu', 'Cumprido', 'Loja 3')
    rastreamento4 = Rastreamento(151, 'Saiu para a loja', 'Concluido', 'Loja 1')
    tabela.push(rastreamento1)
    tabela.push(rastreamento2)
    tabela.push(rastreamento3)
    tabela.push(rastreamento4)
    print(tabela.search(151))