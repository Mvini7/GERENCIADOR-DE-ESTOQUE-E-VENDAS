import module.manipular_estoque as manipular_estoque
import module.manipular_vendas as manipular_vendas

def adicionar_estoque(estoque):
    

    while True:
        try:
            nome_produto = input("Digite o nome do produto: ")
            if nome_produto == "":
                print("\nO nome do produto não pode estar vazio. Tente novamente.\n")
                continue
            quantidade_produto = int(input("Digite a quantidade de produtos: "))
            if quantidade_produto <= 0:
                print("\nA quantidade deve ser maior que zero. Tente novamente.\n")
                continue
            break
        except ValueError:
            print("\nValor inválido. Por favor, insira um número válido.\n")

    novo_item = {
        "produto": nome_produto,
        "quantidade": quantidade_produto
    }
    estoque.append(novo_item)
    manipular_estoque.salvar_estoque(estoque)
    print(f"\nEstoque de {quantidade_produto} unidades de {nome_produto} adicionado com sucesso!")


def adicionar_venda(vendas):
    estoque = manipular_estoque.carregar_estoque()
    manipular_estoque.exibir_estoque(estoque)

    if not estoque:
        print("\nNão há itens no estoque para vender.\n")
        return

    while True:
        try:
            numero_produto = int(input("\nDigite o número do produto do estoque: "))
            if numero_produto <= 0 or numero_produto > len(estoque):
                print("Produto não encontrado. Tente novamente.")
                continue
            break
        except ValueError:
            print("Valor inválido. Digite um número válido.")

    produto_selecionado = estoque[numero_produto - 1]
    print(f"\nProduto selecionado: {produto_selecionado['produto']}")

    while True:
        try:
            preco_produto = float(input("\nDigite o preço do produto: R$ "))
            if preco_produto <= 0:
                print("O preço deve ser maior que zero. Tente novamente.")
                continue
            
            quantidade_vendida = int(input("Digite a quantidade vendida: "))
            if quantidade_vendida <= 0:
                print("A quantidade deve ser maior que zero. Tente novamente.")
                continue
            
            if quantidade_vendida > produto_selecionado['quantidade']:
                print("Quantidade em estoque insuficiente. Tente novamente.")
                continue
            break
        except ValueError:
            print("Valor inválido. Por favor, insira um número válido.")

    total_venda = preco_produto * quantidade_vendida
    produto_selecionado['quantidade'] -= quantidade_vendida
    manipular_estoque.salvar_estoque(estoque)

    venda = {
        "produto": produto_selecionado['produto'],
        "preço": preco_produto,
        "quantidade": quantidade_vendida,
        "total": total_venda
    }
    vendas.append(venda)
    manipular_vendas.salvar_vendas(vendas)

    print(f"\nVenda de {quantidade_vendida} unidades de {produto_selecionado['produto']} adicionada com sucesso!")
    print(f"Estoque atualizado: {produto_selecionado['quantidade']} unidades")

# Gerenciadores principais
def gerenciador_estoque():
    estoque = manipular_estoque.carregar_estoque()
    while True:
        print("\n1. Adicionar estoque")
        print("2. Visualizar estoque")
        print("3. Sair")
        escolha = input("\nEscolha uma opção: ")
        if escolha == "1":
            adicionar_estoque(estoque)
        elif escolha == "2":
            manipular_estoque.exibir_estoque(estoque)
        elif escolha == "3":
            print("Saindo do gerenciador de estoque...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def gerenciador_vendas():
    vendas = manipular_vendas.carregar_vendas()
    while True:
        print("\n1. Visualizar vendas")
        print("2. Visualizar estoque")
        print("3. Adicionar venda")
        print("4. Sair")
        opcao = input("\nDigite o número da opção desejada: ")
        if opcao == "1":
            manipular_vendas.exibir_vendas(vendas)
        elif opcao == "2":
            manipular_estoque.exibir_estoque(manipular_estoque.carregar_estoque())
        elif opcao == "3":
            adicionar_venda(vendas)
        elif opcao == "4":
            print("Saindo do sistema de vendas...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Execução do programa
print("\nBem-vindo ao sistema de gerenciamento!")
while True:
    print("\n1. Gerenciar Estoque")
    print("2. Gerenciar Vendas")
    print("3. Sair")
    escolha = input("\nEscolha uma opção: ")
    if escolha == "1":
        gerenciador_estoque()
    elif escolha == "2":
        gerenciador_vendas()
    elif escolha == "3":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")