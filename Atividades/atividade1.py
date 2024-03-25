'inserindo o carro Brasilia no final da lista:'
carros = [ "Fusca", "Chevette", "Opala", "Maverick", "Fiorino"]
carros.append("Brasilia")
print(carros)

'Inserindo o carro Alfa Romeo no inicio da lista:'
carros = [ "Fusca", "Chevette", "Opala", "Maverick", "Fiorino"]
carros.insert(0, 'Alfa Roneo')
print(carros)

'Inserindo o carro corcel entre o CHevette e o Opala:'
carros = [ "Fusca", "Chevette", "Opala", "Maverick", "Fiorino"]
carros.insert(2, 'Corsel')
print(carros)

'Removendo o carro maverick da lista:'
carros = [ "Fusca", "Chevette", "Opala", "Maverick", "Fiorino"]
item = "Maverick"
carros.remove(item)
print(carros)
