produtos = {}
soma = 0

for i in range(5):
    nomeProduto = input("Digite o nome do produto: ")
    precoProduto = float(input("Digite o preço do produto:"))
    
    produtos[nomeProduto] = precoProduto
    soma += precoProduto 
    
print(f"Os produtos foram armazenados: {produtos}")
print(f"Soma de todos os produtos: R${soma:.2f}")
    