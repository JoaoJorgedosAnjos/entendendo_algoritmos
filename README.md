
-----

# Entendendo Algoritmos: Implementações

Este repositório contém as minhas implementações dos algoritmos e conceitos apresentados no livro "Entendendo Algoritmos", um guia ilustrado para programadores e curiosos.

-----

## 📚 Sobre o Livro "Entendendo Algoritmos"

"Entendendo Algoritmos" é um livro que simplifica a aprendizagem e a aplicação de algoritmos essenciais da ciência da computação. Ele aborda algoritmos comuns para problemas de programação do dia a dia, começando com tarefas básicas como ordenação e pesquisa, e progredindo para tópicos mais complexos como compressão de dados e inteligência artificial.

O livro se destaca por:

  * Sua **abordagem visual**, com mais de 400 imagens e diagramas detalhados.
  * **Comparações de desempenho** entre diferentes algoritmos.
  * **Exemplos de código em Python** (o que este projeto complementa com outras linguagens\!).

É um recurso excelente para programadores autodidatas, engenheiros ou qualquer pessoa que queira revisar ou aprender algoritmos de forma prática e acessível.

-----

## 💡 Propósito Deste Repositório

Enquanto o livro utiliza **Python** para seus exemplos de código, este repositório tem como objetivo reimplementar e explorar esses mesmos algoritmos em outras linguagens de programação, começando com **Go**.

A ideia é:

  * **Solidificar o entendimento** dos conceitos aprendidos no livro.
  * **Praticar a implementação** de algoritmos em diferentes paradigmas e sintaxes.
  * **Comparar abordagens** e nuances de implementação entre linguagens.

-----

## 🚀 Como Estruturar o Projeto

Você pode organizar os códigos por capítulo do livro ou por tipo de algoritmo. Uma sugestão de estrutura seria:

```
entendendo_algoritmos/
├── .vscode/
├── go.mod
├── README.md
│
├── capitulos/             
│   └── cap01_introducao_a_algoritmos/ 
│       ├── exemplos/
│       │   └── ex01_pesquisa_binaria/  
│       │       ├── go/
│       │       │   └── main.go
│       │       ├── python/
│       │       │   └── main.py
│       │       └── c/cpp/      
│       │           └── main.js
│       │
│       └── exemplos/
│           └── ex02_ordenacao_por_selecao/ # Exemplo 02 do Cap. 01
│               ├── go/
│               │   └── main.go
│               └── ...
│
│   └── exercicios/            # Exercícios ESPECÍFICOS do Capítulo 1
│       ├── 01_exercicio_x/    # Exercício 1 do Cap 1 (com nome descritivo)
│       │   ├── problema.md    # Descrição do problema
│       │   ├── solucao.go     # Sua solução Go
│       │   └── solucao.py     # Sua solução Python
│       │
│       └── 02_exercicio_y/
│           ├── problema.md
│           └── solucao.go
│
├── capitulos/
│   └── cap02_algoritmos_graficos/ 
│       ├── exemplos/
│       │   └── ex01_busca_em_largura/
│       │       ├── go/
│       │       │   └── main.go
│       │       └── python/
│       │           └── main.py
│       └── exercicios/
│           └── ...
│
└── ... 
```

-----

## 💻 Linguagens e Implementações

Atualmente, o foco principal é em:

  * **Go:** As implementações iniciais dos algoritmos estão sendo desenvolvidas em Go.

**Próximos Passos:**
Ainda estou considerando adicionar implementações em outras linguagens, dependendo da necessidade e do interesse.

-----

## Contribuições (Opcional)

Se outras pessoas forem se juntar ao projeto, você pode adicionar uma seção de "Como Contribuir". Algo como:

Sinta-se à vontade para explorar os códigos, propor melhorias ou até mesmo adicionar implementações em outras linguagens\!

-----

Espero que este `README.md` ajude a organizar e apresentar bem o seu projeto\!