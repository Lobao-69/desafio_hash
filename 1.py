class Componente:
    def __init__(self, id, status, localizacao,historico):
        self.id = id
        self.status = status
        self.localizacao = localizacao
        self.historico = historico
    
    def __str__(self):
        return f'id: {self.id}, status: {self.status}, localização: {self.localizacao}, historico: {self.historico}'

tabela_componente = {}


#função para adicionar
def adicionar_componente(id, status, localizacao, historico):
    componente = Componente(id, status, localizacao, historico)
    tabela_componente[id] = componente

#Funcao atualizar

def atualizar_componente(id, novo_status, nova_localizacao, novo_historico):
    if id in tabela_componente:
        tabela_componente[id].status = novo_status
        tabela_componente[id].localizacao = nova_localizacao
        tabela_componente[id].historico = novo_historico
    else:
        print("ID não encontrado!")

#Função buscar
def buscar_componente(id):
    if id in tabela_componente:
        return tabela_componente[id]
    else:
        print("ID não encontrado!")

adicionar_componente(1, 'Produzindo', 'Setor A', 'NOVO')
adicionar_componente(2, 'Produzindo', 'Setor A', 'NOVO')
adicionar_componente(3, 'VENDIDO', 'Sem setor', 'Sem historico')
atualizar_componente(2, 'Produzido', 'Setor B', 'NOVO')
atualizar_componente(3, 'VENDIDO', 'Sem setor', 'Sem historico')
buscar_componente(2)
print(buscar_componente(4))