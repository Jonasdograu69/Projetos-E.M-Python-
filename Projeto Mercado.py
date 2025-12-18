from collections import Counter

senha_adm = "4321"
senha_cliente = "1234"


def mostrar_catalogo(catalogo):
    if not catalogo:
        print("Catálogo vazio.")
        return {}

    print("\nCatálogo:")
    mapa = {}
    for i, (produto, dados) in enumerate(catalogo.items(), start=1):
        print(f"{i} - {produto} ({dados['qtd']}x) - R${dados['preco']:.2f}")
        mapa[i] = produto

    return mapa


def adicionar_produto(carrinho, catalogo):
    mapa = mostrar_catalogo(catalogo)
    if not mapa:
        return

    try:
        escolha = int(input("\nDigite o número do produto: "))
        if escolha not in mapa:
            print("Produto inválido.")
            return

        quantidade = int(input("Digite a quantidade desejada: "))
        if quantidade <= 0:
            print("Quantidade inválida.")
            return

    except ValueError:
        print("Entrada inválida.")
        return

    produto = mapa[escolha]

    if catalogo[produto]["qtd"] < quantidade:
        print("Estoque insuficiente.")
        return

    for _ in range(quantidade):
        carrinho.append(produto)

    catalogo[produto]["qtd"] -= quantidade
    print(f"{quantidade}x {produto} adicionado(s) ao carrinho!")


def mostrar_carrinho(carrinho):
    if not carrinho:
        print("Carrinho vazio.")
        return

    contagem = Counter(carrinho)
    print("\nCarrinho:")
    for produto, qtd in contagem.items():
        print(f"{qtd}x {produto}")


def finalizar_compra(carrinho, catalogo):
    if not carrinho:
        print("Carrinho vazio, não há compra para finalizar.")
        return

    contagem = Counter(carrinho)
    total = 0

    print("\n---- RESUMO DA COMPRA ----")
    for produto, qtd in contagem.items():
        preco_unit = catalogo[produto]["preco"]
        subtotal = preco_unit * qtd
        total += subtotal
        print(f"{qtd}x {produto} — R${preco_unit:.2f} — Subtotal: R${subtotal:.2f}")

    print(f"\nTOTAL: R${total:.2f}")
    print("Compra finalizada!")

    carrinho.clear()


def adicionar_catalogo(catalogo):
    produto = input("Nome do produto:\n").strip()
    if not produto:
        print("Produto inválido.")
        return

    try:
        quantidade = int(input("Quantidade a adicionar:\n"))
        preco = float(input("Preço do produto:\n"))
    except ValueError:
        print("Entrada inválida.")
        return

    if produto in catalogo:
        catalogo[produto]["qtd"] += quantidade
        print("Produto já existia. Quantidade atualizada.")
    else:
        catalogo[produto] = {"qtd": quantidade, "preco": preco}
        print("Produto adicionado ao catálogo.")

    print(f'Estoque atual de "{produto}": {catalogo[produto]["qtd"]}')


carrinho = []
catalogo = {}

while True:
    login = input("Senha: ")

    if login == senha_cliente:
        while True:
            try:
                escolha = int(input("""
========================
MENU DO CLIENTE
1 - Adicionar produto ao carrinho
2 - Ver carrinho
3 - Finalizar compra
0 - Sair
========================
Escolha: """))
            except ValueError:
                print("Opção inválida.")
                continue

            if escolha == 0:
                break
            elif escolha == 1:
                adicionar_produto(carrinho, catalogo)
            elif escolha == 2:
                mostrar_carrinho(carrinho)
            elif escolha == 3:
                finalizar_compra(carrinho, catalogo)
            else:
                print("Opção inválida.")

    elif login == senha_adm:
        print("Bem-vindo, ADM!")

        while True:
            try:
                decisao_adm = int(input("""
========================
MENU DO ADM
1 - Adicionar produto ao catálogo
0 - Sair
========================
Escolha: """))
            except ValueError:
                print("Opção inválida.")
                continue

            if decisao_adm == 0:
                break
            elif decisao_adm == 1:
                adicionar_catalogo(catalogo)
            else:
                print("Opção inválida.")

    else:
        print("Senha inválida.")
