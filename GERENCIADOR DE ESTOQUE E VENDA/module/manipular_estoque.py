import json

# Funções para manipular o estoque
def salvar_estoque(estoque):
    with open('json/estoque.json', 'w', encoding='utf-8') as arquivo:
        json.dump(estoque, arquivo, indent=4, ensure_ascii=False)

def carregar_estoque():
    try:
        with open('json/estoque.json', 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo 'estoque.json' não encontrado. Criando um novo arquivo.")
        return []
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo. O arquivo pode estar corrompido.")
        return []

def exibir_estoque(estoque):
    if estoque:
        print("\nESTOQUE:")
        for i, item in enumerate(estoque, start=1):
            print(f"\nPRODUTO {i}:")
            print(f"Nome: {item['produto']}")
            print(f"Quantidade: {item['quantidade']}")
    else:
        print("Não há estoque registrado.")