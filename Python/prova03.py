#[PYIA-A03] Crie um dicionário para armazenar o nome e o preço de cinco produtos.
# Peça ao usuário para inserir o nome de cada produto e o respectivo preço. À medida
# que o usuário fornece os dados, armazene cada produto como uma chave no dicionário e
# o preço como o valor associado a essa chave. Após a inserção de todos os produtos e preços,
# calcule o valor total da compra somando todos os preços armazenados no dicionário. Por fim,
# exiba o valor total da compra.

produtos = {}
soma = 0

for i in range(5):
    nomeProduto = input("Digite o nome do produto: ")
    precoProduto = float(input("Digite o preço do produto:"))
    
    produtos[nomeProduto] = precoProduto
    soma += precoProduto 
    
print(f"Os produtos foram armazenados: {produtos}")
print(f"Soma de todos os produtos: R${soma:.2f}")
