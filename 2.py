class Inventario:
    def __init__(self, id, estoque, localizacao, fornecedor):
        self.id = id
        self.estoque = estoque
        self.localizacao = localizacao
        self.fornecedor = fornecedor
    
    def __str__(self):
        return f'ID: {self.id} Estoque: {self.estoque} Localizacao: {self.localizacao} Fornecedor: {self.fornecedor}'

tabela_inventario = {}

#Função para Adicionar
def adicionar_inventario(id, estoque, localizacao, fornecedor):
    inventario = Inventario(id, estoque, localizacao, fornecedor)
    tabela_inventario[id] = inventario

#Função para atualizar
def atualizar_inventario(id, novo_estoque, nova_localizacao,novo_fornecedor):
    if id in tabela_inventario:
        tabela_inventario[id].estoque = novo_estoque
        tabela_inventario[id].localizacao = nova_localizacao
        tabela_inventario[id].fornecedor = novo_fornecedor
        
#Função buscar
def buscar_inventario(id):
    if id in tabela_inventario:
        return tabela_inventario[id]
    else:
        print("ID não encontrado!")

adicionar_inventario(1, 45, 'Loja 1', 'Lobo')
adicionar_inventario(2, 27, 'Loja 1', 'Lobo')
atualizar_inventario(2, 27, 'Loja 2', 'Kadson')
buscar_inventario(1)
print(buscar_inventario(1))