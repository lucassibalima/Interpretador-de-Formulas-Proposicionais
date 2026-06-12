# 🧠 Interpretador de Fórmulas Proposicionais

Projeto desenvolvido em Python para interpretar e avaliar fórmulas da Lógica Proposicional.

O programa recebe uma expressão lógica composta por proposições e operadores lógicos, solicita os valores de verdade das variáveis e retorna o resultado final da fórmula.

---

## 👨‍💻 Autor

Lucas Siba de Lima

Leo Mezzadri

Edilberto Garipuna


Curso de Ciência da Computação

---

## 📋 Funcionalidades

* Identificação automática das variáveis da expressão
* Conversão da expressão para notação pós-fixa
* Avaliação de fórmulas proposicionais
* Suporte a múltiplos operadores lógicos
* Implementação utilizando pilhas e manipulação de listas
* Interface simples via terminal

---

## 🔧 Operadores Suportados

| Operador | Significado    |
| -------- | -------------- |
| `~`      | Negação (NÃO)  |
| `^`      | Conjunção (E)  |
| `v`      | Disjunção (OU) |
| `->`     | Implicação     |
| `<->`    | Bicondicional  |

---


## 💻 Exemplo de Uso

### Entrada

```text
(P ^ Q) -> R
```

### Valores Informados

```text
P = V
Q = F
R = V
```

### Saída

```text
Resultado Final:
VERDADEIRO
```

---

## 🧩 Exemplos de Fórmulas

```text
P ^ Q

~P

(P v Q)

(P -> Q)

(P <-> Q)

((P ^ Q) -> (~R v S))

((P -> Q) ^ (Q -> R))
```

---


## 🛠️ Conceitos Utilizados

* Lógica Proposicional
* Estruturas de Dados
* Pilhas (Stack)
* Manipulação de Strings
* Conversão Infixa → Pós-fixa
* Avaliação de Expressões
* Programação Orientada a Objetos

---

## 📚 Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de aplicar conceitos de lógica matemática e programação, implementando um interpretador capaz de processar e avaliar fórmulas proposicionais de forma automática.

A solução utiliza o algoritmo de conversão para notação pós-fixa e uma pilha para avaliar as expressões de maneira eficiente.

---


