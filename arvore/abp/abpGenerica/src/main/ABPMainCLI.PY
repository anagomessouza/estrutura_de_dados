from ABP import ABP  # Certifique-se de que ABP está definido corretamente

def exibir_menu():
    print("=== Árvore Binária de Pesquisa ===")
    print("0. SAIR")
    print("1. Inserir")
    print("2. Apagar")
    print("3. Existe?")
    print("4. Imprimir")
    print("5. Limpar")
    return input("Escolha uma opção (0-5): ")

def exibir_menu_imprimir():
    print("1. Imprimir Pré-Ordem")
    print("2. Imprimir Em-Ordem")
    print("3. Imprimir Pós-Ordem")
    return input("Escolha uma opção (1-3): ")

def main():
    arvore = ABP()
    while True:
        opcao = exibir_menu()
        if opcao == "0":
            print("Saindo da ABP. Até mais!")
            break
        elif opcao == "1":
            try:
                valor = int(input("Digite o valor: "))
                arvore.inserir(valor)
            except ValueError:
                print("Entrada inválida.")
        elif opcao == "2":
            try:
                valor = int(input("Digite o valor: "))
                arvore.apagar(valor)
            except ValueError:
                print("Entrada inválida.")
        elif opcao == "3":
            try:
                valor = int(input("Digite o valor: "))
                print(arvore.existe(valor))
            except ValueError:
                print("Entrada inválida.")
        elif opcao == "4":
            tipo = exibir_menu_imprimir()
            if tipo == "1":
                print(f"\nPré-Ordem: {arvore.imprimir_pre_ordem()}\n")
            elif tipo == "2":
                print(f"\nEm-Ordem: {arvore.imprimir_em_ordem()}\n")
            elif tipo == "3":
                print(f"\nPós-Ordem: {arvore.imprimir_pos_ordem()}\n")
            else:
                print("Opção inválida.")
        elif opcao == "5":
            arvore.limpar()
            print("Árvore limpa!")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
