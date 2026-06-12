class InterpretadorLogico:

    def __init__(self):
        self.precedencia = {
            "~": 5,
            "^": 4,
            "v": 3,
            "->": 2,
            "<->": 1
        }

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

            elif expressao[i:i+3] == "<->":
                tokens.append("<->")
                i += 3
                continue

            elif expressao[i:i+2] == "->":
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
                    pilha and
                    pilha[-1] != "(" and
                    self.precedencia[pilha[-1]] >= self.precedencia[token]
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


def obter_valores(expressao):

    variaveis = sorted(
        set(c for c in expressao if c.isalpha())
    )

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


def main():

    print("=" * 50)
    print("INTERPRETADOR DE FÓRMULAS PROPOSICIONAIS")
    print("=" * 50)

    expressao = input("\nDigite a fórmula lógica: ")

    interpretador = InterpretadorLogico()

    tokens = interpretador.tokenizar(expressao)

    posfixa = interpretador.para_posfixa(tokens)

    valores = obter_valores(expressao)

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


if __name__ == "__main__":
    main()