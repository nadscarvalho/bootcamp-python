# Módulo 1 - Conhecendo a Linguagem de Programação Python
## 1. Modo Interativo
*Utilizado diretamente no terminal*
- dir

Sem argumentos, retorna a lista de nomes no escopo local atual. Com um argumento, retorna uma lista de atributos válidos para o objeto. **dir()**
- help

Invoca o sistema de ajuda integrado. É possível fazer buscas em modo interativo ou informar por parâmetro qual o nome do módulo, função, classe, método ou variável. **help()**

## 2. Variáveis e Constantes

- Variável

É um valor mutável, sofrem alterações ao longo da execução do programa.

- Constantes

É um valor imutável, não sofre e/ou não é permitido sofrer alterações. Isso não existe em Python, mas há convenção para a utilização de uma variável como constante: **criar a variável com o nome todo em letras maiúsculas.**

## 3. Conversão de Tipos

Em todos os casos, deve-se seguir os passos de pegar o construtor (int, float, str e etc) e passá-lo para a nova atribuição que se deseja. 
- Inteiro para float

Adiciona a variável anteriormente atribuída como *int* para *float*:

    preco = 10 # perceba que se não há atribuição, logo é um int por definição;
    print(preco) # resultado esperado: 10;
    preco = float(preco) # transforma o int em float;
    print(preco) # resultado esperado: 10.0.

- Float para inteiro

Deve-se basicamente seguir os mesmos passos do exemplo acima:

    preco = 10.30 # perceba que já adicionamos o ponto, logo é reconhecido como float;
    print(preco) # resultado esperado: 10.3
    print = int(preco) # transforma o float em int;
    print(preco) # resultado esperado: 10

- Numérico para string

Segue-se os anteriores:

    preco = 10.50;
    idade = 28;
    print(str(preco)) # converte float para string;
    print(str(idade)) # converte int para string:
    texto = f"idade {idade} preco {preco}" # é possível retornar a saída como texto para todos os casos;
    print(texto) # resultado esperado: idade 28 preco 10.5

- String para número

Muito utilizado diariamente:

    preco = "10.50"
    idade = "28"
    preco = float(preco) # converte para float, pode-se fazer assim ou, como no exemplo acima, diretamente no print print(float(preco)). Serve para todos os exemplos de conversão descritos neste tópico.
    idade = int(idade) # converte para int

## 4. Funções de Entrada e Saída
- Função input

Utilizada para quando queremos ler dados da entrada padrão (teclado). Por padrão, recebe o valor informado como string. 

- Função print

Utilizada para quando queremos exibir dados na saída padrão (tela). 


    sep='separador':

    Especifica como os objetos serão separados, se houver mais do que um. O padrão é um espaço em branco. 
--
    end='caractere'

    Especifica o caractere que é impresso no final da linha. O padrão é **\n**, uma quebra de linha.