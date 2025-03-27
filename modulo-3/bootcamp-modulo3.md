# Módulo 3 - Trabalhando com Coleções em Python

## 1. Listas
Listas em Python podem armazenar de maneira sequencial qualquer tipo de objeto. Podemos criar listas utilizando o construtor **list**, a função range ou colocando valores separados por vírgula dentro de colchetes. Listas são objetos mutáveis, portanto podemos alterar seus valores após a criação.

Exemplos:

    frutas = ["laranja", "maçã", "uva"]
    frutas = [] # lista vazia
    letras = list("python")
    numeros = list(range(10))
    carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]

- Acesso direto

A lista é uma sequência, portanto podemos acessar seus dados utilizandos índices. Contamos o índice de determinada sequência a partir do zero. As sequências também suportam indexação negativa. A contagem começa em -1.

- Listas aninhadas

Listas podem armazenar todos os tipos de objetos Python, portanto podemos ter listas que armazenam outras listas. Com isso podemos criar estruturas bidimensionais (tabelas), e acessar informando os índices de linha e coluna.

- Fatiamento

Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequência. Para isso, basta passar o índice inicial e/ou final para acessar o conjunto. Podemos ainda informar quantas posições o cursor deve "pular" no acesso.

- Iterar listas

A forma mais comum para percorrer os dados de uma lista é utilizando comando for.

- Função enumerate

Às vezes é necessário saber qual o índice do objeto dentro do laço for. Para isso podemos usar a função enumerate.

- Compreensão de listas

Oferece uma sintaxe mais curta quando você deseja: criar uma nova lista com base nos valores de uma lista existente(filtro) ou gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente.

### 1.1 Métodos da Classe List
- Append

[].append() adiciona um novo elemento à lista. 

- Clear

[].clear() limpa os dados da lista, deixando-a vazia.

- Copy

[].copy() copia a lista e a torna independente da sua original.

- Count

[].count() conta quantas vezes um determinado objeto aparece na lista.

- Extend

[].extend() adiciona uma nova lista a uma já existente.

- Index

[].index() retorna em qual posição o objeto aparece pela primeira vez.

- Pop

[].pop() retira, por padrão, sempre o último elemento da lista. Pode retirar um específico, se nomeado.

- Remove

[].remove() outra forma de remover um objeto da lista, diferente do pop, nele você passa o nome do objeto que deseja remover. 

- Reverse

[].reverse() faz o espelhamento da lista.

- Sort

[].sort() faz o ordenamento da lista em ordem alfabética. Pode receber argumentos. **reverse=True** traz o ordenamento alfabético ao contrário. **key=lambda** faz alterações de acordo com o declarado.

- Len

[].len() retorna o tamanho dos objetos.

- Sorted

sorted([]) similar ao sort.

- Insert

[].insert() adiciona um elemento a uma posição específica da lista.

- Sum

sum([]) retorna a soma de números de uma lista.

- Max

max([]) retorna o maior elemento de uma lista.

- Min

min([]) retorna o menor elemento de uma lista.

## 2. Tuplas

Tuplas são estruturas de dados muito parecidas com as listas, a principal diferença é que tuplas são imutáveis enquanto listas são mutáveis. Ou seja, enquanto as listas podem sofrer alterações no desenvolvimento do código, as tuplas não podem e permanecerão inalteradas. Podemos criar tuplas através da classe **tuple**, ou colocando valores separados por vírgula entre parenteses. 

Exemplos

    frutas = ("laranja", "pera", "uva",)
    letras = tuple("python")
    numeros = tuple([1,2,3,4])
    pais = ("Brasil",)

## 3. Conjuntos

Um set é uma coleção que não possui objetos repetidos, usamos sets para representar conjuntos matemáticos ou eliminar itens duplicados de um iterável.

- Acessando os Dados

Conjuntos em Python não suportam indexação e nem fatiamento, caso queira acessar os seus valores é necessário converter o conjunto para lista.

- Iterar Conjuntos

A forma mais comum para percorrer os dados de um conjunto é utilizando o comando for.

### 3.1 Métodos da Classe Set
- União

{}.union({}) faz a união de conjuntos. Pode ser utilizado o *|*.

- Intersecção

{}.intersection({}) faz a intersecção de conjuntos. Pode ser utilizado o *&*

- Diferença

{}.difference.({}) retorna a diferença entre os conjuntos. Os elementos que estão no primeiro, mas não no segundo. Pode ser utilizado o *-*

- Diferença Simétrica

{}.symetric_difference({}) retorna os elementos que estão em um, mas não em ambos. Pode ser utilizado o *^*

- Issubset

{}.issubset({}) verifica se todos os elementos de um conjunto estão presente em outro, se um é subconjunto de outro.

- Issuperset

{}.issuperset({}) verifica se todos os elementos de um conjunto estão presentes em outro, se todos os elementos de um estão em outro.

- Isdisjoint

{}.isdisjoint({}) verifica se os conjuntos não têm elementos em comum. Dois conjuntos são disjuntos se a interseção entre eles for vazia.

- Add

{}.add() adiciona elementos ao final do conjunto.

- Clear

{}.clear() limpa os dados do conjunto.

- Copy

{}.copy() faz a cópia do conjunto, tornando-o independente.

- Discard

{}.discard() discarta um número específico.

- Pop 

{}.pop() remove elementos do conjunto, da esquerda para direita.

- Remove

{}.remove() remove um número específico. Diferente do discard, se tentar remover um elemento que não existe, dará algum erro.

- Len

{}.len() retira o valor total do conjunto, quantos objetos estão contidos nele.

- In

in utilizado para verificar se um elemento está dentro do conjunto.

## 4. Dicionários

Um dicionário é um conjunto não-ordenado de pares chave:valor, onde as chaves são únicas em uma dada instância do dicionário. Dicionários são delimitados por chaves: {}, e contém uma lista de pares chave:valor separada por vírgulas, também é possível declarar por meio da palavra **dict**.

- Acesso aos dados

Os dados são acessados e modificados através da chave.

- Dicionários aninhados

Dicionários podem armazenar qualquer tipo de objeto Python como valor, desde que a chave para esse valor seja um objeto imutável como strings e números.

- Iterar dicionários

A forma mais comum para percorrer os dados de um dicionário é utilizando o comando for.

### 4.1 Métodos da classe Dict

- Clear

{}.clear() limpa os dados do dicionário.

- Copy

{}.copy() copia um dicionário, tornando-o independente.

- Fromkeys

{}.fromkeys() capaz de criar valores para uma lista que é passada, tornando-se um dicionário.

- Get

{}.get() outra forma de acessar valores de um dicionário. Útil para quando quer acessar uma chave de uma dicionário, mas não tem certeza se ela existe. Por padrão retornará *None* se não existir. Também é possível pedir para retornar um dicionário vazio a essa chave se ela não existir ou um valor específico. 

- Items

{}.items() retorna uma lista de tupla com os valores contidos no seu dicionário. 

- Keys

{}.keys() retorna apenas as chaves do dicionários e não os seus valores.

- Pop

{}.pop() remove uma chave e retorna seu valor, se não existir, é possível atribuir um dicionário vazio ou valor específico.


- Pop Item

{}.popitem() diferente do acima, não informamos a chave que será removida, ele remove uma a uma, se não houver mais o que remover, irá retornar um KeyError.

- Set Default

{}.setdefault() é capaz de adicionar uma chave com valor ao dicionário, mas se já existir, seu valor não é modificado.

- Update

{}.update() atualiza as chaves e seus valores. Se não existirem, irá adicionar ao dicionário.

- Values

{}.values() retorna apenas os valores do dicionário e não as suas chaves.

- In

in verifica se há uma chave no dicionário.

- Del

Remove um valor específico ou toda a chave do dicionário, a depender do que for informado.