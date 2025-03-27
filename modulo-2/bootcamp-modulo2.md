# Módulo 2 - Sintaxe Básica com Python

## 1. Operadores aritméticos
| Operador       | Símbolo | Ordem de precedência |
| -------------- | ------- | ----------------- |
| Adição | + | 4 |
| Subtração | - | 4 |
| Multiplicação | * | 3 |
| Divisão | / | 3 |
| Divisão Inteira | // | 3 |
| Módulo | % | 3 |
| Exponenciação | ** | 2 |
| Parênteses | () | 1

**Importante:** Na divisão de inteiro, a operação 6/4 resultaria em 1.5, mas em 6//4 resulta em 1, pois **o arredondamento sempre vai para o número inteiro menor.** Em -6//4 resulta em -2 pois o arredondamento foi para o número menor, ou seja, em -2 que é menor que -1.

**Importante:** o cálculo da expressão de operadores é **sempre** feito da esquerda para a direita, **EXCETO** o operador da exponenciação que usa a associação do lado direito. Ex.: 2 ** 2 ** 3 = 2 ** 3 = 8; 2 ** 8 = 256.

## 2. Operadores de Comparação
| Operador       | Símbolo |
| -------------- | ------- |
| Igual | == |
| Maior ou igual | >= |
| Diferente | != |
| Menor | < |
| Menor ou igual | <= |

## 3. Operadores de Atribuição
Utilizados para definir o valor inicial ou sobrescrever o valor de uma variável.

| Operador                           | Símbolo |
| ---------------------------------- | ------- |
| Atribuição Simples | = |
| Atribuição com Adição | += |
| Atribuição com Subtração | -= |
| Atribuição com Divisão | /= |
| Atribuição com Divisão Inteira | //= |
| Atribuição com Módulo | %= |
| Atribuição com Exponenciação | **= |

## 4. Operadores de Lógicos
| Operador       | Símbolo |
| -------------- | ------- |
| E | and |
| OU | or |
| NÃO | not |

## 5. Operadores de Identidade
Utilizados para comparar se os dois objetos testados ocupam a mesma posição na memória.

**is:** operador de identidade;

**is not:** negação do operador de identidade.

## 6. Operadores de Associação
Utilizados para verificar se um objeto está presente em uma sequência.

**in:** operador de associação;

**not in:** negação do operador de associação.

## 7. Identação e Blocos
Além de manter o código mais legível e manutenível, através da identação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina.

## 8. Estruturas Condicionais
A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.

- if

Para criar uma estrutura condicional simples, composta por um único desvio, podemos utilizar a palavra reservada **if**. O comando irá testar a expressão lógica, e em caso de retorno verdadeiro, as ações presentes no bloco de código do if serão executadas.

- if/else

Para criar uma estrutura condicional com dois desvios, podemos utilizar as palavras reservadas **if** e **else**. Como sabemos sabemos se a expressão lógica testada no if for verdadeira, então o bloco de código do if será executado. Caso contrário, o bloco de código do else será executado.

- if/elif/else

Em alguns cenários, queremos mais de dois desvios, para isso podemos utilizar a palavra reservada **elif**. Não existe um número máximo de elifs para utilizar.

- if aninhado

Podemos criar estruturas condicionais aninhadas, para isso basta adicionar estruturas if/elif/else dentro do bloco de código de estruturas if/elif/else.

- if ternário

Permite escrever uma condição em uma única linha. Ele é composto por três partes:
1. O retorno caso a expressão retorne verdadeiro;
2. A expressão lógica;
3. O retorno caso a expressão retorne falso.

Exemplo:

    saldo = 500
    saque = 400
    status = "Sucesso" if saldo >= saque else "Falha"
    print(f"{status} ao realizar o saque!")
    retorno esperado: sucesso ao realizar o saque!

## 9. Estruturas de Repetição
Utilizados para repetir um trecho de código um determinado número de vezes. Esse número pode ser conhecido previamente ou determinado através de uma expressão lógica.

- for

É usado para percorrer um objeto iterável. Faz sentido usar quando **sabemos o número exato de vezes que nosso bloco de código deve ser executado, ou quando queremos percorrer um objeto iterável.**

Exemplo:

    (1) texto = input("Informe um texto: ") "Python"
    (2) vogais = "AEIOU"
    (3) for letra in texto:
    (4)    if letra.upper() in vogais:
    (5)    print(letra, end=" ")

Explicação do código acima:

O **for** reconhece o objeto a ser iterável, parte por parte, neste caso o texto inserido pelo usuário. O for é composto de duas partes:

1. Qual o objeto iterável quero percorrer? *3. in **texto***
2. Representa o item que está sendo iterado naquele momento. *3. for **letra***

Na primeira volta, ou seja, no primeiro laço, a **letra** terá o valor de **P**, no segundo laço, a letra terá valor de **Y**, seguido de **T**, **H**, **O**, **N**. O for lê item por item do objeto iterável e vai a armazenando na variável definida previamente, neste caso é **letra** mas poderia ter qualquer outro nome permitido. 

Em (4), o *.upper()* transforma todas as letras em maiúsculas, a fim de evitar problemas. Posteriormente, verifica se algum dos itens armazenados em **letra** está contido em **vogais**. 

Em (5), retorna apenas o conteúdo de **letra** que está contido em vogais. O *end=" "* é legal pois deixa o conteúdo de saída lado a lado.

- range

Uma função built-in no Python, usada para produzir uma sequência de número inteiros a partir de um início (inclusivo) para um fim (exclusivo). Ela recebe 3 argumentos: start(opcional), stop(obrigatório), step(opcional).

Exemplo:

    for numero in range(0,51,5):
        print(numero, end=" ")

- while

Usado para repetir um bloco de código várias vezes. Faz sentido usar o while quando **não sabemos o número exato de vezes que nosso bloco de código deve ser executado.**

- break

Utilizado para forçar a parada do laço de repetição caso uma condição seja atendida.

Exemplo:

    while True:
        numero = int(input("Informe um número: "))

        if numero == 10:
            break
        print(numero)

No exemplo acima, quando o usuário digitar 10, o laço de repetição é interrompido.

- continue

Útil para quando queremos pular uma condição dentro do laço.

Exemplo: 

    for numero in range(10):
        if numero == 2:
            continue
        print(numero, end=" ")

No exemplo acima, irá exibir os números de 0 a 9, mas irá pular o número 2.

## 10. Manipulação de Strings
- Upper

.upper() converte todas as letras para maiúsculas.

- Lower

.lower() converte todas as letras para minúsculas.

- Title

.title() converte todas as letras para minúsculas, exceto a primeira.

- Strip

.strip() remove os espaços em branco da direita e da esquerda.

- Lstrip

.lstrip() remove apenas o espaço da esquerda.

- Rstrip

.rstrip() remove apenas o espaço da direita.

- Center

.center(arg, arg2) Centraliza uma string de acordo com o argumento que colocar. Por exemplo, se sua string contém **Python** e passa **10** como argumento, retornará "  Python  ", a string centralizada no espaço indicado e vazio dos lados. Caso coloque o segundo argumento, que é opcional, retornará a string e os espaços serão ocupados com esse argumento. **'#'** retornará **"##Python##"**. 

- Join

("separador".join(nome-string)) Recebe um argumento e une ao iterável. Exemplo: **(".".join(variavel))** retornará **"P.Y.T.H.O.N".**

## 11. Fatiamento de Strings

É uma técnica utilizada para retornar substrings(partes da string original), informando início (start), fim (stop) e passo (step): [start:stop[,step]].

Exemplos:

    nome = "Nadine Martins Carvalho"
    nome[0] # Retorna a primeira letra, pois a contagem inicia em 0
    nome[:6] # Retorna 'Nadine', pois retorna sempre um número anterior
    nome[7:] # Retorna 'Martins Carvalho' pois pulará os 7 primeiros e retorna o restante
    nome[7:14] # Retorna 'Martins' pois pulará os 6 primeiros, retornará do 7 ao 13
    nome[3:8:2] # Retorna 'ieM' pois começará a retornará a partir do 3, pulando de 2 até 8
    nome[:] # Retorna 'Nadine Martins Carvalho' traz toda a string sem fatiamento
    nome[::-1] # Retorna a string invertida

## 12. String Múltiplas Linhas

São definidas informando 3 aspas simples ou duplas durante a atribuição.

## 13. Funções

É um bloco de código identificado por um nome e pode receber uma lista de parâmetros, esses parâmetros podem ou não ter valores padrões.

 - Retornando Valores

 Para retornar um valor, utilizamos a palavra reservada **return**. Toda função Python retorna *None* por padrão.

 - Argumentos Nomeados

 Funções também podem ser chamadas usando argumentos nomeados da forma chave=valor.

 - Args e kwargs

 Podemos combinar parâmetros obrigatórios com args e kwargs. Quando esses são definidos (*args e **kwargs), o método recebe os valores como tupla e dicionário respectivamente. Ou seja, *args(argumentos posicionais variáveis) é usado para passar um *número variável de argumentos posicionais* para uma função e estes são recebidos como uma tupla. **kwargs (argumentos nomeados variáveis) são usados para passar um número variável de argumentos nomeados (chave=valor)* e estes são recebidos como um dicionário.
