class Leitura:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def __str__(self):
        return self.name

    def __repr__(self):
        return f'ID: {self.id}-Nome:{self.name}'

class Sensor:
    def __init__(self, id: int, leituras: []):
        self.id = id
        self.leituras = leituras
    
    def __str__(self):
        return self.leituras
    

class Tabela:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho
    
    def hash(self, value):
        return value % self.tamanho
    
    def push(self, valor: Sensor):
        chave = self.hash(valor.id)
        if self.tabela[chave] is None:
            self.tabela[chave] = [valor.leituras]
        else:
            self.tabela[chave].append(valor)
            
    def search(self, id: int):
        chave = self.hash(id)
        return self.tabela[chave]
    
    def remove(self, valor: Sensor):
        chave = self.hash(valor.id)
        self.tabela.pop(chave)


if __name__ == '__main__':
    tabela = Tabela(10)
    leitura1 = Leitura(1, "leitura 1")
    leitura2 = Leitura(2, "leitura 2")
    leitura3 = Leitura(3, "leitura 3")
    sensor1= Sensor(1, [leitura1, leitura2, leitura3])
    sensor2 = Sensor(2, [leitura1, leitura2, leitura3])
    tabela.push(sensor1)
    tabela.push(sensor2)
    print(tabela.search(2))