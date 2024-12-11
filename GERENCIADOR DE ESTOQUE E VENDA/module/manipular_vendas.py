import json

def salvar_vendas(vendas):
    with open('json/vendas.json', 'w', encoding='utf-8') as arquivo:
        json.dump(vendas, arquivo, indent=4, ensure_ascii=False)

def carregar_vendas():
    try:
        with open('json/vendas.json', 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo 'vendas.json' não encontrado. Criando um novo arquivo.")
        return []
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo. O arquivo pode estar corrompido.")
        return []

def exibir_vendas(vendas):
    if vendas:
        print("\nVENDAS REALIZADAS:")
        for i, venda in enumerate(vendas, start=1):
            print(f"\nVENDA {i}:")
            print(f"Produto: {venda['produto']}")
            print(f"Preço: R$ {venda['preço']:.2f}")
            print(f"Quantidade vendida: {venda['quantidade']}")
            print(f"Total: R$ {venda['total']:.2f}")
    else:
        print("Não há vendas registradas.")