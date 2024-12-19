class Restaurante: 
    
    # construtor
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
        
    
restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')



print(restaurante_praca)