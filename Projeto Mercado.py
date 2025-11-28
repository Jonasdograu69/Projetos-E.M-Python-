from collections import Counter

carrinho = []
catalogo = {}   

senha_adm = "4321"
senha_cliente = "1234"

while True:
    login = input("Senha: ")

    
    if login == senha_cliente:
        while True:
            print("\n")

            if carrinho:
                contagem = Counter(carrinho)
                print("Carrinho:")
                for produto, qtd in contagem.items():
                    print(f"{qtd}x {produto}")
            else:
                print("Carrinho vazio.")

            if catalogo:
                print("\nCatálogo atual:")
                for produto, dados in catalogo.items():
                    print(f'{dados["qtd"]}x {produto} — R${dados["preco"]:.2f}')
            else:
                print("\nCatálogo vazio.")

            add = input('\nDigite o produto para adicionar ao carrinho. '
                        'Para sair, digite "sair". '
                        'Para finalizar a compra, digite (F):\n').lower()

            if add == "sair":
                print("A suas ordens")
                break

           
            if add == "f":
                if not carrinho:
                    print("Carrinho vazio, não há compra para finalizar.")
                    continue

                total = 0
                contagem = Counter(carrinho)

                print("\n---- RESUMO DA COMPRA ----")
                for produto, qtd in contagem.items():
                    preco_unit = catalogo[produto]["preco"]
                    subtotal = preco_unit * qtd
                    total += subtotal
                    print(f"{qtd}x {produto} — R${preco_unit:.2f} cada — Subtotal: R${subtotal:.2f}")

                print(f"\nTOTAL: R${total:.2f}")
                print("Compra finalizada!")

                carrinho.clear()
                break

           
            if add not in catalogo:
                print("Produto inexistente no catálogo")

            elif catalogo[add]["qtd"] == 0:
                print("Produto sem estoque")

            else:
                carrinho.append(add)
                catalogo[add]["qtd"] -= 1
                print(f"{add} adicionado ao carrinho!")

    
    elif login == senha_adm:
        print("Bem vindo, ADM!")

        while True:
            decisao_adm = input(
                'Digite (C) para cadastrar produto ao catálogo ou "sair" para encerrar:\n'
            ).lower()

            if decisao_adm == "sair":
                print("A suas ordens!")
                break

            elif decisao_adm == "c":
                produto = input("Nome do produto:\n").strip()

                if produto == "":
                    print("Produto inválido.")
                    continue

                quantidade = int(input("Quantidade a adicionar:\n"))
                preco = float(input("Preço do produto:\n"))

                if produto in catalogo:
                    catalogo[produto]["qtd"] += quantidade
                    print("Produto já existia. Quantidade atualizada.")
                
                else:
                    catalogo[produto] = {"qtd": quantidade, "preco": preco}
                    print("Produto adicionado ao catálogo.")

                print(f'Estoque atual de "{produto}": {catalogo[produto]["qtd"]}')

    
    else:
        print("Senha inválida.")
