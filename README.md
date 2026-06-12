# 🧠 Interpretador de Fórmulas Proposicionais

Um interpretador de lógica proposicional desenvolvido em Python capaz de analisar, avaliar e gerar tabelas-verdade para fórmulas compostas.

O projeto foi desenvolvido com o objetivo de aplicar conceitos de Lógica Matemática e Estruturas de Dados, implementando um interpretador próprio sem o uso de calculadoras proposicionais externas.

---

## 👨‍💻 Autor

Lucas Siba de Lima

Leo Mezzadri

Edilberto Garipuna

🎓 Ciência da Computação – PUCPR

---

## 📖 Sobre o Projeto

A lógica proposicional é uma área fundamental da matemática e da computação utilizada para representar e analisar proposições através de operadores lógicos.

Este interpretador permite que o usuário insira uma fórmula lógica, atribua valores de verdade às proposições e obtenha automaticamente o resultado da expressão.

Além disso, o sistema é capaz de gerar tabelas-verdade completas para qualquer quantidade de variáveis presentes na fórmula.

---

## ✨ Funcionalidades

* ✅ Avaliação de fórmulas proposicionais
* ✅ Geração automática de tabela-verdade
* ✅ Identificação automática das variáveis
* ✅ Validação de parênteses
* ✅ Conversão de expressões para notação pós-fixa
* ✅ Avaliação utilizando pilha
* ✅ Interface simples via terminal
* ✅ Implementação sem bibliotecas externas

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

## 💻 Exemplos de Fórmulas

```text
P ^ Q

~P

(P v Q)

(P -> Q)

(P <-> Q)

((P ^ Q) -> R)

((P -> Q) ^ (Q -> R))

((P ^ Q) -> (~R v S))
```

---

## 🖥️ Menu Principal

Ao executar o programa, o usuário pode escolher entre:

```text
1 - Avaliar fórmula
2 - Gerar tabela-verdade
3 - Sair
```

---

## 📊 Exemplo de Avaliação

### Fórmula

```text
(P ^ Q) -> R
```

### Valores

```text
P = V
Q = F
R = V
```

### Resultado

```text
VERDADEIRO
```

---

## 📋 Exemplo de Tabela-Verdade

### Fórmula

```text
P -> Q
```

### Saída

| P | Q | Resultado |
| - | - | --------- |
| V | V | V         |
| V | F | F         |
| F | V | V         |
| F | F | V         |

---

## ⚙️ Funcionamento Interno

O programa realiza o processamento da fórmula em três etapas principais:

### 1. Tokenização

A expressão é dividida em componentes menores chamados tokens.

Exemplo:

```text
(P ^ Q) -> R
```

Tokens gerados:

```python
['(', 'P', '^', 'Q', ')', '->', 'R']
```

---

### 2. Conversão para Notação Pós-Fixa

A expressão é convertida para uma forma mais simples de ser avaliada utilizando pilhas.

Expressão original:

```text
(P ^ Q) -> R
```

Resultado:

```text
P Q ^ R ->
```

---

### 3. Avaliação da Expressão

A expressão pós-fixa é processada utilizando uma pilha até que reste apenas um valor lógico, correspondente ao resultado final da fórmula.

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* Programação Orientada a Objetos (POO)
* Estruturas de Dados
* Pilhas (Stack)
* Manipulação de Strings

---

## 📚 Conceitos Aplicados

* Lógica Proposicional
* Tabela-Verdade
* Negação
* Conjunção
* Disjunção
* Implicação
* Bicondicional
* Tokenização
* Parsing de Expressões
* Notação Pós-Fixa
* Avaliação de Expressões

---





