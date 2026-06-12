from itertools import product


class InterpretadorLogico:

    def __init__(self):
        self.precedencia = {
            "~": 5,
            "^": 4,
            "v": 3,
            "->": 2,
            "<->": 1
        }

    def validar_parenteses(self, expressao):

        contador = 0

        for caractere in expressao:

            if caractere == "(":
                contador += 1

            elif caractere == ")":
                contador -= 1

            if contador < 0:
                return False

        return contador == 0

    def tokenizar(self, expressao):

        tokens = []
        i = 0

        while i < len(expressao):

            if expressao[i].isspace():
                i += 1
                continue

            if expressao[i].isalpha():
                tokens.append(expressao[i])

            elif expressao[i] in "()^v~":
                tokens.append(expressao[i])

            elif expressao[i:i + 3] == "<->":
                tokens.append("<->")
                i += 3
                continue

            elif expressao[i:i + 2] == "->":
                tokens.append("->")
                i += 2
                continue

            i += 1

        return tokens

    def para_posfixa(self, tokens):

        saida = []
        pilha = []

        for token in tokens:

            if token.isalpha():
                saida.append(token)

            elif token == "(":
                pilha.append(token)

            elif token == ")":

                while pilha and pilha[-1] != "(":
                    saida.append(pilha.pop())

                if pilha:
                    pilha.pop()

            else:

                while (
                    pilha
                    and pilha[-1] != "("
                    and self.precedencia[pilha[-1]] >= self.precedencia[token]
                ):
                    saida.append(pilha.pop())

                pilha.append(token)

        while pilha:
            saida.append(pilha.pop())

        return saida

    def avaliar(self, posfixa, valores):

        pilha = []

        for token in posfixa:

            if token.isalpha():
                pilha.append(valores[token])

            elif token == "~":

                a = pilha.pop()
                pilha.append(not a)

            else:

                b = pilha.pop()
                a = pilha.pop()

                if token == "^":
                    pilha.append(a and b)

                elif token == "v":
                    pilha.append(a or b)

                elif token == "->":
                    pilha.append((not a) or b)

                elif token == "<->":
                    pilha.append(a == b)

        return pilha.pop()


def obter_variaveis(expressao):

    return sorted(
        set(
            caractere
            for caractere in expressao
            if caractere.isalpha()
        )
    )


def obter_valores(variaveis):

    valores = {}

    print("\nInforme os valores lógicos:")

    for var in variaveis:

        while True:

            valor = input(f"{var} (V/F): ").upper()

            if valor in ["V", "F"]:
                valores[var] = valor == "V"
                break

            print("Digite apenas V ou F.")

    return valores


def avaliar_formula():

    interpretador = InterpretadorLogico()

    expressao = input("\nDigite a fórmula: ")

    if not interpretador.validar_parenteses(expressao):
        print("\nErro: parênteses não balanceados.")
        return

    tokens = interpretador.tokenizar(expressao)
    posfixa = interpretador.para_posfixa(tokens)

    variaveis = obter_variaveis(expressao)
    valores = obter_valores(variaveis)

    resultado = interpretador.avaliar(posfixa, valores)

    print("\nTokens:")
    print(tokens)

    print("\nExpressão Pós-Fixa:")
    print(posfixa)

    print("\nResultado Final:")

    if resultado:
        print("VERDADEIRO")
    else:
        print("FALSO")


def gerar_tabela_verdade():

    interpretador = InterpretadorLogico()

    expressao = input("\nDigite a fórmula: ")

    if not interpretador.validar_parenteses(expressao):
        print("\nErro: parênteses não balanceados.")
        return

    tokens = interpretador.tokenizar(expressao)
    posfixa = interpretador.para_posfixa(tokens)

    variaveis = obter_variaveis(expressao)

    print("\nTabela-Verdade\n")

    cabecalho = ""

    for var in variaveis:
        cabecalho += f"{var} | "

    cabecalho += "Resultado"

    print(cabecalho)
    print("-" * len(cabecalho))

    for combinacao in product([True, False], repeat=len(variaveis)):

        valores = {}

        for i in range(len(variaveis)):
            valores[variaveis[i]] = combinacao[i]

        resultado = interpretador.avaliar(posfixa, valores)

        linha = ""

        for var in variaveis:

            if valores[var]:
                linha += "V | "
            else:
                linha += "F | "

        linha += "V" if resultado else "F"

        print(linha)


def menu():

    while True:

        print("\n" + "=" * 50)
        print("INTERPRETADOR DE FÓRMULAS PROPOSICIONAIS")
        print("=" * 50)

        print("1 - Avaliar fórmula")
        print("2 - Gerar tabela-verdade")
        print("3 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            avaliar_formula()

        elif opcao == "2":
            gerar_tabela_verdade()

        elif opcao == "3":
            print("\nEncerrando programa...")
            break

        else:
            print("\nOpção inválida.")


if __name__ == "__main__":
    menu()