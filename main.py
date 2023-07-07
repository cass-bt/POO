from projeto_v8 import ExpressionConverter
from projeto_v8 import ValidaException

def main():
    conversor = ExpressionConverter()
    expressao = None
    reset = False

    while expressao == None:
        expressao = input("Digite uma expressão no formato infixo (ou 'sair' para encerrar): ")

        if expressao.lower() == 'sair':
            reset = True
            break

        try:
            conversor.validar_expressao(expressao)
            print("")
            print("A expressão é válida.")

        except ValidaException as ve:
            print(str(ve))
            expressao = None
            continue


    while reset == False:
        print("\n============ Menu ============")
        print("(p) Converter para pós-fixa")
        print("(i) Converter para pré-fixa")
        print("(e) Associar valores e Executar")
        print("(s) Sair")

        print()
        opcao = input("Escolha uma opção: ")
        print()

        if opcao == 'p':
            option = input("Deseja visualizar a conversão passo-a-passo? (S/N): ")
            print()
            if option.lower() == 's':
                if expressao:
                    posfixa = conversor.convercao_pos(expressao, passo_a_passo=True)
                    print()
                    print("Expressão em pósfixa:", posfixa)
                else:
                    print("Nenhuma expressão definida.")
            elif option.lower() == 'n':
                if expressao:    
                    posfixa = conversor.convercao_pos(expressao, passo_a_passo=False)
                    print("Expressão em pósfixa:", posfixa)
                else:
                    print("Nenhuma expressão definida.")
            else:
                print("Opção inválida")

        elif opcao == 'i':
            option = input("Deseja visualizar a conversão passo-a-passo? (S/N): ")
            print()
            if option.lower() == 's':
                if expressao:
                    prefixa = conversor.convercao_pre(expressao, passo_a_passo=True)
                    print()
                    print("Expressão em préfixa:", prefixa)
                else:
                    print("Nenhuma expressão definida.")
            elif option.lower() == 'n':
                if expressao:    
                    prefixa = conversor.convercao_pre(expressao, passo_a_passo=False)
                    print("Expressão em préfixa:", prefixa)
                else:
                    print("Nenhuma expressão definida.")
            else:
                print("Opção inválida")
        elif opcao == 'e':
            if expressao:
                posfixa = conversor.convercao_pos(expressao)
                try:
                    resultado = conversor.calcular(posfixa)
                    print("Resultado da expressão:", resultado)
                except ValueError as erro:
                    print("Erro:", str(erro))
            else:
                print("Nenhuma expressão definida.")
        elif opcao == 's':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()