class Autenticacao:
    def __init__(self, id: int, credenciais, nivel):
        self.id = id
        self.credenciais = credenciais
        self.nivel = nivel
        
    def __str__(self):
        return self.credenciais, self.nivel
    def __repr__(self):
        return f'ID: {self.id}, Credenciais: {self.credenciais}, Nivel: {self.nivel}'

class Tabela:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho
    
    def hash(self, value):
        return value % self.tamanho
    
    def push(self, valor: Autenticacao):
        chave = self.hash(valor.id)
        if self.tabela[chave] is None:
            self.tabela[chave] = [valor]
        else:
            self.tabela[chave].append(valor)
            
    def search(self, id: int):
        chave = self.hash(id)
        return self.tabela[chave]
    
    def remove(self, valor: Autenticacao):
        chave = self.hash(valor.id)
        self.tabela.pop(chave)

if __name__ == '__main__':
    tabela = Tabela(10)
    autenticacao1 = Autenticacao(1, 'Gerente', 'Master')
    autenticacao2 = Autenticacao(2, 'embalador', 'junior')
    autenticacao3 = Autenticacao(3, 'Caixa', 'Fixo')
    tabela.push(autenticacao1)
    tabela.push(autenticacao2)
    tabela.push(autenticacao3)
    print(tabela.search(3))