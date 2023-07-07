class ValidaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class ExpressionConverter:
    def __init__(self):
        self.__prioridade = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
        self.__operadores = ['+', '-', '*', '/', '^']

    def validar_expressao(self, expressao):                     #                                  Validar Expressão
        pilha_parenteses = []                                   # Cria uma lista vazia que será utilizada para o rastreio dos parênteses, posteriormente
        operador_esperado = False                               # será verificado se é um operador é valido, iniciamos um loop para iterar cada
                                                                # caractere fazendo a verificação de operador, operando e também os parênteses tanto
        for i, caractere in enumerate(expressao):               #  de abertura como o de fechamento.
            if caractere.isalpha():
                if operador_esperado:
                    raise ValidaException("Expressão inválida: Operador esperado, mas encontrado um caractere alfabético: '{}'".format(caractere))
                operador_esperado = True
            elif caractere in self.__operadores:
                if not operador_esperado:
                    raise ValidaException("Expressão inválida: Expressão não pode iniciar com operador '{}'".format(caractere))
                if i + 1 >= len(expressao):
                    raise ValidaException("Expressão inválida: o operador '{}' não tem um operando ou parêntese de abertura correspondente.".format(caractere))
                proximo_caractere = expressao[i + 1]
                if not proximo_caractere.isalpha() and proximo_caractere != '(':
                    raise ValidaException("Expressão inválida: o operador '{}' não tem um operando ou parêntese de abertura correspondente.".format(caractere))
                operador_esperado = False
            elif caractere == '(':
                if operador_esperado:
                    raise ValidaException("Expressão inválida: Operador esperado, mas encontrado um parêntese aberto: '{}'".format(caractere))
                pilha_parenteses.append(caractere)
            elif caractere == ')':
                if not pilha_parenteses or pilha_parenteses[-1] != '(':
                    raise ValidaException("Expressão inválida: Parêntese fechado sem parêntese aberto correspondente: '{}'".format(caractere))
                pilha_parenteses.pop()
        if pilha_parenteses:
            raise ValidaException("Expressão inválida: A análise foi concluída, mas a expressão ainda possui parênteses pendentes.")

        return True

    def convercao_pos(self, expressao, passo_a_passo=False):
        posfixa = ''                                               #                            MÉTODO convercao_pos           
        pilha = []                                                 # Percorre a expressão, verifica se o caractére é letra, parentese ou operador, se for letra, converte para minúscula
        tabela_passo_a_passo = []                                  # e concatena direto na string "posfixa", se for parentese de abertura "(", é adicionado na pilha, já se for de fechamento ")",
                                                                   # e concatena direto na string "posfixa", se for parentese de abertura "(", é adicionado na pilha, já se for de fechamento ")",
        for caractere in expressao:                                # irá verificar se a pilha não está vazia e se no topo da pilha existe um parentese de abertura, se existir,
            if caractere.isalpha():                                # será removido da pilha, se não, o caractér que estiver no topo da pilha será concatenado na string até encontrar
                posfixa += caractere.lower()                       # um parentese de abertura, se for operador, verifica se a pilha não está vazia, se o topo da pilha é um parentese
            elif caractere == '(':                                 # aberto "(" e a prioridade do operador, caso uma dessas condições retorne False, o caracter é adicionado à pilha,
                pilha.append(caractere)                            # caso contrário será concatenado a string "posfixa".
            elif caractere == ')':                                 # retorna a expressão convertida em posfixa.
                while pilha and pilha[-1] != '(':
                    posfixa += pilha.pop()
                if pilha and pilha[-1] == '(':
                    pilha.pop()
            elif caractere in self.__operadores:
                while pilha and pilha[-1] != '(' and self.__prioridade[caractere] <= self.__prioridade.get(pilha[-1], 0):
                    posfixa += pilha.pop()
                pilha.append(caractere)

            if passo_a_passo:
                tabela_passo_a_passo.append((caractere, pilha.copy(), posfixa))         # Mostra passo a passo a formulação da tabela.
        if passo_a_passo:
            # Cabeçalho da tabela passo a passo
            print(f"{'Caractere':<10} {'Pilha':<10} {'Pósfixa':<10}")
            print('-' * 35)
            for passo in tabela_passo_a_passo:
                caractere, pilha, posfixa = passo
                pilha_str = ''.join(pilha)
                print(f"{caractere:<10} {pilha_str:<10} {posfixa:<10}")

        while pilha:
            posfixa += pilha.pop()                                 # Se restar algo dentro da pilha após a varredura da expressão, é concatenado na string.

        return posfixa

    def convercao_pre(self, expressao, passo_a_passo=False):
        prefixa = ''
        pilha = []
        tabela_passo_a_passo = []

        for caractere in reversed(expressao):                       #                                    MÉTODO convercao_pre
            if caractere.isalpha():                                 # Pecorre a expressão infixa de trás pra frente, verifica se o caractére é letra, parentese ou operador,
                prefixa = caractere.lower() + prefixa               # se for letra, converte para minúscula e concatena direto na string "prefixaa", se for parentese de fechamento
            elif caractere == ')':                                  # ")", é adicionado na pilha, já se for de abertura "(", irá verificar se a pilha não está vazia e se no topo da
                pilha.append(caractere)                             # pilha existe um parentese de fechamento, se existir, será removido da pilha, se não, o caractér que estiver no topo da pilha
            elif caractere == '(':                                  # será concatenado na string até encontrar um parentese de fechamento, se for operador, verifica se a pilha não está
                while pilha and pilha[-1] != ')':                   # vazia, se o topo da pilha é um parentese fechado ")" e a prioridade do operador, caso uma dessas condições retorne False,
                    prefixa = pilha.pop() + prefixa                 # o caracter é adicionado à pilha, caso contrário será concatenado a string "prefixaa".
                if pilha and pilha[-1] == ')':                      # retorna a expressão convertida em prefixaa.
                    pilha.pop()
            elif caractere in self.__operadores:
                while pilha and pilha[-1] != ')' and self.__prioridade[caractere] <= self.__prioridade.get(pilha[-1], 0):
                    prefixa = pilha.pop() + prefixa
                pilha.append(caractere)

            if passo_a_passo:
                tabela_passo_a_passo.append((caractere, pilha.copy(), prefixa))  

        if passo_a_passo:
        # Cabeçalho da tabela passo a passo
            print(f"{'Caractere':<10} {'Pilha':<10} {'Préfixa':<10}")
            print('-' * 35)
            for passo in tabela_passo_a_passo:
                caractere, pilha, prefixa = passo
                pilha_str = ''.join(pilha)
                print(f"{caractere:<10} {pilha_str:<10} {prefixa:<10}")
          
        while pilha:
            prefixa = pilha.pop() + prefixa                          # Se restar algo dentro da pilha após a varredura da expressão, é concatenado na string.

        return prefixa

    def calcular(self, expressao):
        pilha = []                                                
                                                                        #                                 MÉTODO calcular
        for caractere in expressao:                                     # Varre a expressão convertida para pósfixa, verifica se o caractér é letra, se for, pede ao usuário
            if caractere.isalpha():                                     # um valor a ser atribuido e adiciona esse valor a pilha, caso seja operador, retira 2 operandos da pilha,
                operando = float(input(f'Valor para {caractere}: '))    # armazenando em variáveis e executa a operação utilizando o método "executar_operacao", jogando o resultadoado
                pilha.append(operando)                                  # na pilha até a expressão ser completamente varrida.
            elif caractere in self.__operadores:                          # retorna o resultado final da expressão.
                operando2 = pilha.pop()
                operando1 = pilha.pop()
                resultado = self.__executar_operacao(caractere, operando1, operando2)
                pilha.append(resultado)

        resultado = pilha[0]
        return resultado

    def __executar_operacao(self, operador, operando1, operando2):
        if operador == '+':
            return operando1 + operando2                              #                        MÉTODO executar_operacao
        elif operador == '-':                                         # Executa operações matemáticas de acordo com o operador fornecido, funciona em conjunto aos
            return operando1 - operando2                              # métodos "calcular_pos" e "calcular_pre".
        elif operador == '*':
            return operando1 * operando2
        elif operador == '/':
            return operando1 / operando2
        elif operador == '^':
            return operando1 ** operando2